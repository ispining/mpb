import telebot
import sqlite3

DEBUG = True
ADMIN_ID = 1806892656

token = "8184597620:AAFzW-71EkcsL_xgm_RLTsDcbZCnTUaL1-4"

bot = telebot.TeleBot(token, parse_mode="HTML")

kmarkup = telebot.types.InlineKeyboardMarkup
btn = telebot.types.InlineKeyboardButton


class Database:
    def __init__(self):
        self.db = None
        self.sql = None

    def connect(self) -> None:
        self.db = sqlite3.connect("src/database.db")
        self.sql = self.db.cursor()

    def close(self) -> None:
        for i in [self.sql, self.db]:
            try:
                i.close()
            except:
                pass

    def __enter__(self) -> tuple:
        self.connect()
        return self.db, self.sql

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()


