import logging
import grpc
from service import service_pb2_grpc, service_pb2

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = service_pb2_grpc.TransfersServiceStub(channel)

        from_block = 15218416
        to_block = 15218418
        address = "0x57f1887a8bf19b14fc0df6fd9b2acc9af147ea85"
        
        req = service_pb2.GetTransfersRequest(
            from_block=from_block,
            to_block=to_block,
            address=address
        )
        print("Looking up transfers from %i to %i at %s" %
              (from_block, to_block, address))
        
        transfers = stub.GetTransfers(req)
        for transfer in transfers:
            print(transfer)


if __name__ == '__main__':
    logging.basicConfig()
    run()
