import grpc
from concurrent import futures
import logging
from service.service_pb2_grpc import add_TransfersServiceServicer_to_server
from service.transfers_service import TransfersService
from dotenv import load_dotenv
import os

load_dotenv()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_TransfersServiceServicer_to_server(
        TransfersService(os.getenv("ETHEREUM_NODE_URL")), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
