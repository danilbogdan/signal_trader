# TODO: Implement the PresaleStrategy class
from .base import Strategy


class PumpAndDumpStrategy(Strategy):
    """There are some communities like reddit that are known for pump and dump
    schemes. This strategy will be used to detect and act on these schemes.
    """
    def __init__(self, *args, **kwargs):
        pass

    async def fetch_data(self):
        pass

    async def analyze_data(self, message):
        pass

    async def trigger_action(self, message):
        pass
