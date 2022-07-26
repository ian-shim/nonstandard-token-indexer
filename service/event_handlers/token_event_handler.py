from abc import ABC, abstractmethod
from typing import List
from eth_typing import BlockIdentifier
from web3 import Web3
from web3.types import LogReceipt
from ..service_pb2 import TokenTransfer


class TokenEventHandler(ABC):
    def __init__(self, provider: Web3):
        self.provider = provider

    @property
    @abstractmethod
    def event_abis(self) -> List[str]:
        pass

    @abstractmethod
    def parse_transfers(self, log: LogReceipt) -> List[TokenTransfer]:
        pass

    def event_topics(self) -> List[str]:
        return [Web3.keccak(text=abi).hex() for abi in self.event_abis()]

    def fetch_logs(self, address: str, from_block: BlockIdentifier, to_block: BlockIdentifier) -> List[LogReceipt]:
        return self.provider.eth.get_logs({
            'fromBlock': from_block,
            # toBlock in this API is inclusive. Subtract 1 to make it exclusive
            'toBlock': to_block - 1,
            'address': address,
            'topics': [self.event_topics()]
        })
