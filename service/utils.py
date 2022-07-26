from typing import List
import eth_abi
from eth_typing import ChecksumAddress
from hexbytes import HexBytes
from web3 import Web3


def uint256_to_address(hexstr: str = None, hexbytes: HexBytes = None, bytes32: bytes = None) -> ChecksumAddress:
    if hexbytes is not None:
        hexstr = hexbytes.hex()
    if bytes32 is not None:
        hexstr = Web3.toHex(bytes32)

    assert hexstr.startswith("0x")
    raw = bytes.fromhex(hexstr[2:])
    assert len(raw) == 32
    return Web3.toChecksumAddress(raw[12:])


def decode_data(types: List[str], data: str):
    b = bytes.fromhex(data[2:])
    return eth_abi.decode(types, b)