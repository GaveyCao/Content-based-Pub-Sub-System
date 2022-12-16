from concurrent import futures
import time
import json
import grpc
import pr_pb2
import pr_pb2_grpc
import _thread
import random
import sys
import socket
from pymongo import MongoClient
import time

MASTER_IP = ""
BACKUP_IP = ""

# Connection url for MangoDB
CONNECTION_STRING = "mongodb+srv://ruihw95:89631139azrael@cluster0.cbxycjc.mongodb.net/?retryWrites=true&w=majority"

stub = ""
stub1 = ""

TIMEOUT = 3


def toggle_backup():
    global stub
    stub = pr_pb2_grpc.PublishTopicStub(grpc.insecure_channel(BACKUP_SERVER_IP))


def Forward(request, i):
    global stub
    retries = 0
    while (True):
        if retries >= 4:
            toggle_backup()
            retries = 0
        try:
            if i == 0:
                response = stub.unsubscribeRequestCentral(request, timeout=10)
                return response
            elif i == 1:
                response = stub.deReplicaRequest(request, timeout=10)
                print(response)
                return response
            elif i == 2:
                response = stub.replicaRequest(request, timeout=10)
                return response
            elif i == 3:
                response = stub.subscribeRequestCentral(request, timeout=10)
                return response
            elif i == 4:
                response = stub.getFrontIp(request, timeout=10)
                return response
            elif i == 5:
                response = stub.registerIp(request, timeout=10)
                return response

        except Exception as e:
            retries += 1
            print("master not reachable, retry\n")
            if retries >= 4:
                print("Master is down toggled to Backup")
            time.sleep(TIMEOUT)


def Forward_mult(request, i):
    global stub
    retries = 0
    while (True):
        if retries >= 4:
            toggle_backup()
            retries = 0
        try:
            if i == 0:
                responses = stub.querryTopics(request, timeout=10)
                return responses
            if i == 1:
                responses = stub.giveSubscriberIps(request, timeout=10)
                return responses
            if i == 2:
                responses = stub.giveIps(request, timeout=10)
                return responses
        except Exception as e:
            retries += 1
            print("master not reachable, retry \n")
            if retries >= 4:
                print("Master is down toggled to Backup")
            time.sleep(TIMEOUT)


class VirtualServer(pr_pb2_grpc.PublishTopicServicer):

    def getMasterIp(self, request, context):
        a = json.load(open("backup", "r"))
        return pr_pb2.ips(ip=a["CENTRAL_SERVER_IP"])

    def getBackupIp(self, request, context):
        a = json.load(open("backup", "r"))
        return pr_pb2.ips(ip=a["BACKUP_SERVER_IP"])

    def unsubscribeRequestCentral(self, request, context):
        response = Forward(request, 0)
        return response

    def deReplicaRequest(self, request, context):
        print("dereplica request received!\n")
        response = Forward(request, 1)
        return response

    def replicaRequest(self, request, context):
        print("replica request received!\n")
        response = Forward(request, 2)
        return response

    def subscribeRequestCentral(self, request, context):
        response = Forward(request, 3)
        return response

    def getFrontIp(self, request, context):
        print("get Front end server Ip request received!\n")
        response = Forward(request, 4)
        return response

    def registerIp(self, request, context):
        print("register IP request received!\n")
        response = Forward(request, 5)
        return response

    def querryTopics(self, request, context):
        responses = Forward_mult(request, 0)
        for response in responses:
            yield response

    def giveSubscriberIps(self, request, context):
        responses = Forward_mult(request, 1)
        for response in responses:
            yield response

    def giveIps(self, request, context):
        responses = Forward_mult(request, 2)
        print("give topic server ips!\n")
        for response in responses:
            yield response

    def upgradeBackup(self, request, context):
        print("toggle back up!\n")
        toggle_backup()
        return pr_pb2.acknowledge(ack="Connection is established!\n")


# run gRPC virtual server
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pr_pb2_grpc.add_PublishTopicServicer_to_server(VirtualServer(), server)
    server.add_insecure_port(VIRTUAL_SERVER_IP)
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    # meta data, change to corresponding meta data if needed
    BACKUP_SERVER_IP = '[::]:50053'
    CENTRAL_SERVER_IP = '[::]:50052'
    VIRTUAL_SERVER_IP = '[::]:50051'
    stub = pr_pb2_grpc.PublishTopicStub(grpc.insecure_channel(CENTRAL_SERVER_IP))


    print("Virtual server up...\n")

    serve()
