# Подключение библиотек и модулей
import wikipedia
import telebot
import random
from telebot import types
from module import check_surname
from buttons import KeyboardButtons, add_favorietes_button, more_button

wikipedia.set_lang('ru')
bot = telebot.TeleBot('token')



# Запуск бота, приветствие
@bot.message_handler(commands=['start'])
def start(message):
    send_mess = f'<b>{message.from_user.first_name} {check_surname(message.from_user.last_name)}, Добро пожаловать в WikiGram!</b> \nС этим ботом вы можете узнать абсолютно обо всём что вас интересует \nЧтобы начать поиск, просто напишите мне'
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=KeyboardButtons('nothing'))



#Помощь
@bot.message_handler(commands=['help'])
def start(message):
    bot.send_message(message.chat.id, '*Информация как пользоваться этим ботом*')



# Поиск статьи
@bot.message_handler(content_types=['text'])
def mess(message):
    word = message.text.strip().lower()
    ps = '<b>Статья из официальных источников Википедии🌐</b>'

    markup = types.InlineKeyboardMarkup()
    markup.row(add_favorietes_button(word), more_button(word))

    try:
        final_mess = wikipedia.summary(word)
    except wikipedia.exceptions.PageError:
        final_mess = ''
        bot.send_message(message.chat.id, f'Не очень вас понял😕\nПопробуйте написать слово или термин')

    # Если у искомого слова много вариантов
    except wikipedia.exceptions.DisambiguationError as choice_error:
        f = random.choice(choice_error.options)
        final_mess = wikipedia.summary(f)
        bot.send_message(message.chat.id, f'{final_mess}\n{ps}', reply_markup=markup, parse_mode='html')
    else:
        bot.send_message(message.chat.id, f'{final_mess}\n{ps}', reply_markup=markup, parse_mode='html')







bot.polling(none_stop=True)