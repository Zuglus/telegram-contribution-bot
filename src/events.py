# src/events.py

from telegram import Update
from telegram.ext import ContextTypes

class StartEvent:
    async def handle(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text('Привет! Я объектно-ориентированный бот.')

class HelpEvent:
    async def handle(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text('Вот как ты можешь меня использовать:\n/start - Приветствие\n/help - Справка')
