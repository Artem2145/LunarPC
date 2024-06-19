from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

start_main_kbb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="🖱 - Мышь"), KeyboardButton(text="⌨️ - Клавиатура")],
    [KeyboardButton(text="🖥 - Экран"), KeyboardButton(text="🔓 - Компьютер")]
], resize_keyboard=True)


