import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import os

TOKEN = ""
USER_FILE = "users.txt"

bot = telebot.TeleBot(TOKEN)

def make_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard = True)
    keyboard.add(KeyboardButton('/start'))
    keyboard.add(KeyboardButton('/help'))
    return keyboard


def load_known_users():
    if not os.path.exists(USER_FILE):
        return set()
    with open(USER_FILE, "r") as f:
        return set(line.strip() for line in f.readlines())


def save_new_user(user_id):
    with open(USER_FILE, "a") as f:
        f.write(f"{user_id}\n")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = str(message.from_user.id)
    username = message.from_user.first_name or message.from_user.username or "there"
    known_users = load_known_users()

    if user_id not in known_users:
        save_new_user(user_id)
        greeting = (
            f"Приветствую {username}! 👋\n\n"
            "Добро пожаловать в TempraX 🎉\n"
            "Вижу ты тут первый раз, так что раскажу кто я и для чего я 👀\n"
            "Я бот, который тебе раскажет о серьёзности глобального потепление, но в очень интересном виде 🔮\n"
            "Меня создали, чтобы я распространил как можно большей аудитории об этой проблеме и спасти планету 🦸‍♂️\n"
            )
    else:
        greeting = (
            f"С возвращением, {username}! 👋\n"
            "Чем могу помочь сегодня?👀"
            )

    bot.send_message(message.chat.id, greeting, reply_markup=make_keyboard())

@bot.message_handler(commands=['help'])
def send_help(message):
    help = (
        f"Вот здесь все мои возможности 👇\n\n"
        ""
    )

    bot.send_message(message.chat.id, help, reply_markup=make_keyboard())


print("Бот работает... 🚀")

bot.infinity_polling()
