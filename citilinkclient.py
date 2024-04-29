import grpc_pb2_grpc
import grpc_pb2
import grpc

def run():
    with grpc.insecure_channel('localhost:8082') as channel:
        stub = grpc_pb2_grpc.ProductServiceStub(channel)
        product_request = grpc_pb2.ClientRequest()
        res = stub.Product(product_request)
        print(res)

if __name__ == "__main__":
    run()