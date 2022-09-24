from vkwave.bots.utils.keyboards import Keyboard
from vkwave.bots.utils.keyboards.keyboard import ButtonColor


def create_one_button_keyboard(button_name: str, type: str = 'inline'):
    if type == 'inline':
        kb = Keyboard(inline=True)
        button_name = button_name
    else:
        kb = Keyboard(one_time=True)
    kb.add_text_button(
        button_name,
        color=ButtonColor.PRIMARY,
        payload={'button': button_name}
    )
    return kb.get_keyboard()
