from vkwave.bots import (DefaultRouter, SimpleBotEvent,
                         simple_bot_message_handler)

from cooking_bot.keyboards.default import create_one_button_keyboard

echo_router = DefaultRouter()


@simple_bot_message_handler(echo_router,)
async def echo(event: SimpleBotEvent):
    '''Обработка незарегистрированных команд.'''
    user_data = (
        await event.api_ctx.users.get(
            user_ids=event.object.object.message.peer_id
        )
    ).response[0]
    await event.answer(
        message=(f'Привет {user_data.first_name}!\n'
                 'Для начала работы с ботом '
                 'нажми на кнопку старт или '
                 'набери команду: /start или !start'),
        keyboard=create_one_button_keyboard('start', 'inline')
    )
