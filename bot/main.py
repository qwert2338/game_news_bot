import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import os
from dotenv import load_dotenv

# --------------- Чтение переменных из .env ----------------
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
admin_id_raw = os.getenv("ADMIN_ID")

if BOT_TOKEN is None:
    raise ValueError("Ошибка: переменная BOT_TOKEN не найдена в .env")
if admin_id_raw is None:
    raise ValueError("Ошибка: переменная ADMIN_ID не найдена в .env")

ADMIN_ID = int(admin_id_raw)

# --------------- Создаём бота ----------------
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)

# --------------- Команды ----------------
@dp.message(Command("start"))
async def start(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        await message.answer("✅ Бот запущен!\nЯ буду присылать тебе игровые новости.")
    else:
        await message.answer("❌ У тебя нет доступа к этому боту.")

# --------------- Запуск бота ----------------
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import bot.news_runner as news_runner
    import asyncio
    asyncio.run(news_runner.scheduler())

