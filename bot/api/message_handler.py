import telebot
from telebot import types

file = open('../../resourses/bot_info.txt', 'r')
token = file.readline().split()[2]
bot = telebot.TeleBot(token)
amount = 0
name = ''


@bot.message_handler(content_types=['text'])
def handle(message):
    check_messages(message)
    #   bot.register_next_step_handler(message, check_messages)


def get_user_name(message):
    global name
    name = message.from_user.first_name


def check_messages(message):
    if message.text == '/help':
        bot.send_message(message.from_user.id, 'Нажми /start')
    elif message.text == '/exit':
        bot.stop_bot()
    elif message.text == '/start':
        #    bot.register_next_step_handler(message, send_welcome)
        send_welcome(message)
    else:
        bot.send_message(message.from_user.id, 'Я тебя не понимаю, нажми /start')


def send_welcome(message):
    get_user_name(message)
    bot.send_message(message.from_user.id, 'Привет, ' + name + '!')
    bot.send_message(message.from_user.id, 'Я умный бот, который поможет тебе разобраться с правильным '
                                           'вложением твоих денег!')
    bot.send_message(message.from_user.id, 'С моей помощью ты сможешь выбрать один из следующих банков: '
                                           'Альфа, втб и тд потом заполним')
    bot.send_message(message.from_user.id, 'Давай приступим! Введи сумму вклада')
    bot.register_next_step_handler(message, ask_about_amount)


def ask_about_amount(message):
    global amount
    while amount <= 0:
        try:
            amount = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')

    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='agreement')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='disagreement')
    keyboard.add(key_no)
    bot.send_message(message.from_user.id, text='Ты хочешь оформить вклад на сумму: ' + str(amount) + '?',
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "agreement":
        msg = 'Класс! Вот, посмотри подобранные мной варианты: '
    if call.data == "disagreement":
        msg = 'Напиши /start'
    bot.send_message(call.message.chat.id, msg)


bot.polling(none_stop=True, interval=0)
