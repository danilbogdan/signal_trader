# TODO: Implement the OnChain class
from .base import Strategy


class OnChainStrategy(Strategy):
    """
    Strategy to monitor on-chain activities and detect big transactions on
    specific wallets.
    """
    def __init__(self, *args, **kwargs):
        pass

    async def fetch_data(self):
        pass

    async def analyze_data(self, message):
        pass

    async def trigger_action(self, message):
        pass
