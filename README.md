# Whale Activity on Ethereum

This project tracks large ETH transactions (whale activity) in real-time using the Alchemy WebSocket API. It focuses on transactions from top Ethereum holders list on etherscan.io.

## Features

- Scrapes top ETH holders and their associated name tags from Etherscan  
- Subscribes to pending Ethereum transactions using Alchemy's WebSocket  
- Filters and prints out high-value ETH transfers from top addresses  
- Identifies known wallet tags

## Files Description

- **`alchemy_whale_tracker.py`**  
  - Connects to Alchemy’s WebSocket for filtered pending ETH transactions  
  - Filters transactions by known top holder addresses  
  - Prints out transfers over 500 ETH with name tags if available  

- **`eth_top_holders_scraper.py`**  
  - Scrapes the [Etherscan Top Accounts](https://etherscan.io/accounts) page  
  - Extracts wallet addresses and associated name tags  
  - Returns the data as a pandas DataFrame
    
## Example Output

Subscribed to filtered pending transactions Whale ETH transfer of 120.0 ETH from (Binance 8) to 0xabc...123 (unknown) Whale ETH transfer of 85.3 ETH from (unknown) to 0xdef...456 (Kraken 2)

---

## TODO / Improvements

- **Improve wallet filtering**:  
  Etherscan's top accounts list doesn't include all whale wallets, especially exchange wallets. Consider integrating enriched wallet datasets from sources like [Nansen](https://www.nansen.ai/), [Dune](https://dune.com/), or [Arkham Intelligence](https://arkhamintelligence.com/).

- **Analyze smart contract interactions**:  
  Look beyond simple ETH transfers—pending transactions that call smart contracts (e.g., swaps on Uniswap, deposits to staking contracts, etc.) may signal whale activity too (this information can be seen in "input" of transaction).

- **Create a Telegram bot**:  
  Set up a bot to send real-time whale alerts directly to a Telegram channel or group.

- **Explore alternatives to Alchemy**:  
  Alchemy’s filtered pending transaction subscription is very compute-intensive. Consider other data providers or approaches (e.g., mempool services, local Ethereum node) to make whale alerts more cost-effective.


