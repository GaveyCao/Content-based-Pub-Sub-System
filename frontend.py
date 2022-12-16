from concurrent import futures
import time
import grpc
import pr_pb2
import pr_pb2_grpc
import _thread
import sys
import csv
from multiprocessing.dummy import Pool as ThreadPool
import json
import socket
from pymongo import MongoClient

CONNECTION_STRING = "mongodb+srv://ruihw95:89631139azrael@cluster0.cbxycjc.mongodb.net/?retryWrites=true&w=majority"
THRESHOLD = 1
TIMEOUT = 3


port = sys.argv[1]
SELF_IP = "172.31.25.104:" + str(port)


'''
Helper functions for starting
'''
def register_ip():
    channel = grpc.insecure_channel(CENTRAL_SERVER_IP)
    stub = pr_pb2_grpc.PublishTopicStub(channel)
    response = stub.registerIp(pr_pb2.ips(ip=SELF_IP))
    print("Ip added to central server...\n")

'''
Helper functions for publish
'''
# query topic server ip from central server
def queryTopicIp(request):
    channel = grpc.insecure_channel(CENTRAL_SERVER_IP)
    stub = pr_pb2_grpc.PublishTopicStub(channel)
    responses = stub.giveIps(pr_pb2.topic(topic=request.topic))
    return responses

# send data from front end server to topic server
def publishData(lst):
    request = lst[0]
    accesspoint = lst[1]
    channel = grpc.insecure_channel(accesspoint)
    stub = pr_pb2_grpc.PublishTopicStub(channel)

    response = stub.publish(pr_pb2.topicData(topic=request.topic, data=request.data))
    print(response.ack)
    return response.ack

# query subscriber ip from topic server
def querySubscriberIp(request):
    channel = grpc.insecure_channel(CENTRAL_SERVER_IP)
    stub = pr_pb2_grpc.PublishTopicStub(channel)
    responses = stub.giveSubscriberIps(pr_pb2.topicSubscribe(topic=request.topic, client_ip=SELF_IP))
    return responses

# send message from topic server to front end server
def sendToFrontend(lst):
    request = lst[0]
    client_ip = lst[1]
    channel = grpc.insecure_channel(client_ip)
    stub = pr_pb2_grpc.PublishTopicStub(channel)
    response = stub.sendData(request)

'''
Helper functions for load balancing
'''
# replicate topic server
def replicateTopicServer(request):
    channel = grpc.insecure_channel(CENTRAL_SERVER_IP)
    stub = pr_pb2_grpc.PublishTopicStub(channel)
    response = stub.replicaRequest(pr_pb2.topicSubscribe(topic=request.topic, client_ip=SELF_IP))
    return response

# dereplicate topic server
def dereplicateTopicServer(topic):
    channel = grpc.insecure_channel(CENTRAL_SERVER_IP)
    stub = pr_pb2_grpc.PublishTopicStub(channel)
    response = stub.deReplicaRequest(pr_pb2.topicSubscribe(topic=topic, client_ip=SELF_IP))
    return response
'''
Helper functions for send messages back to client
'''
# generate message
def generateBackup(topic,lst) :
    for data in lst:
        yield pr_pb2.topicData(topic=topic,data=data)

# send message from front end server to client
def forwardBackupToClient(lst):
    requestList = lst[0]
    client_ip = lst[1]
    lst = []
    temp_topic = ""
    for request in requestList:
        lst.append(request.data)
        temp_topic = request.topic
    channel = grpc.insecure_channel(client_ip)
    stub = pr_pb2_grpc.PublishTopicStub(channel)
    response = stub.forwardBackup(generateBackup(temp_topic, lst))

