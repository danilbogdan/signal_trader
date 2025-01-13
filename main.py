import asyncio
import os

from managers.sell_manager import SellManager
from managers.trade_manager import TradeManager
from strategies.telegram import TelegramStrategy
from providers.cex_provider import CEXProvider
from utils.logger import Logger
from utils.notification import NotificationService


async def main():
    # Telegram API keys: https://core.telegram.org/api/obtaining_api_id
    api_id = os.getenv("TELEGRAM_API_ID")
    api_hash = os.getenv("TELEGRAM_API_HASH")

    # Channels to monitor and keywords to search for
    monitored_channels = ["example_channel"]
    keywords = ["listing", "new token", "presale"]

    # Провайдеры
    cex_provider = CEXProvider("mexc", api_key="your_api_key", api_secret="your_api")
    await CEXProvider.init()
    notification_service = NotificationService()
    logger = Logger()

    sell_manager = SellManager(cex_provider, notification_service)
    trade_manager = TradeManager(cex_provider, sell_manager, logger, notification_service)

    # Запуск стратегии
    telegram_strategy = TelegramStrategy(api_id, api_hash, monitored_channels, keywords, trade_manager)
    trade_manager.add_strategy(telegram_strategy)

    # Run the SellManager's periodic price checks
    sell_manager_task = asyncio.create_task(sell_manager.check_prices())

    # Start executing strategies
    await asyncio.gather(trade_manager.execute_strategies(), sell_manager_task)


if __name__ == "__main__":
    asyncio.run(main())
