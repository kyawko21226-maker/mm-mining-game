# ===== FLASK API =====

# =========================
# TON Mining Game Backend
# Flask + Telebot (FINAL)
# =========================

import sqlite3
import time
import telebot

# CONFIG
BOT_TOKEN = "YOUR_BOT_TOKEN"
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