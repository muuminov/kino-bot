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
    "101": "BAACAgEAAxkBAAM7aVvYsmtCsj-mUOPvjBalnYHARxUAAnECAAIF-UhHbxCnbW9U_v84BA", #forsaj 10",
    "102": "BAACAgQAAxkBAAM8aVvYshdHRtdH1rMfMFcYW13XcJ8AAloXAAIDAyhS49H7OoIk1Us4BA", #oyda yolg'iz",
    "103": "BAACAgIAAxkBAAM9aVvYsqM3kWcuBUH36oR90lIKIMMAAp46AALZxDFLcZmZyuUjOy04BA", #mening iblisim 1",
    "104": "BAACAgQAAxkBAAM-aVvYssjNI7YNuTmLk7OwwRLi_GwAAtYRAAJPbPhSa5dhQwqkMZo4BA", #mening iblisim 2",
    "105": "BAACAgQAAxkBAAM_aVvYsvfueD_R3blR34Nn3dlSop0AAjYUAALm_BFTgFOjf73Kbf04BA", #mening iblisim 3",
    "106": "BAACAgUAAyEFAATNH_mnAAMHaVv-7_q_jHXR3x5FoecPDuxHrFgAArkZAAKokAlUOwyt3j5An5U4BA", #ono 1",
    "107": "BAACAgUAAyEFAATNH_mnAAMIaVv-71tV2H3C3-MUmeT6qPUZXhsAAj0cAAKtvklUVTF0mwzNypo4BA", #ono 2",
    "108": "BAACAgUAAyEFAATNH_mnAAMJaVv-71YpU8ENkv_wrER8V_u36UgAAtAdAAKegKhUvivyhgr3HNo4BA", #ono 3",
    "109": "BAACAgIAAyEFAATNH_mnAAMKaVv-72a5190lPZeNVMW_SPyVGRMAAsuSAAIo9fFI4OykFYuMpWM4BA", #ono 4",
    "110": "BAACAgUAAyEFAATNH_mnAAMLaVv-7842hHnoSmaCsPeSYFbcQl8AArAaAAIobjhVTLmcQUBz9i84BA", #ono 5",
    "111": "BAACAgIAAyEFAATNH_mnAAMMaVv-79bYOtzzHj6LsuhBquBhIigAAsGMAAJamHlJjenvAc5K51Q4BA", #ono 6",
    "112": "BAACAgIAAyEFAATNH_mnAAMNaVv-75GlrHR1hzBbM0xd6oiJQf0AAp-dAALa7NBJXJHT2mG6Las4BA", #ono 7",
    "113": "BAACAgUAAyEFAATNH_mnAAMOaVv-71lYgeTxHvyWrQwr5gwY_LwAAkAaAAKFLBBWTA8JHEwF-fo4BA", #ono 8",
    "114": "BAACAgIAAxkBAAIBYWlhOkNBCn5oaxPgf57uFEjSESQ4AAIeBAACqqxYSdw7snnZHDJcOAQ", #sumerki 1",
    "115": "BAACAgIAAxkBAAIBYmlhOkOQCoEvaLy5-hjzTitUrdK4AALGAwACx0RYSfQnWs1AHGS_OAQ", #sumerki 2",
    "116": "BAACAgIAAxkBAAIBY2lhOkN0wfj3KI7K6bUltZaBTB5VAAJIBAACqqxYSdBIKucInj3VOAQ", #sumerki 3",
    "117": "BAACAgIAAxkBAAIBZGlhOkO-UNoUDBg7VP66uFMLMRHdAAIVBAACx0RYSQ88zXBDQZnhOAQ", #sumerki 4",
    "118": "BAACAgIAAxkBAAIBZWlhOkOiyXLkzvbMHYYtYW-Wke7tAALcAgACRmUJSv8jWnvquivkOAQ", #sumerki 5",
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



