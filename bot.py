import asyncio
import logging
from typing import AsyncGenerator, Any, Awaitable, Callable, Dict

from aiogram import Bot, Dispatcher, BaseMiddleware
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.storage.memory import MemoryStorage
from sqlalchemy.ext.asyncio import AsyncSession

from config import load_config
from handlers.base import router as base_router
from handlers.registration import router as registration_router
from handlers.admin import router as admin_router
from database.base import Database

class DatabaseMiddleware(BaseMiddleware):
    def __init__(self, database: Database):
        self.database = database
        super().__init__()

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message | CallbackQuery,
        data: Dict[str, Any]
    ) -> Any:
        async with self.database.session_maker() as session:
            data['session'] = session
            return await handler(event, data)

async def main():
    logging.basicConfig(level=logging.INFO)
    
    # Загружаем конфигурацию
    config = load_config()
    
    # Инициализируем базу данных
    database = Database(config.database.database)  # Изменили путь к конфигурации
    await database.create_db_and_tables()
    
    # Инициализируем хранилище состояний
    storage = MemoryStorage()
    
    # Инициализируем бот и диспетчер
    bot = Bot(token=config.bot.token)
    bot.config = config.bot  # Добавляем конфиг в бот для доступа к admin_id
    dp = Dispatcher(storage=storage)
    
    # Регистрируем роутеры
    dp.include_router(base_router)
    dp.include_router(registration_router)
    dp.include_router(admin_router)
    
    # Настраиваем middleware
    dp.message.middleware(DatabaseMiddleware(database))
    dp.callback_query.middleware(DatabaseMiddleware(database))
    
    # Запускаем бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())