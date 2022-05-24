import telebot
from telebot import types
from bot.api.user_input import UserInput
from bot.response import bot_response

file = open('../../resources/bot_info.txt', 'r')
token = file.readline().split()[2]
bot = telebot.TeleBot(token)
amount = 0
name = 'Человек'
term = 0
user_input = UserInput
answer = False


@bot.message_handler(commands=['start'])
def handle_start(message):
    user_input('Человек', 0, 0)
    send_welcome(message)
    ask_about_term(message)


@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.from_user.id, 'Нажми /start')


@bot.message_handler(commands=['exit'])
def handle_exit(message):
    user_input.set_name(user_input, new_name='Человек')
    user_input.set_amount(user_input, new_amount=0)
    user_input.set_month_count(user_input, new_term=0)
    user_input.print_data(user_input)
    bot.send_message(message.from_user.id, 'До новых сообщений!')
    bot.stop_polling()


@bot.message_handler(commands=['amount_again'])
def handle_amount_again(message):
    bot.send_message(message.from_user.id, 'Введи сумму вклада')
    bot.register_next_step_handler(message, ask_about_amount)


@bot.message_handler(content_types=['text'])
def handle_messages(message):
    user_input.print_data(user_input)
    print('Срок' + str(term))
    if term == 0:
        bot.send_message(message.from_user.id, 'Я не понимаю тебя, нажми /help')
    elif term < 0:
        ask_about_term_next(message.from_user.id)
    else:
        ask_about_amount(message)


def get_user_name(message):
    global name
    name = message.from_user.first_name
    user_input.set_name(user_input, new_name=name)
    user_input.print_data(user_input)
    print('Имя: ' + str(name))


def send_welcome(message):
    get_user_name(message)
    bot.send_message(message.from_user.id, 'Привет, ' + name + '!')
    bot.send_message(message.from_user.id, 'Я умный бот, который поможет тебе разобраться с правильным '
                                           'вложением твоих денег!')
    bot.send_message(message.from_user.id, 'С моей помощью ты сможешь выбрать один из следующих банков: '
                                           'Альфа, втб и тд потом заполним')


def ask_about_term(message):
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Выбрать срок', callback_data='agree_term')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='Пропустить', callback_data='disagree_term')
    keyboard.add(key_no)
    bot.send_message(message.from_user.id, text='Давай приступим!\nДля начала скажи, ты хотел бы указать срок?',
                                                reply_markup=keyboard)


def ask_about_term_next(message):
    global term
    term = 0
    user_input.set_month_count(user_input, new_term=0)
    keyboard = types.InlineKeyboardMarkup()
    key_3months = types.InlineKeyboardButton(text='3 месяца', callback_data='3months')
    keyboard.add(key_3months)
    key_9months = types.InlineKeyboardButton(text='9 месяцев', callback_data='9months')
    keyboard.add(key_9months)
    key_year = types.InlineKeyboardButton(text='1 год', callback_data='1year')
    keyboard.add(key_year)
    key_more = types.InlineKeyboardButton(text='Более', callback_data='more')
    keyboard.add(key_more)
    bot.send_message(message, text='Ты хочешь оформить свой вклад на: ', reply_markup=keyboard)


def ask_about_amount(message):
    global amount
    amount = 0
    # user_input.set_amount(user_input, new_amount=0)
    try:
        amount = abs(int(message.text))
    except Exception:
        bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
        bot.register_next_step_handler(message, ask_about_amount)
        return
    if amount > 0:
        user_input.set_amount(user_input, new_amount=amount)
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='agreement')
        keyboard.add(key_yes)
        key_no = types.InlineKeyboardButton(text='Нет', callback_data='disagreement')
        keyboard.add(key_no)
        bot.send_message(message.from_user.id, text='Ты хочешь оформить вклад на сумму: ' + str(amount) + '?',
                         reply_markup=keyboard)
    user_input.print_data(user_input)
    print('Сумма: ' + str(amount))


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global term
    msg = call.message.chat.id
    if call.data == "disagree_term":
        term = 0.5
        user_input.set_month_count(user_input, new_term=term)
        bot.send_message(msg, 'Введи сумму вклада')
    if call.data == "agree_term":
        term = -1
        user_input.set_month_count(user_input, new_term=term)
        bot.send_message(msg, 'Отлично! Выбери срок')
        ask_about_term_next(msg)
    if call.data == "3months":
        term = 3
        user_input.set_month_count(user_input, new_term=term)
        bot.send_message(msg, 'Твой срок - 3 месяца')
        bot.send_message(msg, 'Введи сумму вклада')
    if call.data == "9months":
        term = 9
        user_input.set_month_count(user_input, new_term=term)
        bot.send_message(msg, 'Твой срок - 9 месяцев')
        bot.send_message(msg, 'Введи сумму вклада')
    if call.data == "1year":
        term = 12
        user_input.set_month_count(user_input, new_term=term)
        bot.send_message(msg, 'Твой срок - 1 год')
        bot.send_message(msg, 'Введи сумму вклада')
    if call.data == "more":
        term = 36
        user_input.set_month_count(user_input, new_term=term)
        bot.send_message(msg, 'Твой срок - более 1 года')
        bot.send_message(msg, 'Введи сумму вклада')
    if call.data == "agreement":
        bot.send_message(msg, 'Класс! Вот, посмотри подобранные мной варианты: ')
        bot_response.create_response_with_contribution(user_input)
    if call.data == "disagreement":
        bot.send_message(msg, 'Напиши /start')
    user_input.print_data(user_input)
    print('Сумма: ' + str(amount))
    print('Срок: ' + str(term))
    print('Имя: ' + str(name))


bot.polling(none_stop=True, interval=0)
