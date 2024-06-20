from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

start_main_kbb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="🖱 - Мышь"), KeyboardButton(text="⌨️ - Клавиатура")],
    [KeyboardButton(text="🖥 - Экран"), KeyboardButton(text="🔓 - Компьютер")]
], resize_keyboard=True)



mouse_main_kbb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="ЛКМ", callback_data="mouse_LKM"), InlineKeyboardButton(text="🔼", callback_data="upstairs"), InlineKeyboardButton(text="ПКМ", callback_data="mouse_PKM")],
    [InlineKeyboardButton(text="◀️", callback_data="mouse_left"), InlineKeyboardButton(text="⬜️", callback_data="AFK"), InlineKeyboardButton(text="▶️", callback_data="mouse_right")],
    [InlineKeyboardButton(text="❌", callback_data="block"), InlineKeyboardButton(text="🔽", callback_data="down"), InlineKeyboardButton(text="⭕️", callback_data="unlocking")]

])