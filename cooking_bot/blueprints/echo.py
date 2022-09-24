from vkwave.bots import (
    DefaultRouter,
    SimpleBotEvent,
    simple_bot_message_handler
)


echo_router = DefaultRouter()


@simple_bot_message_handler(echo_router,)
async def echo(event: SimpleBotEvent) -> str:
    print('----------------------------', event['current_config'])
    user_data = (
        await event.api_ctx.users.get(
            user_ids=event.object.object.message.peer_id
        )
    ).response[0]
    await event.answer(f'Привет {user_data.first_name}')
