import re
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command, CommandStart, Text
from aiogram.utils.markdown import hbold, hcode, hide_link, hlink, hitalic
from aiogram.dispatcher.storage import FSMContext

from bot.dictionary import start_menu, dictionary_button, ListDictionaries

async def start(message: types.Message, state:FSMContext):
    """ Запуск бота """
    await message.answer(f"Привет {message.from_user.first_name}", reply_markup=start_menu)


async def menu_dictionary(
    message: types.Message, list_dictionaries: ListDictionaries):
    """ Словари """
    await message.answer(
        f"{message.from_user.first_name} Выбери словарь: ",
        reply_markup=list_dictionaries.dictionari_menu())


async def show_dictionary(
    call: types.CallbackQuery, list_dictionaries: ListDictionaries):
    _, category = call.data.split(":")
    text = list_dictionaries.get_by_name(category).get()
    await call.message.edit_text(
        f"Словарь категории {category}\n {text}")

### Свалка 
async def shit(message: types.Message):
    await message.reply(f'Нажмите /start', parse_mode=types.ParseMode.MARKDOWN)


def register_commands(dp: Dispatcher):
    """ Регистратор команд """
    # Стартовое меню
    dp.register_message_handler(start, CommandStart(deep_link=re.compile('\d+')) | Command("start"), state='*')   
    
    # Меню словарей
    dp.register_message_handler(menu_dictionary, Text(equals="📊 Словари") | Command('dict'))
    # Словарь
    dp.register_callback_query_handler(show_dictionary, dictionary_button.filter())
    # Мусор 
    dp.register_message_handler(shit, content_types=types.ContentType.ANY, state='*')   