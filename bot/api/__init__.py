import telebot
bot = telebot.TeleBot('%InvestmentBot%')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Привет, меня зовут Вклад-бот. Я помогу тебе выбрать вклад с лучшими условиями в банках Екатеринбурга\nЧтобы продолжить, введите начальную сумму вклада")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши /start")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


bot.polling(none_stop=True, interval=0)
