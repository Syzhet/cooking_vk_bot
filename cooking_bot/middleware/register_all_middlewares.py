from vkwave.bots import SimpleLongPollBot

from .environment import EnvMiddleware


def register_middleware(bot: SimpleLongPollBot):
    bot.add_middleware(EnvMiddleware(bot=bot))
