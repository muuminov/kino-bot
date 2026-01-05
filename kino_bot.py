import telebot

# SHU YERGA BOTFATHERDAN OLINGAN YANGI TOKENNI QO'Y!
API_TOKEN = '8387942640:AAF53VUE6Zd2Wr8vEfq_KZ_eUvFtX5BG_GM'
bot = telebot.TeleBot(API_TOKEN)

# KINO BAZASI
kino_bazasi = {
    "101": "BAACAgQAAxkBAAMJaVqx79KJBD7w-hDmYndKZbpVzs4AAloXAAIDAyhS49H7OoIk1Us4BA", 
    "102": "BAACAgEAAxkBAAMHaVqxq6GOUvr9O_8Qk4GidNBE08MAAnECAAIF-UhHbxCnbW9U_v84BA", 
    "103": "BAACAgIAAxkBAAMKaVqx79zcV0ZO9BdMoP14GLusYmUAAp46AALZxDFLcZmZyuUjOy04BA", 
    "104": "BAACAgQAAxkBAAMLaVqx78kR9cDBMeyeJjZXZq_4B7UAAtYRAAJPbPhSa5dhQwqkMZo4BA", 
    "105": "BAACAgQAAxkBAAMMaVqx78fGORyfB7z-l9Lo0E5Pxn8AAjYUAALm_BFTgFOjf73Kbf04BA", 
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

print("Bot qayta ishga tushdi...")
bot.infinity_polling()