from typing import TYPE_CHECKING
from .base import Strategy
from telethon import TelegramClient, events

if TYPE_CHECKING:
    from managers.trade_manager import TradeManager


class TelegramStrategy(Strategy):
    def __init__(self, api_id, api_hash, monitored_channels, keywords, trade_manager: TradeManager):
        self.client = TelegramClient('telegram_bot', api_id, api_hash)
        self.monitored_channels = monitored_channels
        self.keywords = keywords
        self.trade_manager = trade_manager
    
    async def execute(self):
        await self.fetch_data()
    
    async def fetch_data(self):
        @self.client.on(events.NewMessage(chats=self.monitored_channels))
        async def handler(event):
            message = event.message.message
            await self.analyze_data(message)

        await self.client.start()
        await self.client.run_until_disconnected()

    async def analyze_data(self, message):
        if any(keyword in message for keyword in self.keywords):
            print(f"Triggered by message: {message}")
            await self.trigger_action(message)

    async def trigger_action(self, message):
        # Extract data from message and provide into execute_trade
        token = "ABC"
        await self.trade_manager.place_trade(token, action='buy', amount=100)
