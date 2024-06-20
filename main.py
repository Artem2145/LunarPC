import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
import time
from keyboards import start_main_kbb, mouse_main_kbb
from mouse_def import LKM_mouse_def, PKM_mouse_def, left_mouse_def, right_mouse_def, down_mouse_def, upstairs_mouse_def, block_mouse_def



bot = Bot(token="6515705546:AAFd1Qv0aKPCsHZvPfj-IK0zNuxgm2LNAik")
dp = Dispatcher()




@dp.message(CommandStart())
async def start_main(message: Message):
    await message.answer("🌟 Привет! Спасибо, что выбрал именно нашего бота! 🌟\nНаш телеграмм - https://t.me/+LXG_pxKV0AtjMzE6")
    time.sleep(0.5)
    await message.answer("Выбери тебе нужный пункт.", reply_markup=start_main_kbb)


@dp.message(F.text == "🖱 - Мышь")
async def mouse_main(message: Message):
    await message.answer("Выберите что вам нужно:", reply_markup=mouse_main_kbb)

@dp.callback_query(F.data == "mouse_LKM")
async def mouse_LKM_main(callback: CallbackQuery):
    LKM_mouse_def()
    await callback.message.answer("Левая кнопка мыши нажата.")

@dp.callback_query(F.data == "mouse_PKM")
async def mouse_LKM_main(callback: CallbackQuery):
    PKM_mouse_def()
    await callback.message.answer("Правая кнопка мыши нажата.")

@dp.callback_query(F.data == "upstairs")
async def mouse_upstairs_main(callback: CallbackQuery):
    upstairs_mouse_def()
    await callback.message.answer("Курсор поднялся вверх.")

@dp.callback_query(F.data == "down")
async def mouse_down_main(callback: CallbackQuery):
    down_mouse_def()
    await callback.message.answer("Курсор опустился вниз.")

@dp.callback_query(F.data == "mouse_left")
async def left_mouse_main(callback: CallbackQuery):
    left_mouse_def()
    await callback.message.answer("Курсор ушел в лево.")

@dp.callback_query(F.data == "mouse_right")
async def reight_mouse_main(callback: CallbackQuery):
    right_mouse_def()
    await callback.message.answer("Курсор ушел в право.")



@dp.callback_query(F.data == "block")
async def block_mouse_main(callback: CallbackQuery):
    block_mouse_def()
    await callback.message.answer("Мышка заблокирована.")

@dp.callback_query(F.data == "unlocking")
async def unlocking_mouse_main(callback: CallbackQuery):
    upstairs_mouse_def()
    await callback.message.answer("Мышка разблокирована.")



async def main():
    await dp.start_polling(bot)



if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")