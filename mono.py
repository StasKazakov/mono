import telebot
from telebot import types
from config import BOT_TOKEN, whitelist
from transactions import get_transactions
from datetime import datetime

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.id in whitelist:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        get_key = types.KeyboardButton('💵')
        markup.add(get_key)

        bot.send_message(message.chat.id, "🚀", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "This is private bot")


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == '💵':
        transactions = get_transactions()
        current_date = datetime.now().strftime('%d.%m.%Y')
        response_message = f"📅 <b>{current_date}</b>\n\n"
        for transaction in transactions:
            response_message += f'🕔 {transaction.time}\n👩🏻‍🦰 {transaction.description}\n💸 <b>{transaction.amount} грн</b>\n\n'
        bot.send_message(message.chat.id, response_message.strip(), parse_mode='html')


try:
    bot.polling(none_stop=True)
except Exception as e:
    bot.send_message(499507850, 'alarm')
    print(e)
