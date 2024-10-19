# src/event_manager.py

class EventManager:
    def __init__(self):
        self._subscribers = {}

    def subscribe(self, event_name, handler):
        """Подписывает объект-обработчик на событие."""
        if event_name not in self._subscribers:
            self._subscribers[event_name] = []
        self._subscribers[event_name].append(handler)

    async def publish(self, event_name, *args, **kwargs):
        """Вызывает все объекты-обработчики, подписанные на событие."""
        if event_name in self._subscribers:
            for handler in self._subscribers[event_name]:
                await handler(*args, **kwargs)
