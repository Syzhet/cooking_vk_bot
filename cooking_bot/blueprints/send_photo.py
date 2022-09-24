from vkwave.bots import (
    DefaultRouter,
    SimpleBotEvent,
    simple_bot_message_handler
)
from vkwave.bots.utils.uploaders import PhotoUploader
from vkwave.bots import PayloadFilter, CommandsFilter

from cooking_bot.keyboards.inline import create_carusel
from cooking_bot.db_api.models.categories import Category


send_photo_router = DefaultRouter()


@simple_bot_message_handler(
    send_photo_router,
    PayloadFilter({"button": "start"})
    | CommandsFilter('start')
)
async def send_photo(event: SimpleBotEvent):
    current_bot = event['current_bot']['bot']
    user_id = event.object.object.message.peer_id
    photo = await PhotoUploader(
        current_bot.api_context
        ).get_attachment_from_link(
            peer_id=user_id,
            link="http://localhost:8888/cake"
        )
    print('-------------------------', photo)
    # await event.answer(
    #     message='Пишем при помощи этого',
    #     attachment=photo,
    #     keyboard=kb.get_keyboard()
    # )
    await event.answer(
        message='Выберите одну из категорий',
        template=await create_carusel(Category),
    )
