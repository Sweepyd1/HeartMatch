import asyncio
import logging
import sys

from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.utils.media_group import MediaGroupBuilder
from bot.handlers import main_router
from bot.keyboards.register_kb import start_seacrh_kb
from bot.keyboards.start import main_kb
from bot.keyboards.edit_profile import edit_profile
from config import TOKEN
from database.models import UserWithPhotos
from fastapi import FastAPI, Request
from loader import bot, db, dp
from aiogram.types import KeyboardButton, WebAppInfo, ReplyKeyboardMarkup

from utils.utils import get_profile
dp.include_router(main_router)



   
@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    is_exist = await db.is_exist_user(message.from_user.id)

    if not is_exist:
        await message.answer(
            f"Нажмите создать анкету",
            reply_markup=main_kb,
        )
        return

    await message.answer(
        f"Давайте вам найдем кого-нибудь!", reply_markup=start_seacrh_kb
    )
    await message.answer(
        "Откройте веб-приложение:",
        reply_markup=keyboard
    )


@dp.message(Command("myprofile"))
async def get_my_profile(message: Message):
    await get_profile(message.from_user.id, message)
    



@dp.message(Command("profilesettings"))
async def profile_settings(message: Message):
    user: UserWithPhotos = await db.get_my_profile(message.from_user.id)

    if user is None:
        await message.answer("Пожалуйста, создайте анкету!", reply_markup=main_kb)
        return
    await message.answer(
        "⚙️ Настройки профиля:\n"
        "Выберите параметр который хотите изменить:",
        reply_markup=edit_profile
    )
 

@dp.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        "👋 Привет! Я бот для знакомств, который поможет:\n\n"
        "🔍 Найти интересных людей рядом\n"
        "💌 Анонимно проявлять симпатию\n"
        "📩 Обмениваться сообщениями при взаимной лайке\n\n"
        "- /start - начать поиск\n"
        "- /myprofile - ваша анкета\n"
        "- /stop - приостановить поиск\n"
        "🛠 Если что-то сломалось или есть предложения - пишите @Sweepyd1\n"
        "Мы всегда рады помочь и улучшить ваш опыт знакомств! ❤️"
    )


web_app_btn = KeyboardButton(
    text="Открыть приложение 🚀",
    web_app=WebAppInfo(url="https://f4743c014f058f7d2151a457ef5387f9.serveo.net/#/profile")
)


keyboard = ReplyKeyboardMarkup(
    keyboard=[[web_app_btn]],
    resize_keyboard=True
)




async def main() -> None:
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    # await start_command()
    await dp.start_polling(bot)
    


if __name__ == "__main__":
    import uvloop

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    asyncio.run(main())
