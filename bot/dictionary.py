import json
from pathlib import Path
from aiogram.types import (
    InlineKeyboardMarkup, InlineKeyboardButton,
    ReplyKeyboardMarkup, KeyboardButton)
from aiogram.utils.callback_data import CallbackData
from bot.utils import IterableAdapter


# Стартовое меню через ReplyKeyboardMarkup
start_menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='📊 Словари')],
    [KeyboardButton(text='👤 Профиль'), KeyboardButton(text='✅ Правила')]
], resize_keyboard=True, one_time_keyboard=True)


dictionary_button = CallbackData("dictionary", "category")


class FileDictionari:
    def __init__(self, path_dictionary: str, name: str):
        self.name = name
        self.path_dictionary = path_dictionary
        self.dictionary = IterableAdapter(lambda: self.open_file())

    def open_file(self):
        with open(file=self.path_dictionary, mode="r") as file:
            yield json.load(file)

    def get(self):
        return next(self.dictionary)

    def __repr__(self) -> str:
        return self.name


class ListDictionaries:
    def __init__(self, path_dir_dictionary: str):
        self.path_dir_dictionari = path_dir_dictionary
        self.list_dictionary = IterableAdapter(lambda: self.open())
        self._len = 0

    def open(self):
        for path_file_dictionary in Path("bot/data/").glob("*.json"):
            self._len += 1
            yield FileDictionari(
                path_file_dictionary, path_file_dictionary.stem)

    def dictionari_menu(self):
        """ Меню Словарей """
        if self._len % 2 == 0:
            menu = [
                [InlineKeyboardButton(
                    text=f'{dictionary}', callback_data=dictionary_button.new(
                        category=dictionary
                    ))
                 for dictionary in self.list_dictionary]]
        else:
            menu = [[InlineKeyboardButton(
                text=f'{dictionary}', callback_data=dictionary_button.new(
                    category=dictionary))]
                    for dictionary in self.list_dictionary]
        menu.append([InlineKeyboardButton(
            text='⬅️ Назад', callback_data='📊 .Catalog')])
        return InlineKeyboardMarkup(inline_keyboard=menu)

    def get_by_name(self, name: str):
        for dictionary in self.list_dictionary:
            if dictionary.name == name:
                return dictionary
