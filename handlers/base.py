# handlers/base.py
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router(name='base')

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Добро пожаловать в бот учёта взносов!")

@router.message(Command("help"))
async def cmd_help(message: Message):
    base_commands = """
    Доступные команды:
    /start - Начать работу с ботом
    /help - Показать это сообщение
    /register - Подать заявку на регистрацию
    """
    
    # Если это админ, добавляем команды администратора
    if message.from_user.id == message.bot.config.admin_id:
        admin_commands = """
        
    Команды администратора:
    /toggle_registration - Открыть/закрыть регистрацию
        """
        base_commands += admin_commands
    
    await message.answer(base_commands)