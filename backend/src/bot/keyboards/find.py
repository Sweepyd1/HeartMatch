from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

find_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            # KeyboardButton(text="Посмотреть анкету"),  
            KeyboardButton(text="Продолжить искать"),  

        ]
    ],
    resize_keyboard=True,
)
