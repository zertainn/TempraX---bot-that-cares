import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = ""

bot = telebot.TeleBot(TOKEN)

def make_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard = True)
    keyboard.add(KeyboardButton('/start'))
    return keyboard

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Приветствую')
    bot.send_message(message.chat.id, 'Используй команду /help, чтобы узнать о всех доступных командах', reply_markup=make_keyboard())

bot.infinity_polling()
