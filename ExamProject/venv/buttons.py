import telebot
from telebot import types

def KeyboardButtons(n):
    buttons = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Избранные')
    btn2 = types.KeyboardButton('История')
    buttons.row(btn1, btn2)
    return buttons



def more_button(word):
    btn = types.InlineKeyboardButton('Подробнее', url=f'https://ru.wikipedia.org/wiki/{word}')
    return btn

def add_favorietes_button(n):
    btn = types.InlineKeyboardButton('Добавить в избранные ⭐', callback_data='text')
    return btn

