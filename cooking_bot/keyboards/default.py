from typing import Optional

from vkwave.bots.utils.keyboards import Keyboard
from vkwave.bots.utils.keyboards.keyboard import ButtonColor


def create_one_button_keyboard(button_name: str, type: Optional[str] = None):
    if type == 'inline':
        kb = Keyboard(inline=True)
        button_name = button_name
    else:
        kb = Keyboard(one_time=True)
    kb.add_callback_button(
        button_name,
        color=ButtonColor.PRIMARY,
        payload={'button': button_name}
    )
    return kb.get_keyboard()


def create_kb_product_description(back_to_cat: str):
    kb = Keyboard(inline=True)
    kb.add_callback_button(
        'Назад',
        color=ButtonColor.PRIMARY,
        payload={'button': back_to_cat}
    )
    kb.add_row()
    kb.add_callback_button(
        'В меню',
        color=ButtonColor.PRIMARY,
        payload={'button': 'start'}
    )
    return kb.get_keyboard()
