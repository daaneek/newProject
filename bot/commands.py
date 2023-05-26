import re
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command, CommandStart, Text
from aiogram.utils.markdown import hbold, hcode, hide_link, hlink, hitalic
from aiogram.dispatcher.storage import FSMContext

from bot.keyboards import start_menu




async def start(message: types.Message, state:FSMContext):
    """ Запуск бота """
    await message.answer(f"Привет {message.from_user.first_name}", reply_markup=start_menu)


### Стартовое меню
async def menu_dict(message: types.Message, state: FSMContext):
    """ Словари """
    # TODO реализовать подгрузку словарей держать их в генераторах чтобы не потребляли память

### Свалка 
async def shit(message: types.Message):
    await message.reply(f'Нажмите /start', parse_mode=types.ParseMode.MARKDOWN)


def register_commands(dp: Dispatcher):
    """ Регистратор команд """
    dp.register_message_handler(start, CommandStart(deep_link=re.compile('\d+')) | Command("start"), state='*')   # Стартовое меню