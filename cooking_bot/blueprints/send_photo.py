from vkwave.bots import (
    DefaultRouter,
    SimpleBotEvent,
    simple_bot_message_handler
)
from vkwave.bots.utils.uploaders import PhotoUploader


send_photo_router = DefaultRouter()


@simple_bot_message_handler(send_photo_router,)
async def send_photo(event: SimpleBotEvent):
    current_bot = event['current_bot']['bot']
    user_id = event.object.object.message.peer_id
    photo = await PhotoUploader(current_bot.api_context).get_attachment_from_link(peer_id=user_id, link="https://user-images.githubusercontent.com/28061158/75329873-7f738200-5891-11ea-9565-fd117ea4fc9e.jpg")
    await event.answer(message='Пишем при помощи этого', attachment=photo)
