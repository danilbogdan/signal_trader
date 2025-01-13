# Crypto Trading Bot

This project is a modular and extensible crypto trading bot that utilizes different strategies to monitor market trends, execute trades, and manage selling tokens based on predefined profit targets.

## Features

1. **Modular Strategies:**
    - Social Media sentiment analysis.
    - Presale tracking.
    - On-chain activity monitoring.
    - Pump-and-dump detection.
2. **Provider Support:**
    - Works with Centralized Exchanges (CEX).
    - Works with Decentralized Exchanges (DEX).
3. **Trade Management:**
    - Unified interface for trade execution (buy/sell).
    - Risk management integration.
4. **Sell Manager:**
    - Tracks purchased tokens.
    - Monitors token prices periodically.
    - Executes sales when target price conditions are met.
5. **Extensibility:**
    - Easily add new strategies or providers by implementing the respective abstract base classes.

## Project Structure

```
crypto-trading-bot/
├── main.py                         # Main entry point of the application
├── strategies/
│   ├── __init__.py                 # Strategy module initializer
│   ├── base_strategy.py            # Abstract base class for all strategies
│   ├── social_media.py             # Example: Social Media strategy implementation
│   ├── presale.py                  # Example: Presale strategy implementation
├── providers/
│   ├── __init__.py                 # Provider module initializer
│   ├── base_provider.py            # Abstract base class for providers
│   ├── dex_provider.py             # Example: DEX provider implementation
│   ├── cex_provider.py             # Example: CEX provider implementation
├── managers/
│   ├── __init__.py                 # Managers module initializer
│   ├── trade_manager.py            # Manages strategies and trade execution
│   ├── sell_manager.py             # Monitors prices and executes sell actions
│   ├── risk_manager.py             # Handles risk validation and budget control
├── services/
│   ├── __init__.py                 # Services module initializer
│   ├── logger.py                   # Logs events and transactions
│   ├── notification.py             # Handles user notifications
└── README.md                       # Project documentation
```

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/crypto-trading-bot.git
    cd crypto-trading-bot
    ```

2. Install dependencies:

    Ensure you have Python 3.9+ installed, then install the required libraries:

    ```sh
    pip install -r requirements.txt
    ```

3. Configure API Keys:

    - Add your API keys for the respective exchanges (CEX/DEX) in a `.env` file.
    - Example `.env` file:

    ```env
    CEX_API_KEY=your_cex_api_key
    CEX_API_SECRET=your_cex_api_secret
    DEX_RPC_URL=your_dex_rpc_url
    ```

4. Run the application:

    ```sh
    python main.py
    ```

## Usage

1. **Adding a New Strategy:**
    - Create a new strategy class in the `strategies/` directory.
    - Extend `Strategy` from `base_strategy.py` and implement `fetch_data`, `analyze_data`, and `trigger_action`.

2. **Adding a New Provider:**
    - Create a new provider class in the `providers/` directory.
    - Extend `Provider` from `base_provider.py` and implement methods like `get_price`, `buy`, `sell`, and `get_liquidity`.

3. **Tracking and Selling Tokens:**
    - Tokens bought through strategies are automatically tracked by the `SellManager`.
    - Modify the `SellManager` logic for custom profit targets or selling conditions.

## Example Workflow

1. A `SocialMediaStrategy` fetches data from a Telegram channel.
2. It detects a positive signal for token ABC and triggers a buy action.
3. The `TradeManager` executes the buy through the `DEXProvider`.
4. The `SellManager` tracks the token and monitors its price.
5. When the price reaches the target, the `SellManager` executes a sell.

## Extending the Bot

### Add a Strategy

Example: Create `custom_strategy.py`:

```python
from .base_strategy import Strategy

class CustomStrategy(Strategy):
    async def fetch_data(self):
        pass  # Fetch data logic

    async def analyze_data(self, data):
        pass  # Analysis logic

    async def trigger_action(self, data):
        pass  # Action logic
```

Add it to the `TradeManager`:

```python
from strategies.custom_strategy import CustomStrategy

custom_strategy = CustomStrategy(trade_manager)
trade_manager.add_strategy(custom_strategy)
```

## Contributing

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m "Add a new feature"`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.

## License

This project is licensed under the MIT License. See `LICENSE` for details.