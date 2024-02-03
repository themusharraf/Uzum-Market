import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters.command import Command
from root import TOKEN
from aiogram.types import Message, BotCommand
from buttons import button
from inl_button import btn1
from inl_button import *
from databtn import choice
from databtn import phbtn

bot = Bot(token=TOKEN)

dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer_photo(photo="https://images.app.goo.gl/BzpMtZdoGCiPusTT6",
                               caption=f"Assalomu alaykum {message.from_user.full_name} Bizning 🏪 Uzum Market botimizga xush kelibsiz 👋",
                               reply_markup=button)


@dp.message(F.text == "Telefonlar")
async def phones(message: Message):
    await message.answer_photo(photo="https://images.uzum.uz/clmsv4nn7c6gg9idnb40/original.jpg",
                               caption="Xiaomi Redmi 13C 4 ГБ + 128 ГБ / 8 ГБ+256 ГБ, 6.74 90 Гц,"
                                       " 5000 mAh, Dual SIM,LTE",
                               reply_markup=btn1)
    await message.answer_photo(photo="https://images.uzum.uz/cmru4uh25ku8ad8j8e0g/original.jpg",
                               caption="Smartfon TECNO Spark Go 2024", reply_markup=btn2)
    await message.answer_photo(photo="https://images.uzum.uz/cmue5u9s99ouqbfsum9g/original.jpg",
                               caption="Smartfon Honor X8b 8/128/256 GB, NFC, 2NanoSIM, ko'zni himoya qiluvchi AMOLED ekrani bilan",
                               reply_markup=btn3)
    await message.answer_photo(photo="https://images.uzum.uz/cmrieh925ku8ad8j4ibg/original.jpg",
                               caption="Smartfon Samsung Galaxy A24, 6/128 GB, 6.550 mp, 90hz, sAMOLED, 2SIM, Android 13",
                               reply_markup=btn4)


@dp.message(F.text == "Aksessuarlar")
async def Aksusuarlar(message: Message):
    await message.answer_photo(photo="https://images.uzum.uz/ciopubn5d7kom1tjti90/original.jpg",
                               caption="Simsiz zaryadlovchi Apple va Samsungning telefon, soat va quloqchinlari uchun",
                               reply_markup=btn5)
    await message.answer_photo(photo="https://images.uzum.uz/ck84macvutv5dskpu4f0/original.jpg",
                               caption="G'ilof iPhone 6s,7,8,SE,XR,XS,11,12,13,14,15 Pro, Max, Plus, Mini uchun, shaffof, silikon",
                               reply_markup=btn6)
    await message.answer_photo(photo="https://images.uzum.uz/clsn1ec6pk58gtm69aeg/original.jpg",
                               caption="Dumaloq lampa/Tik-Tok lampa/Jmary FM 536A/Selfie tripodli halqali chiroq",
                               reply_markup=btn7)
    await message.answer_photo(photo="https://images.uzum.uz/clfj5j56sfhvbd1im7og/original.jpg",
                               caption="Tashqi akkumulyator, 10000 mA/soat, quyosh energiyasida quvvatlanadi",
                               reply_markup=btn8)


@dp.message(F.text == "Admin")
async def admin(message: Message):
    await message.answer("Mutaxassislarimizga sizga qulay ijtimoiy tarmoq chati yoki telefon orqali savol bering:"
                         f"", reply_markup=phbtn)


async def main():
    await dp.start_polling(bot)
    await bot.set_my_commands([
        BotCommand(command="/start", description="Bot ishga qayta tushirish"),
        BotCommand(command="/help", description="Yordam")
    ])
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
