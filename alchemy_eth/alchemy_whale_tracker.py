import asyncio
import json
import websockets
import pandas as pd
from eth_top_holders_scraper import eth_top_holders_scraper

df = eth_top_holders_scraper()

addresses = df['address'].values.tolist()

api_key = ""

alchemy_wss_mainnet = f"wss://eth-mainnet.g.alchemy.com/v2/{api_key}"

async def listen_to_pending_transactions():
    async with websockets.connect(alchemy_wss_mainnet) as ws:

        subscription_params = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "eth_subscribe",
            "params": [
                "alchemy_filteredNewFullPendingTransactions",
                {
                    "address": addresses
                }
            ]
        }

        await ws.send(json.dumps(subscription_params))
        print(f"Subscribed to filtered pending transactions")

        while True:
            response = await ws.recv()
            data = json.loads(response)
            #print(json.dumps(data, indent=2))

            if "method" in data and data["method"] == "eth_subscription":
                tx=data['params']['result']
                #print(json.dumps(data, indent=2))
                # ETH transfers
                if int(tx["value"], 16) / 1e18 > 500:
                    print(f"Transaction hash: {tx['hash']}")
                    from_address = tx['from']
                    to_address = tx['to']
                    from_tag = df[df['address'] == from_address]['name_tag']
                    to_tag = df[df['address'] == to_address]['name_tag']
                    from_tag_str = from_tag.iloc[0] if not from_tag.empty else "unknown"
                    to_tag_str = to_tag.iloc[0] if not to_tag.empty else "unknown"

                    print(f"Whale ETH transfer of {int(tx['value'], 16) / 1e18} ETH from ({from_tag_str}) to {tx['to']} ({to_tag_str})")

asyncio.run(listen_to_pending_transactions())

# Each call is 100 CU's worth.