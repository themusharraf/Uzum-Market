from aiogram import types

btn = [
    [types.KeyboardButton(text="Telefonlar"), types.KeyboardButton(text="Aksessuarlar")],
    [types.KeyboardButton(text="Admin")]

]
button = types.ReplyKeyboardMarkup(keyboard=btn, resize_keyboard=True)
