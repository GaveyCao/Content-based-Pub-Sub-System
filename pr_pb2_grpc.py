# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import pr_pb2 as pr__pb2


class PublishTopicStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.publishRequest = channel.unary_unary(
                '/PublishTopic/publishRequest',
                request_serializer=pr__pb2.topicData.SerializeToString,
                response_deserializer=pr__pb2.acknowledge.FromString,
                )
        self.subscribeRequest = channel.unary_unary(
                '/PublishTopic/subscribeRequest',
                request_serializer=pr__pb2.topicSubscribe.SerializeToString,
                response_deserializer=pr__pb2.acknowledge.FromString,
                )
        self.subscribeRequestCentral = channel.unary_unary(
                '/PublishTopic/subscribeRequestCentral',
                request_serializer=pr__pb2.topicDataType.SerializeToString,
                response_deserializer=pr__pb2.acknowledge.FromString,
                )
        self.giveIps = channel.unary_stream(
                '/PublishTopic/giveIps',
                request_serializer=pr__pb2.topic.SerializeToString,
                response_deserializer=pr__pb2.ips.FromString,
                )
        self.publish = channel.unary_unary(
                '/PublishTopic/publish',
                request_serializer=pr__pb2.topicData.SerializeToString,
                response_deserializer=pr__pb2.acknowledge.FromString,
                )
        self.getFrontIp = channel.unary_unary(
                '/PublishTopic/getFrontIp',
                request_serializer=pr__pb2.empty.SerializeToString,
                response_deserializer=pr__pb2.ips.FromString,
                )
        self.registerIp = channel.unary_unary(
                '/PublishTopic/registerIp',
                request_serializer=pr__pb2.ips.SerializeToString,
                response_deserializer=pr__pb2.acknowledge.FromString,
                )
        self.sendBackupRequest = channel.unary_unary(
                '/PublishTopic/sendBackupRequest',
                request_serializer=pr__pb2.topicSubscribe.SerializeToString,
                response_deserializer=pr__pb2.acknowledge.FromString,
                )
        self.sendBackup = channel.stream_unary(
                '/PublishTopic/sendBackup',
                request_serializer=pr__pb2.topicData.SerializeToString,
                response_deserializer=pr__pb2.acknowledge.FromString,
                )
        self.forwardBackup = channel.stream_unary(
                '/PublishTopic/forwardBackup',
                request_serializer=pr__pb2.topicData.SerializeToString,
                response_deserializer=pr__pb2.acknowledge.FromString,
                )
        self.giveSubscriberIps = channel.unary_stream(
                '/PublishTopic/giveSubscriberIps',
                request_serializer=pr__pb2.topicSubscribe.SerializeToString,
                response_deserializer=pr__pb2.ips.FromString,
                )
        self.sendData = channel.unary_unary(
                '/PublishTopic/sendData',
                request_serializer=pr__pb2.topicData.SerializeToString,
                response_deserializer=pr__pb2.acknowledge.FromString,
                )
        self.replicaRequest = channel.unary_unary(
                '/PublishTopic/replicaRequest',
                request_serializer=pr__pb2.topicSubscribe.SerializeToString,
                response_deserializer=pr__pb2.acknowledge.FromString,
                )
        self.querryTopics = channel.unary_stream(
                '/PublishTopic/querryTopics',
                request_serializer=pr__pb2.empty.SerializeToString,
                response_deserializer=pr__pb2.topic.FromString,
                )
        self.sendBackupRequestReplica = channel.unary_unary(
                '/PublishTopic/sendBackupRequestReplica',
                request_serializer=pr__pb2.topicSubscribe.SerializeToString,
                response_deserializer=pr__pb2.acknowledge.FromString,
                )
        self.sendBackupReplica = channel.stream_unary(
                '/PublishTopic/sendBackupReplica',
                request_serializer=pr__pb2.topicData.SerializeToString,
                response_deserializer=pr__pb2.acknowledge.FromString,
                )
        self.unsubscribeRequest = channel.stream_unary(
                '/PublishTopic/unsubscribeRequest',
                request_serializer=pr__pb2.topicSubscribe.SerializeToString,
                response_deserializer=pr__pb2.acknowledge.FromString,
                )
        self.deReplicaRequest = channel.unary_unary(
                '/PublishTopic/deReplicaRequest',
                request_serializer=pr__pb2.topicSubscribe.SerializeToString,
                response_deserializer=pr__pb2.acknowledge.FromString,
                )
        self.unsubscribeRequestCentral = channel.unary_unary(
                '/PublishTopic/unsubscribeRequestCentral',
                request_serializer=pr__pb2.topicSubscribe.SerializeToString,
                response_deserializer=pr__pb2.acknowledge.FromString,
                )
        self.commit_request = channel.unary_unary(
                '/PublishTopic/commit_request',
                request_serializer=pr__pb2.commit_req_data.SerializeToString,
                response_deserializer=pr__pb2.acknowledge.FromString,
                )
        self.commit_phase_two = channel.unary_unary(
                '/PublishTopic/commit_phase_two',
                request_serializer=pr__pb2.commit_req_data.SerializeToString,
                response_deserializer=pr__pb2.acknowledge.FromString,
                )
        self.upgradeBackup = channel.unary_unary(
                '/PublishTopic/upgradeBackup',
                request_serializer=pr__pb2.empty.SerializeToString,
                response_deserializer=pr__pb2.acknowledge.FromString,
                )
        self.giveDataPhaseOne = channel.unary_unary(
                '/PublishTopic/giveDataPhaseOne',
                request_serializer=pr__pb2.empty.SerializeToString,
                response_deserializer=pr__pb2.topic.FromString,
                )
        self.giveDataPhaseTwo = channel.unary_unary(
                '/PublishTopic/giveDataPhaseTwo',
                request_serializer=pr__pb2.empty.SerializeToString,
                response_deserializer=pr__pb2.acknowledge.FromString,
                )
        self.getMasterIp = channel.unary_unary(
                '/PublishTopic/getMasterIp',
                request_serializer=pr__pb2.empty.SerializeToString,
                response_deserializer=pr__pb2.ips.FromString,
                )
        self.getBackupIp = channel.unary_unary(
                '/PublishTopic/getBackupIp',
                request_serializer=pr__pb2.empty.SerializeToString,
                response_deserializer=pr__pb2.ips.FromString,
                )


