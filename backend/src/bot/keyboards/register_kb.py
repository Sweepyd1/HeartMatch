from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

name_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Имя")],
       ],
    resize_keyboard=True,
)

gender_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Мужчина"),KeyboardButton(text="Женщина") ],
       ],
    resize_keyboard=True,
)

gender_interested_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Мужчины"),KeyboardButton(text="Женщины")  ],
       ],
    resize_keyboard=True,
)

age_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Возраст")],
       ],
    resize_keyboard=True,
)



description_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Пропустить")],
       ],
    resize_keyboard=True,
)

city_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Город")],
       ],
    resize_keyboard=True,
)

# async def get_user_city():
#     city_kb = ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton(text="Город")],
#        ],
#     resize_keyboard=True,
# )


start_seacrh_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Начать искать")],
       ],
    resize_keyboard=True,
)
