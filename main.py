import os
import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

async def main():
    token = os.getenv("9035731676:AAEQFvY9qSfFkD04jVGzkDq9SllVcD7iB_Q")
    if not token:
        raise RuntimeError("9035731676:AAEQFvY9qSfFkD04jVGzkDq9SllVcD7iB_Q")

    bot = Bot(token=token)
    dp = Dispatcher()

    @dp.message(CommandStart())
    async def start(message: Message):
        await message.answer(
            "🎁 Добро пожаловать в GiftEz!\n\n"
            "Отправь ссылку на Telegram-подарок."
        )

    @dp.message()
    async def other(message: Message):
        await message.answer(
            "🔎 Получил сообщение. Анализ подарков скоро появится."
        )

    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
