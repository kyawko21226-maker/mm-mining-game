# ===== FLASK API =====

# =========================
# TON Mining Game Backend
# Flask + Telebot (FINAL)
# =========================

import sqlite3
import time
import telebot

# CONFIG
BOT_TOKEN = "8840003564:AAGXM8nRIr6eHFmHGMfW84mj9DEUEK2sNAs"
bot = telebot.TeleBot(BOT_TOKEN)

# CONSTANTS
MINING_DURATION = 3600
BASE_SPEED = 100
BOOST_AMOUNT = 50
TON_PER_QUBIT = 0.00000000002
MIN_WITHDRAW = 0.01

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Welcome to MM Mining Game!")

@bot.message_handler(commands=['mine'])
def mine(message):
    bot.reply_to(message, "Mining started ⛏"

@bot.message_handler(commands=['invite'])
def invite(message):
    bot.reply_to(message, "Your invite link: https://t.me/MMMiningGame_bot")

@bot.message_handler(commands=['withdraw'])
def withdraw(message):
    bot.reply_to(message, "Minimum withdraw is 0.01 TON")

@bot.message_handler(commands=['leaderboard'])
def leaderboard(message):
    bot.reply_to(message, "Top miners coming soon!")

@bot.message_handler(commands=['mystats'])
def mystats(message):
    bot.reply_to(message, "Your balance: 0 TON")

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, "Commands:\n/start\n/mine\n/invite\n/withdraw\n/leaderboard\n/mystats\n/about")

@bot.message_handler(commands=['about'])
def about(message):
    bot.reply_to(message, "MM Mining Game Bot v1")                 

# DATABASE
def db():
    return sqlite3.connect("database.db", check_same_thread=False)

# (init_db, get_user, create_user, calculate_mining)
# 👉 ဒီ functions တွေအကုန် bot.py ထဲမှာထား

# ===== TELEGRAM BOT =====
# 👉 /start, /mine, /task, /wallet, /withdraw အကုန်ထား

# ===== RUN =====
from flask import Flask
import os
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run_bot():
    print("Bot polling started...")
    bot.infinity_polling()

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()

    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
