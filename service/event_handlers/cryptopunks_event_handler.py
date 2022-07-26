from typing import List
from web3 import Web3

from web3.types import LogReceipt

from .token_event_handler import TokenEventHandler
from ..service_pb2 import TokenTransfer
from ..utils import uint256_to_address


class CryptopunksEventHandler(TokenEventHandler):
    def event_abis(self) -> List[str]:
        return ["PunkTransfer(address,address,uint256)"]

    def parse_transfers(self, log: LogReceipt) -> List[TokenTransfer]:
        return [TokenTransfer(
            address=Web3.toChecksumAddress(log.address),
            from_address=uint256_to_address(hexbytes=log.topics[1]),
            to_address=uint256_to_address(hexbytes=log.topics[2]),
            token_id=str(Web3.toInt(hexstr=log.data)),
            transaction_hash=log.transactionHash.hex(),
            block_number=log.blockNumber,
            log_index=log.logIndex,
            chain_id=1,
            block_hash=log.blockHash.hex(),
            tx_index=log.transactionIndex
        )]
