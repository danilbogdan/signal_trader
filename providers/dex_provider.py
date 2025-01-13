# TODO: implemet DEXProvider class that inherits from Provider
from .base_provider import Provider


class DEXProvider(Provider):
    async def get_price(self, token):
        pass

    async def buy(self, token, amount):
        pass

    async def sell(self, token, amount):
        pass

    async def get_liquidity(self, token):
        pass
