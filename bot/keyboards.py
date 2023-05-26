from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

start_menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='📊 Словари')],
    [ KeyboardButton(text='👤 Профиль'), KeyboardButton(text='✅ Правила')]
], resize_keyboard=True, one_time_keyboard=True)
