import telebot
import telebot_mem
import os

from telebot_mem import MongoMem

API_TOKEN = os.environ['TELEGRAM_API_TOKEN']
bot = telebot.TeleBot(API_TOKEN)

memdb = MongoMem("mongodb://localhost:27017/", "telegram")
memdb.validate()
# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
@memdb.memorize
def echo_message(message):
    bot.reply_to(message, memdb.get_last_message().get("text", "I don't know what to say"))

bot.infinity_polling()

