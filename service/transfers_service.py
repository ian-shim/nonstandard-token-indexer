from .service_pb2_grpc import TransfersServiceServicer
from web3 import Web3

from .service_pb2 import GetTransfersRequest
from .event_handlers.cryptokitties_event_handler import CryptoKittiesEventHandler
from .event_handlers.cryptopunks_event_handler import CryptopunksEventHandler
from .event_handlers.erc721_event_handler import ERC721EventHandler
from .event_handlers.erc1155_event_handler import ERC1155EventHandler


class TransfersService(TransfersServiceServicer):
    def __init__(self, provider_url: str):
        if (provider_url is None or provider_url == ""):
            raise Exception("Please provide a valid Ethereum provider URL")
        self.web3_provider = Web3(Web3.HTTPProvider(provider_url))
        self.cryptopunks_event_handler = CryptopunksEventHandler(
            self.web3_provider)
        self.cryptokitties_event_handler = CryptoKittiesEventHandler(
            self.web3_provider)
        self.erc721_event_handler = ERC721EventHandler(self.web3_provider)
        self.erc1155_event_handler = ERC1155EventHandler(self.web3_provider)
        print("Ready to serve requests")

    def validate_request(self, request: GetTransfersRequest):
        assert(request.from_block is not None and request.from_block > 0)
        assert(request.to_block is not None and request.to_block > 0)
        assert(request.from_block < request.to_block)
        assert(request.address is not None and Web3.isAddress(request.address))

    def get_event_handler(self, address: str):
        if address == "0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB":
            return self.cryptopunks_event_handler
        elif address == "0x06012c8cf97BEaD5deAe237070F9587f8E7A266d":
            return self.cryptokitties_event_handler
        elif address == "0x76BE3b62873462d2142405439777e971754E8E77":
            return self.erc1155_event_handler
        else:
            return self.erc721_event_handler

    def GetTransfers(self, request: GetTransfersRequest, context):
        self.validate_request(request)
        checksum_address = Web3.toChecksumAddress(request.address)

        event_handler = self.get_event_handler(checksum_address)

        for log in event_handler.fetch_logs(checksum_address, request.from_block, request.to_block):
            for transfer in event_handler.parse_transfers(log):
                yield transfer
