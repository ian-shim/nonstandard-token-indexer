from typing import List
from web3 import Web3

from web3.types import LogReceipt

from .token_event_handler import TokenEventHandler
from ..service_pb2 import TokenTransfer
from ..utils import uint256_to_address, decode_data


class ERC1155EventHandler(TokenEventHandler):
    def event_abis(self) -> List[str]:
        return [
            "TransferSingle(address,address,address,uint256,uint256)",
            "TransferBatch(address,address,address,uint256[],uint256[])"
        ]

    def parse_transfers(self, log: LogReceipt) -> List[TokenTransfer]:
        if log.topics[0] == Web3.keccak(text="TransferSingle(address,address,address,uint256,uint256)"):
            [token_id, value] = decode_data(["uint256", "uint256"], log.data)
            return [TokenTransfer(
                address=Web3.toChecksumAddress(log.address),
                from_address=uint256_to_address(hexbytes=log.topics[2]),
                to_address=uint256_to_address(hexbytes=log.topics[3]),
                token_id=str(token_id),
                transaction_hash=log.transactionHash.hex(),
                block_number=log.blockNumber,
                log_index=log.logIndex,
                chain_id=1,
                block_hash=log.blockHash.hex(),
                tx_index=log.transactionIndex
            )]

        elif log.topics[0] == Web3.keccak(text="TransferBatch(address,address,address,uint256[],uint256[])"):
            [token_ids, _] = decode_data(["uint256[]", "uint256[]"], log.data)
            return [TokenTransfer(
                address=Web3.toChecksumAddress(log.address),
                from_address=uint256_to_address(hexbytes=log.topics[2]),
                to_address=uint256_to_address(hexbytes=log.topics[3]),
                token_id=str(token_id),
                transaction_hash=log.transactionHash.hex(),
                block_number=log.blockNumber,
                log_index=log.logIndex,
                chain_id=1,
                block_hash=log.blockHash.hex(),
                tx_index=log.transactionIndex
            ) for token_id in token_ids]
