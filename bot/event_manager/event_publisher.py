import asyncio

event_subscribers = {}

def publish_event(event_name, event_data):
    print(f"Событие опубликовано: {event_name}, данные: {event_data}")  # Логируем событие
    if event_name in event_subscribers:
        for subscriber in event_subscribers[event_name]:
            # Проверяем, является ли подписчик асинхронным
            if asyncio.iscoroutinefunction(subscriber):
                # Если да, используем await
                asyncio.create_task(subscriber(event_data))
            else:
                # Если нет, вызываем как обычную функцию
                subscriber(event_data)

def subscribe_event(event_name, handler):
    if event_name not in event_subscribers:
        event_subscribers[event_name] = []
    event_subscribers[event_name].append(handler)
    print(f"Подписчик зарегистрирован на событие: {event_name}")  # Логируем подписку
