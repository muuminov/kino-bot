import os
import telebot
from flask import Flask
import threading

app = Flask(__name__)

@app.route('/')
def index():
    return "Kino bot 24/7 rejimida ishlayapti!"

API_TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(API_TOKEN)

# 🎬 KINO BAZASI - Hamma 5 ta kinoni kiritdim
kino_bazasi = {
    "101": "BAACAgEAAxkBAAM7aVvYsmtCsj-mUOPvjBalnYHARxUAAnECAAIF-UhHbxCnbW9U_v84BA",
    "102": "BAACAgQAAxkBAAM8aVvYshdHRtdH1rMfMFcYW13XcJ8AAloXAAIDAyhS49H7OoIk1Us4BA",
    "103": "BAACAgIAAxkBAAM9aVvYsqM3kWcuBUH36oR90lIKIMMAAp46AALZxDFLcZmZyuUjOy04BA",
    "104": "BAACAgQAAxkBAAM-aVvYssjNI7YNuTmLk7OwwRLi_GwAAtYRAAJPbPhSa5dhQwqkMZo4BA",
    "105": "BAACAgQAAxkBAAM_aVvYsvfueD_R3blR34Nn3dlSop0AAjYUAALm_BFTgFOjf73Kbf04BA",
}

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Salom! Men tayyorman. Kino kodini yuboring!\nAgar yangi kino qo'shmoqchi bo'lsangiz, menga video yuboring, men sizga ID beraman.")

# 🎥 Video yuborsangiz, sizga uning ID sini beradi (Admin uchun qulaylik)
@bot.message_handler(content_types=['video'])
def get_video_id(message):
    file_id = message.video.file_id
    bot.reply_to(message, f"Ushbu videoning yangi ID kodi:\n\n`{file_id}`", parse_mode="Markdown")

# 🔍 Kino qidirish funksiyasi
@bot.message_handler(func=lambda message: True)
def find_kino(message):
    kod = message.text
    if kod in kino_bazasi:
        file_id = kino_bazasi[kod]
        try:
            bot.send_video(message.chat.id, file_id, caption=f"🎬 Mana siz qidirgan kino!\nKodi: {kod}")
        except Exception as e:
            bot.reply_to(message, "❌ Bu kino kodi (ID) eskirgan ko'rinadi. Iltimos, videoni qayta yuklab yangi ID oling.")
    else:
        bot.reply_to(message, "❌ Kechirasiz, bu kod bilan kino topilmadi.")

def run_bot():
    bot.infinity_polling(timeout=20, long_polling_timeout=10)

if __name__ == "__main__":
    threading.Thread(target=run_bot, daemon=True).start()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

