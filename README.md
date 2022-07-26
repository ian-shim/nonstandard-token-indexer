# Non-Standard Contract Populator
Implements a service that serves transfer events for non-standard NFT contracts. Specifically, these 5 contracts:
|  |  |  |
| --- | --- | --- |
| ethereum-mainnet | 0xb47e3cd837ddf8e4c57f05d70ab865de6e193bbb |	Cryptopunks |
| ethereum-mainnet | 0x06012c8cf97bead5deae237070f9587f8e7a266d |	CryptoKitties |
| ethereum-mainnet | 0xc2c747e0f7004f9e8817db2ca4997657a7746928 |	Hashmasks |
| ethereum-mainnet | 0x76be3b62873462d2142405439777e971754e8e77 |	Parallels |
| ethereum-mainnet | 0x57f1887a8BF19b14fC0dF6Fd9B2acc9Af147eA85 |	ENS |

# Usage
1. Clone the repo

2. Add Ethereum node URL in `.env` file
3. Create a virtualenv and install the requirements
```bash
$ virtualenv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```

4. Run the server
```bash
$ python3 run_server.py
```
5. Set parameters in `client.py` and send request to the server
```bash
$ python3 client.py
```

# Testing
```bash
$ python3 -m unittest discover
```