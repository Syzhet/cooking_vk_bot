from vkwave.bots import BaseMiddleware, BotEvent, MiddlewareResult


class EnvMiddleware(BaseMiddleware):
    def __init__(self, **kwargs):
        super().__init__()
        self.kwargs = kwargs

    async def pre_process_event(self, event: BotEvent):
        event['current_bot'] = self.kwargs
        return MiddlewareResult(True)
