"""
functional_handlers.py — модуль с функциональными обработчиками для событий Telegram-бота.

Цель: Предоставить чистые функции, которые обрабатывают команды и публикуют сообщения.
Функциональный подход обеспечивает простоту и предсказуемость логики.
"""

from telegram import Update
from telegram.ext import ContextTypes
from typing import Callable

def create_message_handler(message: str) -> Callable:
    """
    Создает обработчик, который отправляет заданное сообщение пользователю.

    Параметры:
        message (str): Сообщение, которое будет отправлено пользователю.

    Возвращает:
        Callable: Асинхронная функция-обработчик, которая отправляет сообщение.
    """
    async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
        """
        Отправляет заданное сообщение в ответ на команду пользователя.

        Параметры:
            update (Update): Объект обновления от Telegram.
            context (ContextTypes.DEFAULT_TYPE): Контекст команды Telegram.
        """
        # Проверка, что сообщение существует и reply_text доступен
        if update.message:
            await update.message.reply_text(message)
        else:
            print("[Warning] Нет сообщения в update. Обработчик не смог отправить ответ.")

    return handler
