from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    async def execyte(self):
        await self.fetch_data()
        await self.analyze_data()
        await self.trigger_action()

    @abstractmethod
    async def fetch_data(self):
        pass

    @abstractmethod
    async def analyze_data(self):
        pass

    @abstractmethod
    async def trigger_action(self):
        pass
