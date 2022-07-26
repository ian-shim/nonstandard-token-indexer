import unittest
from unittest.mock import MagicMock
from web3 import Web3
from service.event_handlers.cryptokitties_event_handler import CryptoKittiesEventHandler
from .fixtures import LOGS


class TestCryptokittiesEventHandler(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.provider = Web3(Web3.HTTPProvider('https://randomurl.com'))
        self.handler = CryptoKittiesEventHandler(self.provider)

    def test_event_topics(self):
        self.assertEqual(self.handler.event_topics(), [
                         "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"])
        
    def test_parse_transfers(self):
        self.provider.eth.get_logs = MagicMock(return_value=LOGS['cryptokitties'])
        logs = self.handler.fetch_logs('0x', 123, 456)

        transfer = self.handler.parse_transfers(logs[0])[0]

        self.assertEqual(transfer.address,
                         "0x06012c8cf97BEaD5deAe237070F9587f8E7A266d")
        self.assertEqual(transfer.from_address,
                         "0xcc9861c99bb22a5bd1261190ecf59a3fd1f7f720")
        self.assertEqual(transfer.to_address,
                         "0xbc4b58fad3c3c585d963d4a593cf9ff8fcdf6151")
        self.assertEqual(transfer.token_id, '1797390')
        self.assertEqual(transfer.transaction_hash,
                         '0x73aa352cae6024d82be60c0165020a5cdf62fb87565b3a7d04f6929b2be0f2e1')
        self.assertEqual(transfer.block_number, 15213914)
        self.assertEqual(transfer.log_index, 333)
        self.assertEqual(transfer.chain_id, 1)
        self.assertEqual(
            transfer.block_hash, '0x1fdd7db84b0e6f645963be2a75da504fc0129aab287f54c43d685f561f6ff11f')
        self.assertEqual(transfer.tx_index, 155)
