from vkwave.bots import SimpleBotEvent
from vkwave.bots.core.dispatching.filters import base


class ButtonCatFilter(base.BaseFilter):
    async def check(self, event: SimpleBotEvent):
        '''Проверка payload для inline-кнопок при выборе категорий.'''
        payload_list = [
            {'button': 'Сдоба'},
            {'button': 'Хлеб'},
            {'button': 'Пирожные'}
        ]
        return base.FilterResult(event.object.object.payload in payload_list)
