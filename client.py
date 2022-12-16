from concurrent import futures
import time
import grpc
import pr_pb2
import pr_pb2_grpc
import _thread
import sys
import json
import socket
from pymongo import MongoClient

CONNECTION_STRING = "mongodb+srv://ruihw95:89631139azrael@cluster0.cbxycjc.mongodb.net/?retryWrites=true&w=majority"


port = sys.argv[1]
SELF_IP = "172.31.25.104:" + str(port)


'''
gRPC Client server class
'''
class Client(pr_pb2_grpc.PublishTopicServicer):
    # gRPC method for receive subscribed topic messages
    def forwardBackup(self, request_iterator, context):
        for request in request_iterator:
            print("\nReceived new data...")
            print(request)
            dataDump.insert_one({"topic": request.topic, "data": request.data})
        return pr_pb2.acknowledge(ack="Data received by the client...")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pr_pb2_grpc.add_PublishTopicServicer_to_server(Client(), server)
    server.add_insecure_port(SELF_IP)
    server.start()
    server.wait_for_termination()

'''
Helper functions for connection
'''
# get frontend server ip from central server
def get_frontend_ip():
    channel = grpc.insecure_channel(CENTRAL_SERVER_IP)
    stub = pr_pb2_grpc.PublishTopicStub(channel)
    response = stub.getFrontIp(pr_pb2.empty())
    print("Frontend server Ip allocated: " + response.ip + "\n")
    if response.ip == "NONE":
        print("No frontend servers active ...exiting...\n")
        exit(1)
    return response.ip

'''
Helper functions for publish
'''
def publish_topic(topic,data):
    channel = grpc.insecure_channel(FRONT_END_SERVER_IP)
    stub = pr_pb2_grpc.PublishTopicStub(channel)
    response = stub.publishRequest(pr_pb2.topicData(topic=topic, data=data))
    print("Ack received: " + response.ack)

'''
Helper function for subscribe
'''
# query available topics from central server
def query_topic():
    channel = grpc.insecure_channel(CENTRAL_SERVER_IP)
    stub = pr_pb2_grpc.PublishTopicStub(channel)
    responses = stub.querryTopics(pr_pb2.empty())
    return responses

# find new unsubscribed topics
def find_new_topic(responses):
    topicList = []
    for response in responses:
        topicList.append(response.topic)

    cursor = subscribedTopics.find({})
    subscribedTopicsList = []
    for document in cursor:
        subscribedTopicsList.append(document["topic"])
    newTopicList = list(set(topicList) - set(subscribedTopicsList))
    return newTopicList

# send subscribe request to central server
def subscribe_topic(topic, self_ip):
    find = {"topic": topic}
    if subscribedTopics.count_documents(find) > 0:
        print("Already subscribed to the topic :", topic)
    else:
        channel = grpc.insecure_channel(FRONT_END_SERVER_IP)
        stub = pr_pb2_grpc.PublishTopicStub(channel)
        response = stub.subscribeRequest(pr_pb2.topicSubscribe(topic=topic, client_ip=self_ip))
        subscribedTopics.insert_one({"topic": topic})

'''
Helper function for unsubscribe
'''
# generate topics to unsubscribe
def generateTopics(lst, client_ip):
    for topic in lst:
        yield pr_pb2.topicSubscribe(topic=topic, client_ip=client_ip)


if __name__ == '__main__':
    _thread.start_new_thread(serve, ())

    mongoClient = MongoClient(CONNECTION_STRING)
    mongoClient.drop_database('Client'+port)
    db = mongoClient['Client'+port]
    subscribedTopics = db["subscribedTopics"]
    dataDump = db["dataDump"]

    # read virtual server ip
    CENTRAL_SERVER_IP = '172.31.26.237:50051'
    # getting front end server ip
    FRONT_END_SERVER_IP = get_frontend_ip()

    print("Connection all established!\n")

    while True:
        print("Type 1 for publish\nType 2 for subscribe\nType 3 for unsubscribe\nType 4 for exit\n")
        response = input()

        if response == "1":
            print("Enter topic")
            topic = input()
            print("Enter message")
            data = input()
            publish_topic(topic, data)

        elif response == "2":
            responses = query_topic()
            newTopicList = find_new_topic(responses)

            for i, topic in enumerate(newTopicList):
                print(i, ": ", topic)

            if len(newTopicList) > 0:
                print("Select available unsubscribed topic from above choices :")
                selectedNumber = input()
                try:
                    if int(selectedNumber) < len(newTopicList):
                        subscribe_topic(newTopicList[int(selectedNumber)], SELF_IP)
                    else:
                        print("Invalid option selected ...")
                except:
                    print("Invalid option selected ...")

            else:
                print("No new topics found ...")

        elif response == "3":
            # show all subscribed topics
            cursor = subscribedTopics.find({})
            lst = []
            for i, document in enumerate(cursor):
                print(i, ": " + document["topic"])
                lst.append(document["topic"])
            unsubscribeList = []
            if len(lst) > 0:
                print("Select topics from above choices, seperated by spaces:")
                selectedNumbers = input().split()
                for selectedNumber in selectedNumbers:
                    try:
                        if int(selectedNumber) < len(lst):
                            unsubscribeList.append(str(lst[int(selectedNumber)]))
                        else:
                            print("Invalid options selected ...")
                            unsubscribeList = []
                            break

                    except:
                        unsubscribeList = []
                        print("Invalid options selected ...")

            else:
                print("No topics subscribed to ...")
            if len(unsubscribeList) > 0:
                channel = grpc.insecure_channel(FRONT_END_SERVER_IP)
                stub = pr_pb2_grpc.PublishTopicStub(channel)
                response = stub.unsubscribeRequest(generateTopics(unsubscribeList, SELF_IP))
                for topic in unsubscribeList:
                    subscribedTopics.delete_one({"topic": topic})
                print("unsubscribed from topics :", unsubscribeList)

        elif response == "4":
            cursor = subscribedTopics.find({})
            lst = []
            for document in cursor:
                lst.append(document["topic"])
            channel = grpc.insecure_channel(FRONT_END_SERVER_IP)
            stub = pr_pb2_grpc.PublishTopicStub(channel)
            response = stub.unsubscribeRequest(generateTopics(lst, SELF_IP))
            mongoClient.drop_database('Client' + port)
            print("exiting now...")
            exit(0)

        else:
            print("Invalid option selected, try again...")