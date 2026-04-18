import telebot
import os
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = os.environ.get("BOT_TOKEN")
VIDEO_FILE_ID = os.environ.get("VIDEO_FILE_ID")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    text = (
        '<tg-emoji emoji-id="540929790527">🎰</tg-emoji>Scrolling plates — генератор номерных знаков\n\n'
        '<tg-emoji emoji-id="541151978204">🎁</tg-emoji>Получай крутые ежедневные награды в течение недели\n'
        '<tg-emoji emoji-id="540888428274">🎯</tg-emoji>Крути н/з своей страны со всеми регионами\n'
        '<tg-emoji emoji-id="540916651363">🌍</tg-emoji>Доступны страны: Россия, Украина, Беларусь, Казахстан\n'
        '<tg-emoji emoji-id="541135740221">✨</tg-emoji>Украшай номерные знаки разными модификаторами и рамками\n'
        '<tg-emoji emoji-id="541118870449">👥</tg-emoji>Создавай комнату и играй с друзьями в разные режимы\n'
        '<tg-emoji emoji-id="541138466667">⚙️</tg-emoji>Меняй настройки игры под себя, выбери свою удобную тему\n'
        '<tg-emoji emoji-id="540916844636">💰</tg-emoji>Продавай свои номера игрокам на маркетплейсе\n\n'
        '<tg-emoji emoji-id="541136131493">👇</tg-emoji>Присоединяйся, вводи свой регион и крути номера👇'
    )

    keyboard = InlineKeyboardMarkup()
    keyboard.row(InlineKeyboardButton("Играть 🎮", web_app=telebot.types.WebAppInfo("https://snusfnf-png.github.io/cardrop/")))
    keyboard.row(
        InlineKeyboardButton("Наш чат💬", url="https://t.me/chatcarzdrop"),
        InlineKeyboardButton("Наш канал📢", url="https://t.me/carzdrop")
    )

    bot.send_video(
        chat_id=message.chat.id,
        video=VIDEO_FILE_ID,
        caption=text,
        parse_mode="HTML",
        reply_markup=keyboard
    )

@bot.message_handler(content_types=['video'])
def get_video_id(message):
    bot.send_message(message.chat.id, message.video.file_id)
print("Бот запущен...")
bot.infinity_polling()
