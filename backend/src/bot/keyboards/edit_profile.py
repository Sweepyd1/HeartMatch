from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

edit_profile = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Имя пользователя 👤"), 
            KeyboardButton(text="Возраст 🎂")
        ],
        [
            KeyboardButton(text="Пол ♀♂"), 
            KeyboardButton(text="Город 🌆")
        ],
        [
            KeyboardButton(text="О себе 📝"), 
            KeyboardButton(text="Ищу пол 👫")
        ],
        [
           
             KeyboardButton(text="Заморозить аккаунт"),
             KeyboardButton(text="Активировать аккаунт")
             

        ],
         [
            KeyboardButton(text="Фото 📸"), 
            KeyboardButton(text="Начать искать")
         ],

    ],
    resize_keyboard=True,
)
   