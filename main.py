import telebot

bot = telebot.TeleBot('here should be a token')


@bot.message_handler(commands=['start'])
def start(f, res=False):
    bot.send_message(f.chat.id, 'Я на связи. Напиши мне что-нибудь )')


@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.chat.id, 'Вы написали: ' + message.text)


bot.polling(none_stop=True, interval=0)