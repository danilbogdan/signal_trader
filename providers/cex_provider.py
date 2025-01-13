# TODO: implemet DEXProvider class that inherits from Provider
from .base_provider import Provider
from ccxt import async_support as ccxt


class CEXProvider(Provider):
    def __init__(self, exchange_id: str, api_key: str, api_secret: str, memo: str = None, *args, **kwargs):
        self.client = getattr(ccxt, exchange_id)({
            'apiKey': api_key,
            'secret': api_secret,
            'enableRateLimit': True,
        })

    async def init(self):
        await self.client.load_markets()

    # todo: retry on failure
    async def get_price(self, token):
        return await self.client.fetch_ticker(token)['last']

    async def buy(self, token, amount):
        return self.client.create_order(token, 'market', 'buy', amount)

    async def sell(self, token, amount):
        return self.client.create_order(token, 'market', 'sell', amount)

    async def get_liquidity(self, token):
        pass
