"""
event_manager.py — модуль управления событиями.

Цель: Предоставить гибкий и расширяемый механизм для подписки и публикации событий.
Обработчики могут быть добавлены динамически, что позволяет адаптировать систему к изменениям.
"""

from typing import Callable, Dict, List, Any
import asyncio

class EventManager:
    """Класс для управления событиями в реактивной архитектуре."""

    def __init__(self):
        """Инициализирует словарь подписчиков."""
        self._subscribers: Dict[str, List[Callable]] = {}

    def subscribe(self, event_name: str, handler: Callable):
        """
        Подписывает обработчик на указанное событие.

        Параметры:
            event_name (str): Имя события.
            handler (Callable): Функция или метод, вызываемый при наступлении события.
        """
        if event_name not in self._subscribers:
            self._subscribers[event_name] = []
        self._subscribers[event_name].append(handler)

    async def publish(self, event_name: str, *args: Any, **kwargs: Any):
        """
        Публикует событие и вызывает все подписанные обработчики.

        Параметры:
            event_name (str): Имя события.
            *args, **kwargs: Аргументы, передаваемые в обработчики.
        """
        handlers = self._subscribers.get(event_name, [])
        if not handlers:
            print(f"[Warning] Нет подписчиков на событие: {event_name}")
            return

        # Параллельное выполнение всех обработчиков события
        await asyncio.gather(*(handler(*args, **kwargs) for handler in handlers))
