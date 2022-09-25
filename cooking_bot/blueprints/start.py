from vkwave.bots import (
    DefaultRouter,
    SimpleBotEvent,
    simple_bot_message_handler,
    simple_bot_handler,
)
from vkwave.types.bot_events import BotEventType
from vkwave.bots.utils.uploaders import PhotoUploader
from vkwave.bots import PayloadFilter, CommandsFilter, EventTypeFilter

from cooking_bot.keyboards.inline import create_carusel
from cooking_bot.db_api.models.categories import Category


start_router = DefaultRouter()


@simple_bot_handler(
    start_router,
    EventTypeFilter(BotEventType.MESSAGE_EVENT),
    PayloadFilter({"button": "start"})
)
async def cb_start(event: SimpleBotEvent):
    conversation_message_id = event.object.object.conversation_message_id
    template = await create_carusel(Category)
    await event.api_ctx.messages.edit(
        peer_id=event.object.object.user_id,
        message="Выберите одну из категорий",
        template=template,
        conversation_message_id=conversation_message_id
    )


@simple_bot_message_handler(
    start_router,
    CommandsFilter('start')
)
async def cmd_start(event: SimpleBotEvent):
    # current_bot = event['current_bot']['bot']
    # user_id = event.object.object.message.peer_id
    # photo = await PhotoUploader(
    #     current_bot.api_context
    #     ).get_attachment_from_link(
    #         peer_id=user_id,
    #         link="http://localhost:8888/cake"
    #     )
    # print('-------------------------', photo)
    await event.answer(
        message="Выберите одну из категорий",
        template=await create_carusel(Category)
    )
