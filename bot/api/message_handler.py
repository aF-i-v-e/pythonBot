import telebot
from telebot import types
from bot.api.user_input import UserInput
from bot.response import bot_response
from bot.response import month_count_buttons_info
from bot.response.bot_response_constants import BotResponseConstants

file = open('../../resources/bot_info.txt', 'r')
token = file.readline().split()[2]
bot = telebot.TeleBot(token)
amount = 0
name = BotResponseConstants.user_name
term = 0
user_input = UserInput("", 0, 0)
is_amount_ready = False
is_term_ready = False
need_term = False
month_keys = {}


@bot.message_handler(commands=['start'])
def handle_start(message):
    """Обработчик команды /start.

        Аргументы:

        message: полная информация от пользователя из телеграмма

        Запускает бота и вызывает первые методы
        """
    global is_amount_ready, is_term_ready, need_term, month_keys
    month_keys = {}
    is_amount_ready = False
    is_term_ready = False
    need_term = False
    send_welcome(message)
    bot.send_message(message.from_user.id, BotResponseConstants.input_sum_response)
    # ask_about_amount(message)
    # ask_about_term(message)


@bot.message_handler(commands=['help'])
def handle_help(message):
    """Обработчик команды /help.

            Аргументы:

            message: полная информация от пользователя из телеграмма

            Дает справку как запустить бота
            """
    bot.send_message(message.from_user.id, BotResponseConstants.push_start_response)


@bot.message_handler(commands=['exit'])
def handle_exit(message):
    """Обработчик команды /exit.

            Аргументы:

            message: полная информация от пользователя из телеграмма

            Останавливает бота
            """
    user_input.set_name(new_name=BotResponseConstants.user_name)
    user_input.set_amount(new_amount=0)
    user_input.set_month_count(new_term=0)
    user_input.print_data()
    bot.send_message(message.from_user.id, BotResponseConstants.goodbye_response)
    bot.stop_polling()


@bot.message_handler(commands=['amount_again'])
def handle_amount_again(message):
    """Обработчик команды /amount_again.

            Аргументы:

            message: полная информация от пользователя из телеграмма

            Спрашивает заново сумму от пользователя
            """
    bot.send_message(message.from_user.id, BotResponseConstants.input_sum_response)
    bot.register_next_step_handler(message, ask_about_amount)


@bot.message_handler(content_types=['text'])
def handle_messages(message):
    """Обработчик сообщений.

            Аргументы:

            message: полная информация от пользователя из телеграмма

            Обрабатывает обычные сообщения от пользователя
            """
    user_input.print_data()
    print(BotResponseConstants.term + str(term))
    if not is_amount_ready:
        ask_about_amount(message)
    elif not is_term_ready:
        ask_about_term(message)
        if need_term:
            ask_about_term_next(message)
        else:
            bot.send_message(message.from_user.id, BotResponseConstants.not_understand_response)
    else:
        show_results(message)


def get_user_name(message):
    """Метод узнает имя пользователя.

            Аргументы:

            message: полная информация от пользователя из телеграмма
            """
    global name
    name = message.from_user.first_name
    user_input.set_name(new_name=name)
    user_input.print_data()
    print(BotResponseConstants.name + str(name))


def send_welcome(message):
    """Бот присылает приветственные сообщения.

            Аргументы:

            message: полная информация от пользователя из телеграмма
            """
    get_user_name(message)
    bot.send_message(message.from_user.id, BotResponseConstants.hello + name + '!')
    bot.send_message(message.from_user.id, BotResponseConstants.welcome_response1)
    bot.send_message(message.from_user.id, BotResponseConstants.welcome_response2)


def ask_about_term(message):
    """Бот узнает, важен ли пользователю срок.

            Аргументы:

            message: полная информация от пользователя из телеграмма
            """
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text=BotResponseConstants.choose_term, callback_data='agree_term')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text=BotResponseConstants.miss, callback_data='disagree_term')
    keyboard.add(key_no)
    bot.send_message(message, text=BotResponseConstants.want_to_specified_term,
                     reply_markup=keyboard)


