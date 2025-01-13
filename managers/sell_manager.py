import asyncio

class SellManager:
    def __init__(self, provider, notification_service):
        self.tracked_tokens = {}  # Format: {token: {"buy_price": x, "target_price": y}}
        self.provider = provider
        self.notification_service = notification_service

    def track_token(self, token, buy_price, target_price):
        """
        Add a token to the tracking list with its buy price and target sell price.
        """
        self.tracked_tokens[token] = {"buy_price": buy_price, "target_price": target_price}
        print(f"Tracking {token}: buy at {buy_price}, target at {target_price}")

    async def check_prices(self):
        """
        Periodically check token prices and trigger sell actions if conditions are met.
        """
        while True:
            for token, data in list(self.tracked_tokens.items()):  # Use list to allow mutation
                current_price = await self.provider.get_price(token)
                if current_price >= data["target_price"]:
                    self.trigger_sell(token, current_price)
                    del self.tracked_tokens[token]
            await asyncio.sleep(10)  # Adjust frequency of price checks

    async def trigger_sell(self, token, current_price):
        """
        Execute the sell action for a token and notify the user.
        """
        print(f"Selling {token} at {current_price}")
        self.provider.sell(token, 1)  # Assuming selling all tracked tokens
        self.notification_service.send_message(f"Sold {token} at {current_price}")