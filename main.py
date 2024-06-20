import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message
import time
from keyboards import start_main_kbb, mouse_main_kbb



bot = Bot(token="7285822177:AAEro27NLuk8C5thTgJFQ0ofSkPAVugp3qc")
dp = Dispatcher()




@dp.message(CommandStart())
async def start_main(message: Message):
    await message.answer("🌟 Привет! Спасибо, что выбрал именно нашего бота! 🌟\nНаш телеграмм - https://t.me/+LXG_pxKV0AtjMzE6")
    time.sleep(0.5)
    await message.answer("Выбери тебе нужный пункт.", reply_markup=start_main_kbb)


@dp.message(F.text == "🖱 - Мышь")
async def mouse_main(message: Message):
    await message.answer("Выберите что вам нужно:", reply_markup=mouse_main_kbb)



async def main():
    await dp.start_polling(bot)



if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")