from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

search_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="👍"),  # Эмодзи лайка
            KeyboardButton(text="💬"),  # Эмодзи сообщения
            KeyboardButton(text="👎"),  # Эмодзи дизлайка
            # KeyboardButton(text="🔙")  # Эмодзи назад
        ]
    ],
    resize_keyboard=True,
)
