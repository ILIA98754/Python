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
from translations import texts, games
import asyncio
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage

bot = Bot(
    token = '8700870573:AAGPlOfuiacKO3g-VYGYGDGINAHW72bJN04',
    default = DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher(storage=MemoryStorage())

user_languages = {}
@dp.message(Command("start"))
async def echo(message: Message):
    await message.answer(
        "Hello! 🖐️ Welcome!\n"
        "What language to speak do you prefer?\n"
        "Enter: RU or EN", reply_markup=keyb)
    
@dp.message(F.text == "🇷🇺 RU")
async def russian(message: Message):
    await message.answer("Здравствуйте!Добро пожаловать в ChatBot для игр Steam! Как мы можем вам помочь?", reply_markup=create_questions)
@dp.message(F.text == "🇬🇧 EN")
async def english(message: Message):
    await message.answer("Hello! Welcome to ChatBot for Steam games! How we can help you?", reply_markup=create_questions)

@dp.message(F.text == "🇷🇺 RU")
async def russian(message: Message):
    user_languages[message.from_user.id] ="ru"
    await message.answer(
        texts["ru"]["добро пожаловать"], #call the ["welcome"]
        reply_markup=create_menu("ru")
    )

@dp.message(F.text == "🇬🇧 EN")
async def english(message: Message):
    user_languages[message.from_user.id] ="en"
    await message.answer(
        texts["en"]["welcome"],
        reply_markup=create_menu("en")
    )

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

class Registration(StatesGroup):
    name = State()
    number = State()
    date = State()

@dp.message(Command("registration"))
async def from_FSM(message:Message, state: FSMContext):
    await message.answer("Hi, enter your name please.")
    await state.set_state(Registration.name)

@dp.message(Registration.name)
async def from_FSM(message:Message, state: FSMContext):
    await message.answer("Ok, now enter your number.")
    await state.update_data(name=message.text)
    await state.set_state(Registration.number)

@dp.message(Registration.number)
async def name_FSM(message:Message, state: FSMContext):
    await message.answer("Thank you, enter please the data, when you want to start")
    await state.update_data(number=message.text)
    await state.set_state(Registration.date)

@dp.message(Registration.date)
async def name_FSM(message:Message, state: FSMContext):
    await state.update_data(date=message.text)
    data = await state.get_data()
    print(data)
    await message.answer("Thank you, you request sent.")
    await state.clear()

async def main():
    await dp.start_polling(bot)

if __name__=="__main__":
    asyncio.run(main())