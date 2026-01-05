import os
import telebot
from flask import Flask # Buni qo'shamiz

server = Flask(__name__) # Sayt yaratamiz
API_TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(API_TOKEN)

@server.route("/")
def webhook():
    return "Bot ishlayapti!", 200

# Botingni qolgan kodlari shu yerda bo'ladi...

if __name__ == "__main__":
    # Botni alohida oqimda yurgizamiz
    import threading
    threading.Thread(target=bot.infinity_polling).start()
    # Saytni yoqamiz
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
