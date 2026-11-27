# print("The project chat-Bot is here!")
# 8700870573:AAGPlOfuiacKO3g-VYGYGDGINAHW72bJN04
from queue import Full

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Message
from aiogram.filters import Command
from keyb import keyb, create_questions, create_menu, menu_game
from aiogram import F
from aiogram.types import CallbackQuery
from translations import texts
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
    await message.answer("Здравствуйте!Добро пожаловать в ChatBot для игр Steam! Как мы можем вам помочь?", reply_markup=keyb)
@dp.message(F.text == "🇬🇧 EN")
async def english(message: Message):
    await message.answer("Hello! Welcome to ChatBot for Steam games! How we can help you?", reply_markup=keyb)

@dp.message(F.text == "🇷🇺 RU")
async def russian(message: Message):
    user_languages[message.from_user.id] ="ru"
    await message.answer(
        texts["ru"]["добро пожаловать"],
        reply_markup=create_menu("ru")
    )

@dp.message(F.text == "🇬🇧 EN")
async def english(message: Message):
    user_languages[message.from_user.id] ="en"
    await message.answer(
        texts["en"]["welcome"],
        reply_markup=create_menu("en")
    )

games = {
    "portal": {
        "en": {
            "name": "Portal 2",
            "walkthrough": "https://www.youtube.com/results?search_query=Portal+2+full+walkthrough",
            "easters": "https://www.youtube.com/results?search_query=Portal+2+all+easter+eggs+secrets"
        },
        "ru": {
            "name": "Портал 2",
            "walkthrough": "https://www.youtube.com/results?search_query=Portal+2+полное+прохождение+на+русском",
            "easters": "https://www.youtube.com/results?search_query=Portal+2+все+пасхалки+секреты+на+русском"
        }
    },

    "stardew": {
        "en": {
            "name": "Stardew Valley",
            "walkthrough": "https://www.youtube.com/results?search_query=Stardew+Valley+full+walkthrough",
            "easters": "https://www.youtube.com/watch?v=q9LLNLuGJ-Q"
        },
        "ru": {
            "name": "Долина Стардью",
            "walkthrough": "https://www.youtube.com/results?search_query=Stardew+Valley+полное+прохождение+на+русском",
            "easters": "https://www.youtube.com/results?search_query=Stardew+Valley+все+секреты+пасхалки+на+русском"
        }
    },

    "undertale": {
        "en": {
            "name": "Undertale",
            "walkthrough": "https://www.youtube.com/results?search_query=Undertale+full+walkthrough",
            "easters": "https://www.youtube.com/results?search_query=Undertale+all+secrets+easter+eggs"
        },
        "ru": {
            "name": "Андертейл",
            "walkthrough": "https://www.youtube.com/results?search_query=Undertale+полное+прохождение+на+русском",
            "easters": "https://www.youtube.com/results?search_query=Undertale+все+секреты+пасхалки+на+русском"
        }
    },

    "talos": {
        "en": {
            "name": "The Talos Principle 2",
            "walkthrough": "https://www.youtube.com/results?search_query=The+Talos+Principle+2+full+walkthrough",
            "easters": "https://www.youtube.com/watch?v=HvveuyoJeRQ"
        },
        "ru": {
            "name": "Принцип Талоса 2",
            "walkthrough": "https://www.youtube.com/watch?v=iZwucInusPc",
            "easters": "https://www.youtube.com/results?search_query=The+Talos+Principle+2+все+секреты+на+русском"
        }
    }
}


@dp.message(Command("question"))
async def start(message: Message):
    language = user_languages.get(message.from_user.id, "ru")
    print("USER ID:", message.from_user.id)
    print("LANGUAGE:", language)
    print("TEXTS:", texts[language]["question_contact"]["welcome"])
    await message.answer(
        texts[language]["question_contact"]["welcome"],
         reply_markup=create_questions(language)
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