'''
gRPC FrontEnd server/Topic server class
'''
class AccessPoint(pr_pb2_grpc.PublishTopicServicer):
    '''
    Front end server
    '''

    '''
    Publish
    '''
    # send publish request to topic server
    def publishRequest(self, request, context):
        print("FRONTEND : Data received for topic : "+request.topic)
        # query topic server ips
        responses = queryTopicIp(request)
        returned_ips = []
        for response in responses:
            print("FRONTEND : Data to be sent to topic server IP: " + response.ip + " for topic: "+request.topic)
            returned_ips.append(response.ip)
        lst = []
        pool = ThreadPool(len(returned_ips))
        for returned_ip in returned_ips:
            lst.append([request, returned_ip])
        # publish messages to topic servers
        results = pool.map(publishData, lst)
        return pr_pb2.acknowledge(ack="Published in "+str(len(results))+" topic servers")

    '''
    Subscribe
    '''
    # send subscribe request to central server
    def subscribeRequest(self, request, context):
        print("\nFRONTEND : new client subscriber ", request.client_ip, " for topic", request.topic)
        find = {"topic": request.topic}
        if subscribers.count_documents(find) > 0:
            print("FRONTEND : Not the first client for topic ", request.topic)
            subType = "old"
        else:
            print("FRONTEND : First client for topic ", request.topic)
            subType = "new"

        newSubscribers.insert_one({"topic": request.topic, "ip": request.client_ip})
        # add topic subscribers
        subscribers.insert_one({"topic": request.topic, "ip": request.client_ip})

        # ask for replicate if subscriber for topic exceeds threshold
        if subscribers.count_documents(find) > THRESHOLD:
            print("Too many subscribers! start load balancing ......\n")
            response = replicateTopicServer(request)

        channel = grpc.insecure_channel(CENTRAL_SERVER_IP)
        stub = pr_pb2_grpc.PublishTopicStub(channel)
        response = stub.subscribeRequestCentral(pr_pb2.topicDataType(topic=request.topic, client_ip=SELF_IP, type=subType))
        return pr_pb2.acknowledge(ack="temporary acknowledge")

    # send messages back to new subscribed client
    def sendBackup(self, request_iterator, context):
        requestList = []
        topic = ""
        for request in request_iterator:
            requestList.append(request)
            topic = request.topic

        find = {"topic": topic}
        pool = ThreadPool(newSubscribers.count_documents(find))
        lst = []
        cursor = newSubscribers.find({"topic": topic})
        for document in cursor:
            lst.append([requestList, document["ip"]])
        results = pool.map(forwardBackupToClient, lst)
        newSubscribers.delete_many({"topic": topic})
        return pr_pb2.acknowledge(ack="complete data backup received and forwarded to resepective clients...")

    # Add data to replica server
    def sendBackupReplica(self, request_iterator, context):
        requestList = []
        for request in request_iterator:
            requestList.append(request)
        for request in requestList:
            dataDump.insert_one({"topic": request.topic, "data": request.data})
            topic = request.topic
        print("Replication complete for topic : "+topic)
        return pr_pb2.acknowledge(ack="complete data backup received by the replica...")

    '''
    Unsubscribe
    '''
    # Unsubscribe client from topic
    def unsubscribeRequest(self, request_iterator, context):
        topicList = []
        for request in request_iterator:
            print("FRONTEND : Unsubscribe request from client", request.client_ip, " for topic", request.topic)
            client_ip = request.client_ip
            topicList.append(request.topic)
        for topic in topicList:
            # delete subscribers
            subscribers.delete_one({"topic": topic, "ip": client_ip})
            find = {"topic": topic}
            count = subscribers.count_documents(find)
            # derepricate front servers if subscriber drop below threshold
            if 0 < count <= THRESHOLD:
                print("Too little subscribers!\n")
                response = dereplicateTopicServer(topic)
                if response.ack == "DONE":
                    dataDump.delete_many({"topic": topic})
                    print("TOPIC_SERVER : Dereplicated for topic :", topic)
            else:
                channel = grpc.insecure_channel(CENTRAL_SERVER_IP)
                stub = pr_pb2_grpc.PublishTopicStub(channel)
                response = stub.unsubscribeRequestCentral(pr_pb2.topicSubscribe(topic=topic, client_ip=SELF_IP))
        return pr_pb2.acknowledge(ack="done")

    '''
    Topic server
    '''

    '''
    Publish
    '''
    # send publish data to topic server
    def publish(self, request, context):
        print("TOPIC_SERVER : Data received for topic : "+request.topic)
        dataDump.insert_one({"topic": request.topic, "data": request.data})
        # query subscriber ips
        responses = querySubscriberIp(request)
        ipList = []
        for response in responses:
            ipList.append(response.ip)
            print("TOPIC_SERVER : frontend subscriber IP received: " + response.ip +" for topic: "+request.topic)
        if ipList == [] or ipList[0] == 'none':
            return pr_pb2.acknowledge(ack="No subscribers for this replica")
        pool = ThreadPool(len(ipList))
        lst = []
        for client_ip in ipList:
            lst.append([request, client_ip])
        results = pool.map(sendToFrontend, lst)
        print('d')
        return pr_pb2.acknowledge(ack="Data send to clients complete")

    # topic server send data to front end server
    def sendData(self, request, context):
        find = {"topic": request.topic}
        pool = ThreadPool(subscribers.count_documents(find))
        lst = []
        for document in subscribers.find(find):
            lst.append([[request], document["ip"]])
        results = pool.map(forwardBackupToClient, lst)
        return pr_pb2.acknowledge(ack="data sent to subscribed clients")

    '''
    Subscribe
    '''
    # send topic and data to subscribed client
    def sendBackupRequest(self, request, context):
        cursor = dataDump.find({"topic": request.topic})
        lst = []
        for document in cursor:
            lst.append(document["data"])
        channel = grpc.insecure_channel(request.client_ip)
        stub = pr_pb2_grpc.PublishTopicStub(channel)
        response = stub.sendBackup(generateBackup(request.topic, lst))
        return pr_pb2.acknowledge(ack="data send to : "+request.client_ip+" complete...")

    # send topic and data to new replica front server
    def sendBackupRequestReplica(self, request, context):
        print("TOPIC_SERVER : Sending data backup for topic : "+request.topic+" to the new replica : "+request.client_ip)
        cursor = dataDump.find({"topic": request.topic})
        lst = []
        for document in cursor:
            lst.append(document["data"])
        channel = grpc.insecure_channel(request.client_ip)
        stub = pr_pb2_grpc.PublishTopicStub(channel)
        response = stub.sendBackupReplica(generateBackup(request.topic,lst))
        return pr_pb2.acknowledge(ack="data send to : "+request.client_ip+" replica complete...")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pr_pb2_grpc.add_PublishTopicServicer_to_server(AccessPoint(), server)
    server.add_insecure_port(SELF_IP)
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    # read virtual server ip
    # change to corresponding virtual server ip if needed
    CENTRAL_SERVER_IP = '172.31.26.237:50051'
    # register self ip to virtual server
    register_ip()

    mongoClient = MongoClient(CONNECTION_STRING)
    mongoClient.drop_database('Frontend'+port)
    db = mongoClient['Frontend'+port]
    dataDump = db["dataDump"]
    subscribers = db["subscribers"]
    newSubscribers = db["newSubscribers"]

    serve()