from typing import Union

from vkwave.bots import (
    DefaultRouter,
    SimpleBotEvent,
    simple_bot_message_handler,
    simple_bot_handler,
)
from vkwave.types.bot_events import BotEventType
from vkwave.bots import PayloadFilter, CommandsFilter, EventTypeFilter
from vkwave.bots.fsm import (
    FiniteStateMachine,
    ForWhat,
    StateFilter,
    ANY_STATE,
    NO_STATE
)
from vkwave.bots.utils.uploaders import PhotoUploader

from cooking_bot.keyboards.inline import create_carusel
from cooking_bot.keyboards.default import create_kb_product_description
from cooking_bot.db_api.models.categories import Category
from cooking_bot.db_api.models.products import Product
from cooking_bot.utils.state import CatState
from cooking_bot.filters.button_filter import ButtonCatFilter


start_router = DefaultRouter()

fsm = FiniteStateMachine()


async def create_answer(
    event: SimpleBotEvent,
    text: str,
    obj: Union[Category, Product],
    filter: int = None,
    add_back: bool = None
):
    conversation_message_id = event.object.object.conversation_message_id
    template = await create_carusel(obj, filter, add_back)
    await event.api_ctx.messages.edit(
        peer_id=event.object.object.user_id,
        message=text,
        template=template,
        conversation_message_id=conversation_message_id
    )


@simple_bot_handler(
    start_router,
    EventTypeFilter(BotEventType.MESSAGE_EVENT),
    PayloadFilter({"button": "start"}) &
    StateFilter(fsm=fsm, state=ANY_STATE, for_what=ForWhat.FOR_USER),
)
async def cb_start(event: SimpleBotEvent):
    try:
        await fsm.finish(event=event, for_what=ForWhat.FOR_USER)
    except KeyError:
        pass
    await fsm.set_state(
        event=event,
        state=CatState.category,
        for_what=ForWhat.FOR_USER
    )
    text = "Выберите одну из категорий"
    await create_answer(event, text, Category)


@simple_bot_message_handler(
    start_router,
    CommandsFilter('start') &
    StateFilter(fsm=fsm, state=ANY_STATE, for_what=ForWhat.FOR_USER),
)
async def cmd_start(event: SimpleBotEvent):
    try:
        await fsm.finish(event=event, for_what=ForWhat.FOR_USER)
    except KeyError:
        pass
    await fsm.set_state(
        event=event,
        state=CatState.category,
        for_what=ForWhat.FOR_USER
    )
    await event.answer(
        message="Выберите одну из категорий",
        template=await create_carusel(Category)
    )


@simple_bot_handler(
    start_router,
    EventTypeFilter(BotEventType.MESSAGE_EVENT),
    StateFilter(fsm=fsm, state=CatState.category, for_what=ForWhat.FOR_USER)
    | StateFilter(fsm=fsm, state=NO_STATE, for_what=ForWhat.FOR_USER),
    ButtonCatFilter()
)
async def cb_cat(event: SimpleBotEvent):
    category_name = event.object.object.payload['button']
    cat_id = Category.query.where(Category.name == category_name).gino.scalar()
    await fsm.set_state(
        event=event,
        state=CatState.product,
        for_what=ForWhat.FOR_USER,
        extra_state_data={"category": category_name, 'cat_id': cat_id},
    )
    text = f"Категория {category_name}"
    await create_answer(
        event,
        text,
        Product,
        filter=cat_id,
        add_back=True
    )


@simple_bot_handler(
    start_router,
    EventTypeFilter(BotEventType.MESSAGE_EVENT),
    PayloadFilter({"button": "Назад"}) &
    StateFilter(fsm=fsm, state=CatState.product, for_what=ForWhat.FOR_USER),
)
async def cb_back(event: SimpleBotEvent):
    await cb_start(event)


@simple_bot_handler(
    start_router,
    EventTypeFilter(BotEventType.MESSAGE_EVENT),
    StateFilter(fsm=fsm, state=CatState.product, for_what=ForWhat.FOR_USER),
)
async def cb_product(event: SimpleBotEvent):
    product_name = event.object.object.payload['button']
    product = await Product.query.where(
        Product.name == product_name
    ).gino.first()
    await fsm.add_data(
        event=event,
        for_what=ForWhat.FOR_USER,
        state_data={
            'product_name': product.name,
            'product_description': product.description,
            'product_photo_url': product.photo_url
        },
    )
    product_data = await fsm.get_data(event, for_what=ForWhat.FOR_USER)
    await fsm.finish(event=event, for_what=ForWhat.FOR_USER)
    caption = ('Категория: {category}\n'
               'Название продукта: {product_name}\n'
               'Описание продукта: {product_description}')
    conversation_message_id = event.object.object.conversation_message_id
    peer_id = event.object.object.user_id,

    current_bot = event['current_bot']['bot']
    photo = await PhotoUploader(
        current_bot.api_context
        ).get_attachment_from_link(
            peer_id=peer_id,
            link=f'{product_data["product_photo_url"]}'
        )
    await event.api_ctx.messages.edit(
            peer_id=peer_id,
            message=caption.format(**product_data),
            keyboard=create_kb_product_description(product_data['category']),
            conversation_message_id=conversation_message_id,
            attachment=photo
    )
