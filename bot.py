import os
from dotenv import load_dotenv
from vkwave.bots import SimpleLongPollBot, SimpleBotEvent
from vkwave.bots.utils.uploaders import PhotoUploader

load_dotenv()

bot = SimpleLongPollBot(tokens=os.getenv('TOKEN'), group_id=216069290)

@bot.message_handler(bot.command_filter('mem')) # отправляем изображение по команде
async def send_photo(event: SimpleBotEvent):
    user_id = event.object.object.message.peer_id
    photo = await PhotoUploader(bot.api_context).get_attachment_from_link(peer_id=user_id, link="https://user-images.githubusercontent.com/28061158/75329873-7f738200-5891-11ea-9565-fd117ea4fc9e.jpg")    
    await event.answer(message='Пишем при помощи этого', attachment=photo)


@bot.message_handler(bot.text_filter(['Првиет', 'привет', 'хай']))
async def hello(event: SimpleBotEvent) -> str:
    user_data = (await event.api_ctx.users.get(user_ids=event.object.object.message.peer_id)).response[0] # получение даных о пользователе отправившем сообщение
    await event.answer(f'Привет {user_data.first_name}') # получение имени пользователя

bot.run_forever()