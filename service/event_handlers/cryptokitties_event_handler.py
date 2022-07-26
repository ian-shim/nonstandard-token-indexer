from typing import List
from web3 import Web3

from web3.types import LogReceipt

from .token_event_handler import TokenEventHandler
from ..service_pb2 import TokenTransfer
from ..utils import decode_data


class CryptoKittiesEventHandler(TokenEventHandler):
    def event_abis(self) -> List[str]:
        return ["Transfer(address,address,uint256)"]

    def parse_transfers(self, log: LogReceipt) -> List[TokenTransfer]:
        [from_address, to_address, token_id] = decode_data(
            ["address", "address", "uint256"], log.data)
        return [TokenTransfer(
            address=Web3.toChecksumAddress(log.address),
            from_address=from_address,
            to_address=to_address,
            token_id=str(Web3.toInt(token_id)),
            transaction_hash=log.transactionHash.hex(),
            block_number=log.blockNumber,
            log_index=log.logIndex,
            chain_id=1,
            block_hash=log.blockHash.hex(),
            tx_index=log.transactionIndex
        )]
