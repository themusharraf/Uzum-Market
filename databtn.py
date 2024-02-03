from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

choice = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Xiaomi Redmi 13C', callback_data='btn1'),
     InlineKeyboardButton(text='TECNO Spark Go', callback_data='btn2')],
    [InlineKeyboardButton(text='Honor X8b ', callback_data='btn3'),
     InlineKeyboardButton(text='Samsung Galaxy A24', callback_data='btn4')],

])

from aiogram import types

ph = [
    [types.KeyboardButton(text="Telefon raqam📞", request_contact=True)],

]
phbtn = types.ReplyKeyboardMarkup(keyboard=ph, resize_keyboard=True)
