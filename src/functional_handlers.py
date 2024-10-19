# src/functional_handlers.py

from telegram import Update
from telegram.ext import ContextTypes

def create_message_handler(text):
    """Чистая функция, возвращающая обработчик для отправки сообщения."""
    async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(text)
    return handler
