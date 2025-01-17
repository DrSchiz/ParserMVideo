# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import grpc_pb2 as grpc__pb2


class ProductServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Product = channel.unary_unary(
                '/ProductService/Product',
                request_serializer=grpc__pb2.ClientRequest.SerializeToString,
                response_deserializer=grpc__pb2.ClientResponse.FromString,
                )


class ProductServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Product(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProductServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Product': grpc.unary_unary_rpc_method_handler(
                    servicer.Product,
                    request_deserializer=grpc__pb2.ClientRequest.FromString,
                    response_serializer=grpc__pb2.ClientResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ProductService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ProductService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Product(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ProductService/Product',
            grpc__pb2.ClientRequest.SerializeToString,
            grpc__pb2.ClientResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class CommentServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Com = channel.unary_unary(
                '/CommentService/Com',
                request_serializer=grpc__pb2.CommentRequest.SerializeToString,
                response_deserializer=grpc__pb2.CommentResponse.FromString,
                )


class CommentServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Com(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CommentServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Com': grpc.unary_unary_rpc_method_handler(
                    servicer.Com,
                    request_deserializer=grpc__pb2.CommentRequest.FromString,
                    response_serializer=grpc__pb2.CommentResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'CommentService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CommentService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Com(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/CommentService/Com',
            grpc__pb2.CommentRequest.SerializeToString,
            grpc__pb2.CommentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