def ask_about_term_next(message):
    """Бот уточняет срок у пользователя.

            Аргументы:

            message: полная информация от пользователя из телеграмма
            """
    global term, month_keys
    term = 0
    user_input.set_month_count(new_term=0)
    keyboard = types.InlineKeyboardMarkup()
    # key_3months = types.InlineKeyboardButton(text='3 месяца', callback_data='3months')
    # keyboard.add(key_3months)
    # key_9months = types.InlineKeyboardButton(text='9 месяцев', callback_data='9months')
    # keyboard.add(key_9months)
    # key_year = types.InlineKeyboardButton(text='1 год', callback_data='1year')
    # keyboard.add(key_year)
    # key_more = types.InlineKeyboardButton(text='Более', callback_data='more')
    # keyboard.add(key_more)

    month_list = month_count_buttons_info.get_month_count_from_contributions(user_input)
    i = ''
    for month in month_list:
        i = str(month)
        month_keys[i] = types.InlineKeyboardButton(text=str(month) + BotResponseConstants.month,
                                                   callback_data=str(month))
        keyboard.add(month_keys[i])

    bot.send_message(message, text=BotResponseConstants.want_to_make_deposit_on, reply_markup=keyboard)


def ask_about_amount(message):
    """Бот уточняет сумму у пользователя.

                Аргументы:

                message: полная информация от пользователя из телеграмма
                """
    global amount
    amount = 0
    # user_input.set_amount(new_amount=0)
    try:
        amount = abs(int(message.text))
    except Exception:
        bot.send_message(message.from_user.id, BotResponseConstants.digits_please_response)
        bot.register_next_step_handler(message, ask_about_amount)
        return
    if amount > 0:
        user_input.set_amount(new_amount=amount)
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text=BotResponseConstants.yes, callback_data='agreement')
        keyboard.add(key_yes)
        key_no = types.InlineKeyboardButton(text=BotResponseConstants.no, callback_data='disagreement')
        keyboard.add(key_no)
        bot.send_message(message.from_user.id, text=BotResponseConstants
                         .want_to_make_deposit_on_sum + str(amount) + '?'
                         , reply_markup=keyboard)
    user_input.print_data()
    print(BotResponseConstants.sum + str(amount))


def show_results(message):
    bot.send_message(message, BotResponseConstants.look_at_options)
    result = bot_response.create_response_with_contribution(user_input)
    bot.send_message(message, str(result))


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    """Обработчик кнопок у сообщений.

                Аргументы:

                message: полная информация от пользователя из телеграмма
                """
    global term, need_term, is_term_ready, is_amount_ready
    msg = call.message.chat.id
    if call.data == "disagree_term":
        is_term_ready = False
        need_term = False
        term = 0
        user_input.set_month_count(new_term=term)
        # bot.send_message(msg, 'Введи сумму вклада')
        show_results(msg)
    if call.data == "agree_term":
        term = -1
        is_term_ready = False
        need_term = True
        user_input.set_month_count(new_term=term)
        bot.send_message(msg, BotResponseConstants.good_and_choose_term)
        ask_about_term_next(msg)
    for data, button in month_keys.items():
        if call.data == data:
            term = int(data)
            user_input.set_month_count(new_term=term)
            bot.send_message(msg, BotResponseConstants.your_term + str(term) + BotResponseConstants.month)
            show_results(msg)
    # if call.data == "3months":
    #     term = 3
    #     user_input.set_month_count(new_term=term)
    #     bot.send_message(msg, 'Твой срок - 3 месяца')
    #     bot.send_message(msg, 'Введи сумму вклада')
    # if call.data == "9months":
    #     term = 9
    #     user_input.set_month_count(new_term=term)
    #     bot.send_message(msg, 'Твой срок - 9 месяцев')
    #     bot.send_message(msg, 'Введи сумму вклада')
    # if call.data == "1year":
    #     term = 12
    #     user_input.set_month_count(new_term=term)
    #     bot.send_message(msg, 'Твой срок - 1 год')
    #     bot.send_message(msg, 'Введи сумму вклада')
    # if call.data == "more":
    #     term = 36
    #     user_input.set_month_count(new_term=term)
    #     bot.send_message(msg, 'Твой срок - более 1 года')
    #     bot.send_message(msg, 'Введи сумму вклада')
    if call.data == "agreement":
        bot.send_message(msg, BotResponseConstants.good_and_choose_term)
        is_amount_ready = True
        ask_about_term(msg)
        # bot.send_message(msg, 'Класс! Вот, посмотри подобранные мной варианты: ')
        # result = bot_response.create_response_with_contribution(user_input)
        # bot.send_message(msg, str(result))
    if call.data == "disagreement":
        is_amount_ready = False
        bot.send_message(msg, BotResponseConstants.input_sum_response_again)
    user_input.print_data()
    print(BotResponseConstants.sum + str(amount))
    print(BotResponseConstants.term + str(term))
    print(BotResponseConstants.name + str(name))


bot.polling(none_stop=True, interval=0)
