import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import load_config
from handlers.base import router

async def main():
    logging.basicConfig(level=logging.INFO)
    
    # Загружаем конфигурацию
    config = load_config()
    
    # Инициализируем бот и диспетчер
    bot = Bot(token=config.bot.token)
    dp = Dispatcher()
    
    # Регистрируем роутеры
    dp.include_router(router)
    
    # Запускаем бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())