import os
import telebot
from flask import Flask
import threading

# Flask server yaratamiz (Render o'chirib qo'ymasligi uchun)
app = Flask(__name__)

@app.route('/')
def index():
    return "Bot ishlamayapti emas, bot tirik!"

# Botni sozlaymiz
API_TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(API_TOKEN)

# KINO BAZASI
kino_bazasi = {
    "101": "BAACAgQAAxkBAAMJaVqx79KJBD7w-hDmYndKZbPVzs4AAloXAAIDAYhS49H7OoIk1Us4BA",
    "102": "BAACAgEAAxkBAAMHaVqx9qG6QUvr90_8Qk4gidNBE08MAAnECAAI F-UhHbxCnbW9U_v84BA",
    "103": "BAACAgIAAxkBAAMKaVqx79zcV0ZO9BdMoP14GLusYmUAAP46AALZxDFLcZmZyuUjOy04BA",
    "104": "BAACAgQAAxkBAAMLaVqx78kR9cDBMeyeJjzxZq_4B7UAAtYRAAJPbPhSa5dhQwqkMZo4BA",
    "105": "BAACAgQAAxkBAAMMaVqx78fG0RyfB7z-19LoE5Pxn8AAJyYUAAI m_BftgFOjf73kbf04BA",
}

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Salom! Bot qayta yoqildi. Kino kodini yuboring!")

@bot.message_handler(func=lambda message: True)
def find_kino(message):
    kod = message.text
    if kod in kino_bazasi:
        file_id = kino_bazasi[kod]
        bot.send_video(message.chat.id, file_id, caption=f"🎬 Mana siz qidirgan kino!\nKodi: {kod}")
    else:
        bot.reply_to(message, "❌ Kechirasiz, bu kod bilan kino topilmadi.")

# Botni alohida oqimda (thread) yurgizish funksiyasi
def run_bot():
    bot.infinity_polling(timeout=10, long_polling_timeout=5)

if __name__ == "__main__":
    # 1. Botni alohida oqimda ishga tushiramiz
    threading.Thread(target=run_bot, daemon=True).start()
    # 2. Flask saytni Render portida ishga tushiramiz
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
