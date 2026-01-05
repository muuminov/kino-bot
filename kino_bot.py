import os
import telebot
from flask import Flask
import threading

app = Flask(__name__)

@app.route('/')
def index():
    return "Bot tirik!"

API_TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Salom! Men hozirgina qayta tushdim. Ishlayapman!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # Bu yerda bot siz yozgan narsani qaytaradi, shunda ishlayotganini bilasiz
    bot.reply_to(message, f"Siz yozdingiz: {message.text}. Bot 100% ishlayapti!")

def run_bot():
    bot.infinity_polling(timeout=20, long_polling_timeout=10)

if __name__ == "__main__":
    threading.Thread(target=run_bot, daemon=True).start()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
