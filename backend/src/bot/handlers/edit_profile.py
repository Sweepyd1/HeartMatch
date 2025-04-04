from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.utils.media_group import MediaGroupBuilder
from loader import db

from ..keyboards.register_kb import age_kb, city_kb, description_kb, gender_interested_kb, gender_kb, name_kb, start_seacrh_kb
from ..utils.AlbumMiddleware import AlbumMiddleware
from .states.EditProfile import EditProfile
from utils.utils import get_profile
edit_profile = Router()

edit_profile.message.middleware(AlbumMiddleware())

@edit_profile.message(F.text == "Имя пользователя 👤")
async def edit_name_handler(message: Message, state: FSMContext):
    await message.answer("Введите новое имя пользователя:")
    await state.set_state(EditProfile.waiting_for_name)

@edit_profile.message(F.text == "Возраст 🎂")
async def edit_age_handler(message: Message, state: FSMContext):
    await message.answer("Введите ваш возраст (только цифры):")
    await state.set_state(EditProfile.waiting_for_age)

@edit_profile.message(F.text == "Пол ♀♂")
async def edit_gender_handler(message: Message, state: FSMContext):
    await message.answer("Укажите ваш пол (М/Ж):")
    await state.set_state(EditProfile.waiting_for_gender)

@edit_profile.message(F.text == "Город 🌆")
async def edit_city_handler(message: Message, state: FSMContext):
    await message.answer("Введите ваш город:")
    await state.set_state(EditProfile.waiting_for_city)

@edit_profile.message(F.text == "О себе 📝")
async def edit_description_handler(message: Message, state: FSMContext):
    await message.answer("Напишите о себе():")
    await message.answer("или напишите 'ничего', чтобы оставить описание пустым")
    await state.set_state(EditProfile.waiting_for_description)

@edit_profile.message(F.text == "Фото 📸")
async def edit_photo_handler(message: Message, state: FSMContext):
    await message.answer("Отправьте новое фото:")
    await state.set_state(EditProfile.waiting_for_photo)

@edit_profile.message(F.text == "Ищу пол 👫")
async def edit_preferably_gender_handler(message: Message, state: FSMContext):
    await message.answer("Кого вы ищете? (М/Ж):")
    await state.set_state(EditProfile.waiting_for_preferably_gender)


@edit_profile.message(F.text == "Заморозить аккаунт")
async def deactivate_account(message: Message):
   await db.deactivate_account(message.from_user.id)
   await message.answer("Вы заморозили вашу анкету")

@edit_profile.message(F.text == "Активировать аккаунт")
async def deactivate_account(message: Message):
   await db.activate_account(message.from_user.id)
   await message.answer("Ваш аккаунт активирован")

@edit_profile.message(EditProfile.waiting_for_name)
async def process_name(message: Message, state: FSMContext):
    if len(message.text) > 50:
        return await message.answer("Имя слишком длинное (макс. 50 символов)")
    await message.answer("Имя успешно обновлено!")
    await db.update_name(message.from_user.id, message.text)
    await state.clear()

@edit_profile.message(EditProfile.waiting_for_age)
async def process_age(message: Message, state: FSMContext):
    if not message.text.isdigit():
        return await message.answer("Возраст должен быть числом!")
    age = int(message.text)
    if not 12 <= age <= 100:
        return await message.answer("Введите реальный возраст (12-100)")
    await message.answer("Возраст успешно обновлен!")
    await db.update_age(message.from_user.id, age)
    await state.clear()

@edit_profile.message(EditProfile.waiting_for_gender)
async def process_gender(message: Message, state: FSMContext):
    gender = message.text.lower()
    if gender not in ['м', 'ж']:
        return await message.answer("Используйте только М или Ж")
    await message.answer("Пол успешно обновлен!")
    await db.update_gender(message.from_user.id, gender)
    await state.clear()

@edit_profile.message(EditProfile.waiting_for_city)
async def process_city(message: Message, state: FSMContext):
    if len(message.text) > 50:
        return await message.answer("Название города слишком длинное")
    await message.answer("Город успешно обновлен!")
    await db.update_city(message.from_user.id, message.text)
    await state.clear()

@edit_profile.message(EditProfile.waiting_for_description)
async def process_description(message: Message, state: FSMContext):
    if len(message.text) > 500:
        return await message.answer("Описание слишком длинное (макс. 500 символов)")
    description = message.text
    if message.text == "ничего":
        description = ""
    await message.answer("Описание успешно обновлено!")
    await db.update_description(message.from_user.id, description)
    await state.clear()

@edit_profile.message(EditProfile.waiting_for_preferably_gender)
async def process_preferably_gender(message: Message, state: FSMContext):
    gender = message.text.lower()
    if gender not in ['м', 'ж']:
        return await message.answer("Используйте М или Ж ")
    await message.answer("Предпочитаемый пол успешно обновлен!")
    await db.update_preferably_gender(message.from_user.id, gender)
    await state.clear()



@edit_profile.message(EditProfile.waiting_for_photo)
async def process_photo(message: Message, state: FSMContext, album: list = None):
    albums_photo = []
   

    if album:
        for obj in album:
            if obj.photo:
                file_id = obj.photo[-1].file_id
                albums_photo.append(file_id)
       

    else:
        albums_photo.append(message.photo[-1].file_id)

    await db.update_photos(message.from_user.id, albums_photo)
    await get_profile(message.from_user.id, message)

