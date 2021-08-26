from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import callback_data

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🏃‍♂️Реабилитация"),
            KeyboardButton(text="📱IT Здоровье")
        ],
        [
            KeyboardButton(text="💪Витамины и минералы"),
            KeyboardButton(text="🌿Биодобавки"),
        ]
    ],
    resize_keyboard=True
)

rehabilitation_sub = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🦵Для ног"),
        ],
        [
            KeyboardButton(text="🖐Для рук"),
        ]
    ],
    resize_keyboard=True
)

it_health_sub = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🌡Бесконтактные термометры"),
        ],
        [
            KeyboardButton(text="🩸Измерители давления"),
        ],
        [
            KeyboardButton(text="🤳Умные измерители здоровья")
        ]
    ],
    resize_keyboard=True
)

vitamins = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="💪Спортивное питание"),
        ],
        [
            KeyboardButton(text="🍏Витамины"),
        ],
        [
            KeyboardButton(text="🌿Биодобавки")
        ]
    ],
    resize_keyboard=True
)