import asyncio


class TradeManager:
    def __init__(self, provider, sell_manager, logger, notification_service):
        self.strategies = []
        self.provider = provider
        self.sell_manager = sell_manager
        self.logger = logger
        self.notification_service = notification_service

    def add_strategy(self, strategy):
        self.strategies.append(strategy)

    async def execute_strategies(self):
        """
        Entry point for executing all strategies.
        Each strategy runs its `fetch_data` method asynchronously.
        """
        tasks = [asyncio.create_task(strategy.execute()) for strategy in self.strategies]
        await asyncio.gather(*tasks)

    async def place_trade(self, token, action, amount):
        """
        Execute a trade (buy or sell) and log the event.
        Tracks the token in SellManager if it's a buy action.
        """
        if action == "buy":
            success = await self.provider.buy(token, amount)
            if success:
                self.logger.log_event(f"Bought {amount} of {token}")
                # Example: Track token for selling at a 20% profit
                buy_price = self.provider.get_price(token)
                target_price = buy_price * 1.2
                self.sell_manager.track_token(token, buy_price, target_price)
        elif action == "sell":
            success = self.provider.sell(token, amount)
            if success:
                self.logger.log_event(f"Sold {amount} of {token}")
