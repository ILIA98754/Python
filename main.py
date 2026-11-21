# print("The project chat-Bot is here!")
# 8700870573:AAGPlOfuiacKO3g-VYGYGDGINAHW72bJN04
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Message
from aiogram.filters import Command
from keyb import keyb, question, create_menu, menu_game
from aiogram import F
import asyncio

bot = Bot(
    token = '8700870573:AAGPlOfuiacKO3g-VYGYGDGINAHW72bJN04',
    default = DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()

user_languages = {}
@dp.message(Command("start"))
async def echo(message: Message):
    await message.answer(
        "Hello! 🖐️ Welcome!\n"
        "What language to speak do you prefer?\n"
        "Enter: RU or EN", reply_markup=keyb)
    
@dp.message(F.text == "🇷🇺 RU")
async def russian(message: Message):
    await message.answer("Здравствуйте!?", reply_markup=keyb_menu)
@dp.message(F.text == "🇬🇧 EN")
async def english(message: Message):
    await message.answer("Hello! Welcome to ChatBot for Steam games! How we can help you?", reply_markup=keyb_menu)

@dp.message(F.text == "🇷🇺 RU")
async def russian(message: Message):
    user_languages[message.from_user.id] ="ru"
    await message.answer(
        text["ru"]["welcome"],
        reply_markup=create_menu("ru")
    )

@dp.message(F.text == "🇬🇧 EN")
async def russian(message: Message):
    user_languages[message.from_user.id] ="en"
    await message.answer(
        text["en"]["welcome"],
        reply_markup=create_menu("en")
    )


# @dp.message(F.text == "Портал 2")
# async def english(message: Message):
#     await message.answer(

@dp.message(Command("question"))
async def start(message: Message):
    language = user_languages.get(message.from_user.id, "ru")
    print("USER ID:", message.from_user.id)
    print("LANGUAGE:", language)
    print("TEXT:" text[language]["questionn_contact"]["welcome"])
    await message.answer(
        texts[language]["question_contact"]["welcome"],
         reply_markup=create_question(language)
    )
    
@dp.callback_query(F.data == "add_channel")
async def add_channel(callback: CallbackQuery):
    language = user_languages.get(callback.from_user.id, "ru")
    await callback.answer()
    await callback.message.answer(
        texts[language]["question_contact"]["add_chanel"]
    )

@dp.callback_query(F.data == "no_channel")
async def add_channel(callback: CallbackQuery):
    language = user_languages.get(callback.from_user.id, "ru")
    await callback.answer()
    await callback.message.answer(
        texts[language]["question_contact"]["no_chanel"]
    )

async def main():
    await dp.start_polling(bot)

if __name__=="__main__":
    asyncio.run(main())
