from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from models.settings import BotSettings

router = Router(name='admin')

@router.message(Command("toggle_registration"))
async def cmd_toggle_registration(message: Message, session: AsyncSession):
    # Проверяем, что это админ
    if message.from_user.id != message.bot.config.admin_id:
        return

    # Получаем текущее состояние регистрации
    settings = await session.execute(
        select(BotSettings).where(BotSettings.name == "registration_enabled")
    )
    setting = settings.scalar_one_or_none()
    
    if not setting:
        # Если настройки нет, создаём её
        setting = BotSettings(name="registration_enabled", value=False)
        session.add(setting)
    
    # Меняем значение на противоположное
    setting.value = not setting.value
    await session.commit()
    
    status = "открыта" if setting.value else "закрыта"
    await message.answer(f"Регистрация {status}")