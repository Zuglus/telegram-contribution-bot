
from event_handlers.history import handle_view_history
from event_handlers.payments import handle_create_payment
from event_handlers.start_menu import handle_start_command
from event_manager.event_publisher import subscribe_event
from aiogram import Bot
from settings.bot_settings import get_bot_token

bot = Bot(token=get_bot_token())


# Регистрации подписчиков на события
def register_event_handlers():
    subscribe_event("start_command_received", handle_start_command)
    subscribe_event("create_payment_clicked", handle_create_payment)
    subscribe_event("view_history_clicked", handle_view_history)
