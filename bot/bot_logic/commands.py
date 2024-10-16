from aiogram import types
from aiogram.dispatcher import Dispatcher
from event_manager.event_publisher import publish_event

def register_commands(dp: Dispatcher):
    @dp.message_handler(commands=["start"])
    async def send_welcome(message: types.Message):
        publish_event("start_command_received", {"user_id": message.from_user.id})
