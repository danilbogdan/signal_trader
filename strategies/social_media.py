# TODO: Implement the SocialMediaStrategy class
from .base import Strategy


class SocialMediaStrategy(Strategy):
    """This strategy will be used to detect tokens that are
    being shilled on social media platforms like Twitter, Reddit, etc.
    """
    def __init__(self, *args, **kwargs):
        pass

    async def fetch_data(self):
        pass

    async def analyze_data(self, message):
        pass

    async def trigger_action(self, message):
        pass