class PublishTopicServicer(object):
    """Missing associated documentation comment in .proto file."""

    def publishRequest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def subscribeRequest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def subscribeRequestCentral(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def giveIps(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def publish(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getFrontIp(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def registerIp(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def sendBackupRequest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def sendBackup(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def forwardBackup(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def giveSubscriberIps(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def sendData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def replicaRequest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def querryTopics(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def sendBackupRequestReplica(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def sendBackupReplica(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def unsubscribeRequest(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def deReplicaRequest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def unsubscribeRequestCentral(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def commit_request(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def commit_phase_two(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def upgradeBackup(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def giveDataPhaseOne(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def giveDataPhaseTwo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getMasterIp(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getBackupIp(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PublishTopicServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'publishRequest': grpc.unary_unary_rpc_method_handler(
                    servicer.publishRequest,
                    request_deserializer=pr__pb2.topicData.FromString,
                    response_serializer=pr__pb2.acknowledge.SerializeToString,
            ),
            'subscribeRequest': grpc.unary_unary_rpc_method_handler(
                    servicer.subscribeRequest,
                    request_deserializer=pr__pb2.topicSubscribe.FromString,
                    response_serializer=pr__pb2.acknowledge.SerializeToString,
            ),
            'subscribeRequestCentral': grpc.unary_unary_rpc_method_handler(
                    servicer.subscribeRequestCentral,
                    request_deserializer=pr__pb2.topicDataType.FromString,
                    response_serializer=pr__pb2.acknowledge.SerializeToString,
            ),
            'giveIps': grpc.unary_stream_rpc_method_handler(
                    servicer.giveIps,
                    request_deserializer=pr__pb2.topic.FromString,
                    response_serializer=pr__pb2.ips.SerializeToString,
            ),
            'publish': grpc.unary_unary_rpc_method_handler(
                    servicer.publish,
                    request_deserializer=pr__pb2.topicData.FromString,
                    response_serializer=pr__pb2.acknowledge.SerializeToString,
            ),
            'getFrontIp': grpc.unary_unary_rpc_method_handler(
                    servicer.getFrontIp,
                    request_deserializer=pr__pb2.empty.FromString,
                    response_serializer=pr__pb2.ips.SerializeToString,
            ),
            'registerIp': grpc.unary_unary_rpc_method_handler(
                    servicer.registerIp,
                    request_deserializer=pr__pb2.ips.FromString,
                    response_serializer=pr__pb2.acknowledge.SerializeToString,
            ),
            'sendBackupRequest': grpc.unary_unary_rpc_method_handler(
                    servicer.sendBackupRequest,
                    request_deserializer=pr__pb2.topicSubscribe.FromString,
                    response_serializer=pr__pb2.acknowledge.SerializeToString,
            ),
            'sendBackup': grpc.stream_unary_rpc_method_handler(
                    servicer.sendBackup,
                    request_deserializer=pr__pb2.topicData.FromString,
                    response_serializer=pr__pb2.acknowledge.SerializeToString,
            ),
            'forwardBackup': grpc.stream_unary_rpc_method_handler(
                    servicer.forwardBackup,
                    request_deserializer=pr__pb2.topicData.FromString,
                    response_serializer=pr__pb2.acknowledge.SerializeToString,
            ),
            'giveSubscriberIps': grpc.unary_stream_rpc_method_handler(
                    servicer.giveSubscriberIps,
                    request_deserializer=pr__pb2.topicSubscribe.FromString,
                    response_serializer=pr__pb2.ips.SerializeToString,
            ),
            'sendData': grpc.unary_unary_rpc_method_handler(
                    servicer.sendData,
                    request_deserializer=pr__pb2.topicData.FromString,
                    response_serializer=pr__pb2.acknowledge.SerializeToString,
            ),
            'replicaRequest': grpc.unary_unary_rpc_method_handler(
                    servicer.replicaRequest,
                    request_deserializer=pr__pb2.topicSubscribe.FromString,
                    response_serializer=pr__pb2.acknowledge.SerializeToString,
            ),
            'querryTopics': grpc.unary_stream_rpc_method_handler(
                    servicer.querryTopics,
                    request_deserializer=pr__pb2.empty.FromString,
                    response_serializer=pr__pb2.topic.SerializeToString,
            ),
            'sendBackupRequestReplica': grpc.unary_unary_rpc_method_handler(
                    servicer.sendBackupRequestReplica,
                    request_deserializer=pr__pb2.topicSubscribe.FromString,
                    response_serializer=pr__pb2.acknowledge.SerializeToString,
            ),
            'sendBackupReplica': grpc.stream_unary_rpc_method_handler(
                    servicer.sendBackupReplica,
                    request_deserializer=pr__pb2.topicData.FromString,
                    response_serializer=pr__pb2.acknowledge.SerializeToString,
            ),
            'unsubscribeRequest': grpc.stream_unary_rpc_method_handler(
                    servicer.unsubscribeRequest,
                    request_deserializer=pr__pb2.topicSubscribe.FromString,
                    response_serializer=pr__pb2.acknowledge.SerializeToString,
            ),
            'deReplicaRequest': grpc.unary_unary_rpc_method_handler(
                    servicer.deReplicaRequest,
                    request_deserializer=pr__pb2.topicSubscribe.FromString,
                    response_serializer=pr__pb2.acknowledge.SerializeToString,
            ),
            'unsubscribeRequestCentral': grpc.unary_unary_rpc_method_handler(
                    servicer.unsubscribeRequestCentral,
                    request_deserializer=pr__pb2.topicSubscribe.FromString,
                    response_serializer=pr__pb2.acknowledge.SerializeToString,
            ),
            'commit_request': grpc.unary_unary_rpc_method_handler(
                    servicer.commit_request,
                    request_deserializer=pr__pb2.commit_req_data.FromString,
                    response_serializer=pr__pb2.acknowledge.SerializeToString,
            ),
            'commit_phase_two': grpc.unary_unary_rpc_method_handler(
                    servicer.commit_phase_two,
                    request_deserializer=pr__pb2.commit_req_data.FromString,
                    response_serializer=pr__pb2.acknowledge.SerializeToString,
            ),
            'upgradeBackup': grpc.unary_unary_rpc_method_handler(
                    servicer.upgradeBackup,
                    request_deserializer=pr__pb2.empty.FromString,
                    response_serializer=pr__pb2.acknowledge.SerializeToString,
            ),
            'giveDataPhaseOne': grpc.unary_unary_rpc_method_handler(
                    servicer.giveDataPhaseOne,
                    request_deserializer=pr__pb2.empty.FromString,
                    response_serializer=pr__pb2.topic.SerializeToString,
            ),
            'giveDataPhaseTwo': grpc.unary_unary_rpc_method_handler(
                    servicer.giveDataPhaseTwo,
                    request_deserializer=pr__pb2.empty.FromString,
                    response_serializer=pr__pb2.acknowledge.SerializeToString,
            ),
            'getMasterIp': grpc.unary_unary_rpc_method_handler(
                    servicer.getMasterIp,
                    request_deserializer=pr__pb2.empty.FromString,
                    response_serializer=pr__pb2.ips.SerializeToString,
            ),
            'getBackupIp': grpc.unary_unary_rpc_method_handler(
                    servicer.getBackupIp,
                    request_deserializer=pr__pb2.empty.FromString,
                    response_serializer=pr__pb2.ips.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'PublishTopic', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PublishTopic(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def publishRequest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/PublishTopic/publishRequest',
            pr__pb2.topicData.SerializeToString,
            pr__pb2.acknowledge.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def subscribeRequest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/PublishTopic/subscribeRequest',
            pr__pb2.topicSubscribe.SerializeToString,
            pr__pb2.acknowledge.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def subscribeRequestCentral(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/PublishTopic/subscribeRequestCentral',
            pr__pb2.topicDataType.SerializeToString,
            pr__pb2.acknowledge.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def giveIps(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/PublishTopic/giveIps',
            pr__pb2.topic.SerializeToString,
            pr__pb2.ips.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def publish(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/PublishTopic/publish',
            pr__pb2.topicData.SerializeToString,
            pr__pb2.acknowledge.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getFrontIp(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/PublishTopic/getFrontIp',
            pr__pb2.empty.SerializeToString,
            pr__pb2.ips.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def registerIp(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/PublishTopic/registerIp',
            pr__pb2.ips.SerializeToString,
            pr__pb2.acknowledge.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def sendBackupRequest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/PublishTopic/sendBackupRequest',
            pr__pb2.topicSubscribe.SerializeToString,
            pr__pb2.acknowledge.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def sendBackup(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/PublishTopic/sendBackup',
            pr__pb2.topicData.SerializeToString,
            pr__pb2.acknowledge.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def forwardBackup(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/PublishTopic/forwardBackup',
            pr__pb2.topicData.SerializeToString,
            pr__pb2.acknowledge.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def giveSubscriberIps(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/PublishTopic/giveSubscriberIps',
            pr__pb2.topicSubscribe.SerializeToString,
            pr__pb2.ips.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def sendData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/PublishTopic/sendData',
            pr__pb2.topicData.SerializeToString,
            pr__pb2.acknowledge.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def replicaRequest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/PublishTopic/replicaRequest',
            pr__pb2.topicSubscribe.SerializeToString,
            pr__pb2.acknowledge.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def querryTopics(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/PublishTopic/querryTopics',
            pr__pb2.empty.SerializeToString,
            pr__pb2.topic.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def sendBackupRequestReplica(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/PublishTopic/sendBackupRequestReplica',
            pr__pb2.topicSubscribe.SerializeToString,
            pr__pb2.acknowledge.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def sendBackupReplica(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/PublishTopic/sendBackupReplica',
            pr__pb2.topicData.SerializeToString,
            pr__pb2.acknowledge.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def unsubscribeRequest(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/PublishTopic/unsubscribeRequest',
            pr__pb2.topicSubscribe.SerializeToString,
            pr__pb2.acknowledge.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def deReplicaRequest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/PublishTopic/deReplicaRequest',
            pr__pb2.topicSubscribe.SerializeToString,
            pr__pb2.acknowledge.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def unsubscribeRequestCentral(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/PublishTopic/unsubscribeRequestCentral',
            pr__pb2.topicSubscribe.SerializeToString,
            pr__pb2.acknowledge.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def commit_request(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/PublishTopic/commit_request',
            pr__pb2.commit_req_data.SerializeToString,
            pr__pb2.acknowledge.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def commit_phase_two(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/PublishTopic/commit_phase_two',
            pr__pb2.commit_req_data.SerializeToString,
            pr__pb2.acknowledge.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def upgradeBackup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/PublishTopic/upgradeBackup',
            pr__pb2.empty.SerializeToString,
            pr__pb2.acknowledge.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def giveDataPhaseOne(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/PublishTopic/giveDataPhaseOne',
            pr__pb2.empty.SerializeToString,
            pr__pb2.topic.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def giveDataPhaseTwo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/PublishTopic/giveDataPhaseTwo',
            pr__pb2.empty.SerializeToString,
            pr__pb2.acknowledge.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getMasterIp(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/PublishTopic/getMasterIp',
            pr__pb2.empty.SerializeToString,
            pr__pb2.ips.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getBackupIp(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/PublishTopic/getBackupIp',
            pr__pb2.empty.SerializeToString,
            pr__pb2.ips.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
