# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import service_pb2 as service__pb2


class TransfersServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetTransfers = channel.unary_stream(
                '/TransfersService/GetTransfers',
                request_serializer=service__pb2.GetTransfersRequest.SerializeToString,
                response_deserializer=service__pb2.TokenTransfer.FromString,
                )


class TransfersServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetTransfers(self, request, context):
        """Get all NFT transfers in a range, inclusive of the
        lower, exclusive of the higher
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TransfersServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetTransfers': grpc.unary_stream_rpc_method_handler(
                    servicer.GetTransfers,
                    request_deserializer=service__pb2.GetTransfersRequest.FromString,
                    response_serializer=service__pb2.TokenTransfer.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'TransfersService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TransfersService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetTransfers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/TransfersService/GetTransfers',
            service__pb2.GetTransfersRequest.SerializeToString,
            service__pb2.TokenTransfer.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)