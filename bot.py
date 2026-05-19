# ===== FLASK API =====

# =========================
# TON Mining Game Backend
# Flask + Telebot (FINAL)
# =========================

import sqlite3
import time
import telebot

# CONFIG
BOT_TOKEN = "8840003564:AAGdvQ32_6SOqgJYzjy0xTxERFc3JlytRoY"
bot = telebot.TeleBot(BOT_TOKEN)

# CONSTANTS
MINING_DURATION = 3600
BASE_SPEED = 100
BOOST_AMOUNT = 50
TON_PER_QUBIT = 0.00000000002
MIN_WITHDRAW = 0.01

# DATABASE
def db():
    return sqlite3.connect("database.db", check_same_thread=False)

# (init_db, get_user, create_user, calculate_mining)
# 👉 ဒီ functions တွေအကုန် bot.py ထဲမှာထား

# ===== TELEGRAM BOT =====
# 👉 /start, /mine, /task, /wallet, /withdraw အကုန်ထား

# ===== RUN =====
bot.infinity_polling()

from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
