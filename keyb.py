from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from translations import texts

keyb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🇷🇺 RU"),
            KeyboardButton(text="🇬🇧 EN"),
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True)

def create_menu(language):
    list_game = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Portal 2"),
            KeyboardButton(text="Stardew Valley")
        ],
        [
            KeyboardButton(text="Undertale"),
            KeyboardButton(text="The Talos Principle 2")
        ],
    ],
    resize_keyboard=True
    )
    return list_game

def menu_game(language):
    game_play = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="easter"),
            KeyboardButton(text="full walkthrough")
        ],
             ],
    resize_keyboard=True
    )
    return game_play

def create_questions(language):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Add me",
                    callback_data="add_channel"
            )
        ],
        [
             InlineKeyboardButton(
                text="No I don't",
                callback_data="no_channel"
            )
        ]
    ]
)
    return create_questions
   