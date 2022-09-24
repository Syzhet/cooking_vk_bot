from vkwave.bots import SimpleLongPollBot

from .echo import echo_router
from .send_photo import send_photo_router


def register_routers(bot: SimpleLongPollBot):
    bot.dispatcher.add_router(send_photo_router)
    bot.dispatcher.add_router(echo_router)
