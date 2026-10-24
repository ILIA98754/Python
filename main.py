print("The project chat-Bot is here!")
# 8700870573:AAGPlOfuiacKO3g-VYGYGDGINAHW72bJN04
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Message
from aiogram.filters import Command
import asyncio

bot = Bot(
    token = '8700870573:AAGPlOfuiacKO3g-VYGYGDGINAHW72bJN04',
    default = DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()

# @dp.message()
# async def echo(message: Message):
#     await message.answer(message.text)
@dp.message(Command("start"))
async def echo(message:Message):
    await message.answer("Hi friend!")
    
async def main():
    await dp.start_polling(bot)

if __name__=="__main__":
    asyncio.run(main())
