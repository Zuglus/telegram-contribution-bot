import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = 'ВАШ_API_ТОКЕН_ЗДЕСЬ'

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я эхо-бот. Напиши мне что-нибудь, и я повторю это!")

# Обработчик всех текстовых сообщений
@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
