import unittest
from unittest.mock import MagicMock
from web3 import Web3

from service.event_handlers.cryptopunks_event_handler import CryptopunksEventHandler
from .fixtures import LOGS


class TestCryptopunksEventHandler(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.provider = Web3(Web3.HTTPProvider('https://randomurl.com'))
        self.handler = CryptopunksEventHandler(self.provider)

    def test_event_topics(self):
        self.assertEqual(self.handler.event_topics(), [
                         "0x05af636b70da6819000c49f85b21fa82081c632069bb626f30932034099107d8"])
        
    def test_parse_transfers(self):
        self.provider.eth.get_logs = MagicMock(return_value=LOGS['cryptopunks'])
        logs = self.handler.fetch_logs('0x', 123, 456)

        transfer = self.handler.parse_transfers(logs[0])[0]

        self.assertEqual(transfer.address,
                            "0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB")
        self.assertEqual(transfer.from_address,
                         "0x1919DB36cA2fa2e15F9000fd9CdC2EdCF863E685")
        self.assertEqual(transfer.to_address,
                         "0x0232d1083E970F0c78f56202b9A666B526FA379F")
        self.assertEqual(transfer.token_id, '7845')
        self.assertEqual(transfer.transaction_hash,
                         '0x9af18816f53aa7305b9dc03049430644e01d3baf051a362aa8433b68a27c7519')
        self.assertEqual(transfer.block_number, 15213919)
        self.assertEqual(transfer.log_index, 76)
        self.assertEqual(transfer.chain_id, 1)
        self.assertEqual(
            transfer.block_hash, '0xe5a2abc79ed24621ed4dd2d9f94a2b383b18123a804bd7022cb2bb0015feb1fb')
        self.assertEqual(transfer.tx_index, 42)
