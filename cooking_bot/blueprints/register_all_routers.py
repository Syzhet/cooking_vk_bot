from vkwave.bots import SimpleLongPollBot

from .echo import echo_router
from .start import start_router


def register_routers(bot: SimpleLongPollBot):
    '''Регистрация всех роутеров приложения.'''
    bot.dispatcher.add_router(start_router)
    bot.dispatcher.add_router(echo_router)
