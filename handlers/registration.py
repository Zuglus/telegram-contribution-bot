# handlers/registration.py
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from models import User
from models.settings import BotSettings
from database.base import Database

router = Router(name='registration')

# Клавиатура для админа
def get_admin_keyboard(user_id: int):
    builder = InlineKeyboardBuilder()
    builder.button(text="✅ Одобрить", callback_data=f"approve_{user_id}")
    builder.button(text="❌ Отклонить", callback_data=f"reject_{user_id}")
    return builder.as_markup()

@router.message(Command("register"))
async def cmd_register(message: Message, session: AsyncSession):
    # Проверяем, открыта ли регистрация
    settings = await session.execute(
        select(BotSettings).where(BotSettings.name == "registration_enabled")
    )
    setting = settings.scalar_one_or_none()
    
    if not setting or not setting.value:
        await message.answer("В данный момент регистрация закрыта. Пожалуйста, попробуйте позже.")
        return

    # Проверяем, не зарегистрирован ли уже пользователь
    existing_user = await session.execute(
        select(User).where(User.telegram_id == message.from_user.id)
    )
    user = existing_user.scalar_one_or_none()
    
    if user:
        if user.is_approved:
            await message.answer("Вы уже зарегистрированы в системе!")
        else:
            await message.answer("Ваша заявка на рассмотрении у администратора.")
        return

    # Создаём новую заявку на регистрацию
    new_user = User(
        telegram_id=message.from_user.id,
        full_name=message.from_user.full_name,
        is_approved=False
    )
    session.add(new_user)
    await session.commit()

    # Отправляем сообщение пользователю
    await message.answer(
        "Заявка на регистрацию отправлена администратору. "
        "Пожалуйста, ожидайте подтверждения."
    )

    # Отправляем уведомление админу
    admin_message = (
        f"Новая заявка на регистрацию:\n"
        f"ID: {message.from_user.id}\n"
        f"Имя: {message.from_user.full_name}\n"
        f"Username: @{message.from_user.username}"
    )
    
    await message.bot.send_message(
        chat_id=message.bot.config.admin_id,
        text=admin_message,
        reply_markup=get_admin_keyboard(message.from_user.id)
    )

@router.callback_query(F.data.startswith("approve_"))
async def approve_user(callback: CallbackQuery, session: AsyncSession):
    # Проверяем, что это админ
    if callback.from_user.id != callback.bot.config.admin_id:
        await callback.answer("У вас нет прав на это действие!")
        return

    user_id = int(callback.data.split("_")[1])
    user = await session.execute(
        select(User).where(User.telegram_id == user_id)
    )
    user = user.scalar_one_or_none()
    
    if user:
        user.is_approved = True
        await session.commit()
        
        # Уведомляем пользователя
        await callback.bot.send_message(
            chat_id=user_id,
            text="Ваша заявка на регистрацию одобрена! Теперь вы можете пользоваться ботом."
        )
        
        # Уведомляем админа
        await callback.message.edit_text(
            f"Пользователь {user.full_name} одобрен.",
            reply_markup=None
        )
    
    await callback.answer()

@router.callback_query(F.data.startswith("reject_"))
async def reject_user(callback: CallbackQuery, session: AsyncSession):
    # Проверяем, что это админ
    if callback.from_user.id != callback.bot.config.admin_id:
        await callback.answer("У вас нет прав на это действие!")
        return

    user_id = int(callback.data.split("_")[1])
    user = await session.execute(
        select(User).where(User.telegram_id == user_id)
    )
    user = user.scalar_one_or_none()
    
    if user:
        await session.delete(user)
        await session.commit()
        
        # Уведомляем пользователя
        await callback.bot.send_message(
            chat_id=user_id,
            text="К сожалению, ваша заявка на регистрацию отклонена."
        )
        
        # Уведомляем админа
        await callback.message.edit_text(
            f"Заявка пользователя {user.full_name} отклонена.",
            reply_markup=None
        )
    
    await callback.answer()