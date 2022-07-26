import unittest
from unittest.mock import MagicMock
from web3 import Web3

from service.event_handlers.erc721_event_handler import ERC721EventHandler
from .fixtures import LOGS


class TestERC721EventHandler(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.provider = Web3(Web3.HTTPProvider('https://randomurl.com'))
        self.handler = ERC721EventHandler(self.provider)

    def test_event_topics(self):
        self.assertEqual(self.handler.event_topics(), [
                         "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"])
        
    def test_parse_transfers(self):
        self.provider.eth.get_logs = MagicMock(return_value=LOGS['hashmasks'])
        logs = self.handler.fetch_logs('0x', 123, 456)

        transfer = self.handler.parse_transfers(logs[0])[0]

        self.assertEqual(transfer.address,
                         "0xC2C747E0F7004F9E8817Db2ca4997657a7746928")
        self.assertEqual(transfer.from_address,
                         "0xC7a8B45E184138114E6085C82936A8Db93DD156a")
        self.assertEqual(transfer.to_address,
                         "0x0000000050Fd1220ecf21D84687EBaD194Fd537F")
        self.assertEqual(transfer.token_id, '9427')
        self.assertEqual(transfer.transaction_hash,
                         '0xc339a1af8490b9ba7f25eb581a93872165c781d4b716aa6edce39ad6be3d2380')
        self.assertEqual(transfer.block_number, 15214403)
        self.assertEqual(transfer.log_index, 74)
        self.assertEqual(transfer.chain_id, 1)
        self.assertEqual(
            transfer.block_hash, '0x621d099225a5000ec9a7d08d58a1d54683ae09d006d1294e36e5e1ccd0af47a2')
        self.assertEqual(transfer.tx_index, 9)

    def test_parse_transfers_ens(self):
        self.provider.eth.get_logs = MagicMock(return_value=LOGS['ens'])
        logs = self.handler.fetch_logs('0x', 123, 456)

        transfer = self.handler.parse_transfers(logs[0])[0]

        self.assertEqual(transfer.address,
                         "0x57f1887a8BF19b14fC0dF6Fd9B2acc9Af147eA85")
        self.assertEqual(transfer.from_address,
                         "0x283Af0B28c62C092C9727F1Ee09c02CA627EB7F5")
        self.assertEqual(transfer.to_address,
                         "0x40202C1F0E6Fd1F9E2D178BB27cb610aCFfc2A77")
        self.assertEqual(
            transfer.token_id, '67093907974078187927899987782501909830821941753008555992120183736992409706341')
        self.assertEqual(transfer.transaction_hash,
                         '0x15d08796ba3204150272985ae0fea00c9acf3b6ed43b59f5ee732ab877fbca35')
        self.assertEqual(transfer.block_number, 15213900)
        self.assertEqual(transfer.log_index, 64)
        self.assertEqual(transfer.chain_id, 1)
        self.assertEqual(
            transfer.block_hash, '0xe01883323dc383aaa8200f17cfbdc95332d916d62a071e126aa7ebe3f060c67c')
        self.assertEqual(transfer.tx_index, 33)
