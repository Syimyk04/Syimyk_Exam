import wikipedia
import telebot
from module import check_surname

wikipedia.set_lang('ru')
bot = telebot.TeleBot('7776305783:AAFgYFrUMRNg32GiUG0MlDmKU86wOjx8mIA')

# Запуск бота, приветствие
@bot.message_handler(commands=['start'])
def start(message):
    send_mess = f'<b>Привет {message.from_user.first_name} {check_surname(message.from_user.last_name)}!</b>\nЧтобы найти то что вам нужно, просто напишите мне и получите ответ'
    bot.send_message(message.chat.id, send_mess, parse_mode='html')


#Помощь
@bot.message_handler(commands=['help'])
def start(message):
    bot.send_message(message.chat.id, '*Информация как пользоваться этим ботом*')


# Поиск статьи
@bot.message_handler(content_types=['text'])
def mess(message):
    word = message.text.strip().lower()
    try:
        final_mess = wikipedia.summary(word)
    except wikipedia.exceptions.PageError:
        final_mess = ''
        bot.send_message(message.chat.id, f'Не очень вас понял😕\nпопробуйте написать точнее')
    bot.send_message(message.chat.id, f'{final_mess}\n<b>Статья из официальных источников Википедии🌐</b>', parse_mode='html')







bot.polling(none_stop=True)