from abc import ABC, abstractmethod


class Provider(ABC):
    @abstractmethod
    async def get_price(self, token):
        pass

    @abstractmethod
    async def buy(self, token, amount):
        pass

    @abstractmethod
    async def sell(self, token, amount):
        pass

    @abstractmethod
    async def get_liquidity(self, token):
        pass
