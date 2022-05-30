import telebot
from telebot import types
from bot.api.user_input import UserInput
from bot.response import bot_response
from bot.response import month_count_buttons_info
from bot.api.message_handler_constants import MessageHandlerConstants

file = open('../../resources/bot_info.txt', 'r')
token = file.readline().split()[2]
bot = telebot.TeleBot(token)
amount = 0
name = 'Человек'
term = -1
user_input = UserInput("", 0, 0)
is_amount_ready = False
month_keys = {}


@bot.message_handler(commands=['start'])
def handle_start(message):
    """Обработчик команды /start.

        Аргументы:

        message: полная информация от пользователя из телеграмма

        Запускает бота и вызывает первые методы
        """
    global is_amount_ready, month_keys, amount, term, name
    month_keys = {}
    is_amount_ready = False
    amount = 0
    term = -1
    name = 'Человек'
    user_input.set_name(new_name='Человек')
    user_input.set_amount(new_amount=0)
    user_input.set_month_count(new_term=0)
    send_welcome(message)
    bot.send_message(message.from_user.id, MessageHandlerConstants.tell_amount)


@bot.message_handler(commands=['help'])
def handle_help(message):
    """Обработчик команды /help.

            Аргументы:

            message: полная информация от пользователя из телеграмма

            Дает справку как запустить бота
            """
    bot.send_message(message.from_user.id, MessageHandlerConstants.for_help_command)


@bot.message_handler(commands=['exit'])
def handle_exit(message):
    """Обработчик команды /exit.

            Аргументы:

            message: полная информация от пользователя из телеграмма

            Останавливает бота
            """
    bot.send_message(message.from_user.id, MessageHandlerConstants.for_exit_command)
    bot.stop_polling()


@bot.message_handler(commands=['amount_again'])
def handle_amount_again(message):
    """Обработчик команды /amount_again.

            Аргументы:

            message: полная информация от пользователя из телеграмма

            Спрашивает заново сумму от пользователя
            """
    global amount
    amount = 0
    user_input.set_amount(new_amount=amount)
    bot.send_message(message.from_user.id, MessageHandlerConstants.for_amount_again_command)
    bot.register_next_step_handler(message, ask_about_amount)


@bot.message_handler(content_types=['text'])
def handle_messages(message):
    """Обработчик сообщений.

            Аргументы:

            message: полная информация от пользователя из телеграмма

            Обрабатывает обычные сообщения от пользователя
            """
    user_input.print_data()
    print('Срок' + str(term))
    if not is_amount_ready:
        ask_about_amount(message)
    elif term >= 0:
        show_results(message.from_user.id)
    else:
        bot.send_message(message.from_user.id, MessageHandlerConstants.unclear_message)


def get_user_name(message):
    """Метод узнает имя пользователя.

            Аргументы:

            message: полная информация от пользователя из телеграмма
            """
    global name
    name = message.from_user.first_name
    user_input.set_name(new_name=name)
    user_input.print_data()
    print('Имя: ' + str(name))


def send_welcome(message):
    """Бот присылает приветственные сообщения.

            Аргументы:

            message: полная информация от пользователя из телеграмма
            """
    get_user_name(message)
    bot.send_message(message.from_user.id, 'Привет, ' + name + '!')
    bot.send_message(message.from_user.id, MessageHandlerConstants.about_bot)
    bot.send_message(message.from_user.id, MessageHandlerConstants.about_bot_next)


def ask_about_term(message):
    """Бот узнает, важен ли пользователю срок.

            Аргументы:

            message: полная информация от пользователя из телеграмма
            """
    global term
    term = -1
    user_input.set_month_count(new_term=0)
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Выбрать срок', callback_data='agree_term')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='Пропустить', callback_data='disagree_term')
    keyboard.add(key_no)
    bot.send_message(message, text=MessageHandlerConstants.ask_about_term, reply_markup=keyboard)


def ask_about_term_next(message):
    """Бот уточняет срок у пользователя.

            Аргументы:

            message: полная информация от пользователя из телеграмма
            """
    global month_keys
    keyboard = types.InlineKeyboardMarkup()

    month_list = month_count_buttons_info.get_month_count_from_contributions(user_input)
    for month in month_list:
        i = str(month)
        month_keys[i] = types.InlineKeyboardButton(text=str(month)+' мес.', callback_data=str(month))
        keyboard.add(month_keys[i])

    bot.send_message(message, text=MessageHandlerConstants.ask_term, reply_markup=keyboard)


def ask_about_amount(message):
    """Бот уточняет сумму у пользователя.

                Аргументы:

                message: полная информация от пользователя из телеграмма
                """
    global amount, is_amount_ready
    is_amount_ready = False
    amount = 0
    try:
        amount = abs(int(message.text))
    except Exception:
        bot.send_message(message.from_user.id, MessageHandlerConstants.only_numbers)
        bot.register_next_step_handler(message, ask_about_amount)
        return
    if amount > 0:
        user_input.set_amount(new_amount=amount)
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='agreement')
        keyboard.add(key_yes)
        key_no = types.InlineKeyboardButton(text='Нет', callback_data='disagreement')
        keyboard.add(key_no)
        bot.send_message(message.from_user.id, text=MessageHandlerConstants.clarify_amount + str(amount) + '?',
                         reply_markup=keyboard)
    user_input.print_data()
    print('Сумма: ' + str(amount))


def show_results(message):
    """Вывод результатов пользователю.

                Аргументы:

                message: полная информация от пользователя из телеграмма
                """
    bot.send_message(message, MessageHandlerConstants.show_result)
    result = bot_response.create_response_with_contribution(user_input)
    bot.send_message(message, str(result))


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    """Обработчик кнопок у сообщений.

                Аргументы:

                message: полная информация от пользователя из телеграмма
                """
    global term, is_amount_ready
    msg = call.message.chat.id
    if call.data == "disagree_term":
        term = 0
        show_results(msg)
    if call.data == "agree_term":
        term = -1
        user_input.set_month_count(new_term=0)
        bot.send_message(msg, MessageHandlerConstants.tell_term)
        ask_about_term_next(msg)
    for data, button in month_keys.items():
        if call.data == data:
            term = int(data)
            user_input.set_month_count(new_term=term)
            bot.send_message(msg, 'Твой срок - ' + str(term) + ' мес.')
            show_results(msg)
    if call.data == "agreement":
        bot.send_message(msg, MessageHandlerConstants.tell_term_2)
        is_amount_ready = True
        ask_about_term(msg)
    if call.data == "disagreement":
        is_amount_ready = False
        bot.send_message(msg, MessageHandlerConstants.tell_amount_again)
    user_input.print_data()
    print('Сумма: ' + str(amount))
    print('Срок: ' + str(term))
    print('Имя: ' + str(name))


bot.polling(none_stop=True, interval=0)
