import os
import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

TOKEN = os.getenv("9035731676:AAEQFvY9qSfFkD04jVGzkDq9SllVcD7iB_Q")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "🎁 Добро пожаловать в GiftEz!\n\n"
        "🔎 Отправь ссылку на Telegram-подарок.\n"
        "📊 Скоро здесь появится анализ коллекций и цен."
    )

@dp.message(Command("help"))
async def help_command(message: Message):
    await message.answer("GiftEz — анализатор коллекционных подарков Telegram.")

@dp.message()
async def analyze(message: Message):
    if message.text and "t.me/nft/" in message.text:
        await message.answer(
            "🔎 Ссылка получена!\n"
            "Анализ рыночных данных пока настраивается."
        )
    else:
        await message.answer("Отправь ссылку на подарок Telegram.")

async def main():
    if not TOKEN:
        raise RuntimeError("Не задан BOT_TOKEN")
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
