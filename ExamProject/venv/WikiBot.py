# Подключение библиотек и модулей
import wikipedia
import telebot
from telebot import types
from module import check_surname

wikipedia.set_lang('ru')
bot = telebot.TeleBot('token')

# Запуск бота, приветствие
@bot.message_handler(commands=['start'])
def start(message):
    send_mess = f'<b>{message.from_user.first_name} {check_surname(message.from_user.last_name)},Добро пожаловать в WikiBot!</b> \nС этим ботом вы можете найти абсолютно обо всём что вас интересует \nЧтобы начать поиск, просто напишите мне'
    bot.send_message(message.chat.id, send_mess, parse_mode='html')


#Помощь
@bot.message_handler(commands=['help'])
def start(message):
    bot.send_message(message.chat.id, '*Информация как пользоваться этим ботом*')


# Поиск статьи
@bot.message_handler(content_types=['text'])
def mess(message):
    word = message.text.strip().lower()
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Подробнее', url=f'https://ru.wikipedia.org/wiki/{word}'))
    try:
        final_mess = wikipedia.summary(word)
    except wikipedia.exceptions.PageError:
        final_mess = ''
        bot.send_message(message.chat.id, f'Не очень вас понял😕\nПопробуйте написать слово или термин')
    else:
        bot.send_message(message.chat.id, f'{final_mess}\n<b>Статья из официальных источников Википедии🌐</b>', reply_markup=markup, parse_mode='html')







bot.polling(none_stop=True)