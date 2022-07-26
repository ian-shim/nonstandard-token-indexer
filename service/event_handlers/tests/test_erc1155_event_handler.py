import unittest
from unittest.mock import MagicMock
from web3 import Web3
from service.event_handlers.erc1155_event_handler import ERC1155EventHandler

from .fixtures import LOGS


class TestERC1155EventHandler(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.provider = Web3(Web3.HTTPProvider('https://randomurl.com'))
        self.handler = ERC1155EventHandler(self.provider)

    def test_event_topics(self):
        self.assertEqual(self.handler.event_topics(), [
            "0xc3d58168c5ae7397731d063d5bbf3d657854427343f4c083240f7aacaa2d0f62",
            "0x4a39dc06d4c0dbc64b70af90fd698a233a518aa5d07e595d983b8c0526c8f7fb"
        ])

    def test_parse_transfers_batch(self):
        self.provider.eth.get_logs = MagicMock(return_value=LOGS['parallel'])
        logs = self.handler.fetch_logs('0x', 123, 456)

        transfers = self.handler.parse_transfers(logs[0])
        self.assertEqual(len(transfers), 52)

        self.assertEqual([transfer.token_id for transfer in transfers],
                         ['10106', '10109', '10112', '10115', '10120', '10126', '10134', '10137', '10140', '10142', '10144', '10151', '10152', '10154', '10156', '10159', '10161', '10170', '10173', '10176', '10179', '10182', '10185', '10189', '10206', '10208', '10236', '10238', '10239', '10244', '10245', '10248', '10249', '10252', '10255', '10256', '10260', '10263', '10266', '10276', '10279', '10284', '10285', '10286', '10287', '10288', '10289', '10290', '10291', '10295', '10296', '10297'])
        self.assertSetEqual(set([transfer.address for transfer in transfers]), set(
            ["0x76BE3b62873462d2142405439777e971754E8E77"]))
        self.assertSetEqual(set([transfer.from_address for transfer in transfers]), set(
            ["0xECa9D81a4dC7119A40481CFF4e7E24DD0aaF56bD"]))
        self.assertSetEqual(set([transfer.to_address for transfer in transfers]), set(
            ["0x3953a612E28159Fc3ef056Fb7d3a78095d23Af81"]))
        self.assertSetEqual(set([transfer.transaction_hash for transfer in transfers]), set(
            ["0x24a9326fd841d0de129d0b0303e4d8d950f36357be3a5ac8239b52580b53de75"]))
        self.assertSetEqual(set([transfer.block_number for transfer in transfers]), set(
            [15214085]))
        self.assertSetEqual(set([transfer.log_index for transfer in transfers]), set(
            [283]))
        self.assertSetEqual(set([transfer.block_hash for transfer in transfers]), set(
            ["0x7c67b84cb59b2fdeacb0c1bc97d84d2fbd79a64cbaa9301411b8e77b834518fa"]))
        self.assertSetEqual(set([transfer.tx_index for transfer in transfers]), set(
            [113]))

    def test_parse_transfers_single(self):
        self.provider.eth.get_logs = MagicMock(return_value=LOGS['parallel'])
        logs = self.handler.fetch_logs('0x', 123, 456)

        transfer = self.handler.parse_transfers(logs[2])[0]

        self.assertEqual(transfer.address,
                         "0x76BE3b62873462d2142405439777e971754E8E77")
        self.assertEqual(transfer.from_address,
                         "0x9A237d2c4a8c2203719Ff179c9423Aed92751313")
        self.assertEqual(transfer.to_address,
                         "0x5622B632E804e4F9a9DD5FB0371A86fa09847f99")
        self.assertEqual(
            transfer.token_id, '10500')
        self.assertEqual(transfer.transaction_hash,
                         '0x1cbb06ae7f4225dac17b1589f50b1ec869a25b2b6360891699aad2faf20ad373')
        self.assertEqual(transfer.block_number, 15215096)
        self.assertEqual(transfer.log_index, 346)
        self.assertEqual(transfer.chain_id, 1)
        self.assertEqual(
            transfer.block_hash, '0x8e6116540a192d670c12f9112ac83cdbaf9090e2230fcbdcf9c0faecde2ce278')
        self.assertEqual(transfer.tx_index, 179)
