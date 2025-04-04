from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, ContentType
from aiogram.utils.media_group import MediaGroupBuilder
from loader import db

from ..keyboards.register_kb import age_kb, city_kb, description_kb, gender_interested_kb, gender_kb, name_kb, start_seacrh_kb
from ..utils.AlbumMiddleware import AlbumMiddleware
from .states.RegistrationStates import RegistrationStates

reg_router = Router()

reg_router.message.middleware(AlbumMiddleware())

@reg_router.message(F.text == "Создать анкету")
async def registration_handler(message: Message, state: FSMContext):
    await message.answer("Введите ваше имя", reply_markup=ReplyKeyboardRemove())
    await state.set_state(RegistrationStates.waiting_for_name)

@reg_router.message(RegistrationStates.waiting_for_name)
async def process_name(message: Message, state: FSMContext):
    if message.content_type != ContentType.TEXT:
        await message.answer("Пожалуйста, введите текст")
        return
        
    await state.update_data(name=message.text)
    await message.answer("Введите ваш возраст")
    await state.set_state(RegistrationStates.waiting_for_age)

@reg_router.message(RegistrationStates.waiting_for_age)
async def process_age(message: Message, state: FSMContext):
    if message.content_type != ContentType.TEXT:
        await message.answer("Пожалуйста, введите возраст числом")
        return
    
    if not message.text.isdigit() or not 12 <= int(message.text) <= 85:
        await message.answer("Пожалуйста, введите корректный возраст (12-85)")
        return
        
    await state.update_data(age=message.text)
    await message.answer("Введите ваш город")
    await state.set_state(RegistrationStates.waiting_for_city)

@reg_router.message(RegistrationStates.waiting_for_city)
async def process_city(message: Message, state: FSMContext):
    if message.content_type != ContentType.TEXT:
        await message.answer("Пожалуйста, введите текст")
        return
        
    await state.update_data(city=message.text)
    await message.answer("Выберите пол", reply_markup=gender_kb)
    await state.set_state(RegistrationStates.waiting_for_gender)

@reg_router.message(RegistrationStates.waiting_for_gender)
async def process_gender(message: Message, state: FSMContext):
    if message.content_type != ContentType.TEXT or message.text not in ["Мужчина", "Женщина"]:
        await message.answer("Пожалуйста, выберите пол из кнопок ниже")
        return
        
    await state.update_data(gender=message.text)
    await message.answer("Кто вам интересен?", reply_markup=gender_interested_kb)
    await state.set_state(RegistrationStates.waiting_for_preferably_gender)

@reg_router.message(RegistrationStates.waiting_for_preferably_gender)
async def process_preferably_gender(message: Message, state: FSMContext):
    if message.content_type != ContentType.TEXT or message.text not in ["Мужчины", "Женщины"]:
        await message.answer("Пожалуйста, выберите вариант из кнопок ниже")
        return
        
    await state.update_data(preferably_gender=message.text)
    await message.answer("Напишите описание", reply_markup=description_kb)
    await state.set_state(RegistrationStates.waiting_for_description)

@reg_router.message(RegistrationStates.waiting_for_description)
async def process_description(message: Message, state: FSMContext):
    if message.content_type != ContentType.TEXT:
        await message.answer("Пожалуйста, введите текст")
        return
        
    await state.update_data(description=message.text)
    await message.answer("Отправьте ваши фотографии", reply_markup=ReplyKeyboardRemove())
    await state.set_state(RegistrationStates.waiting_for_photos)

@reg_router.message(RegistrationStates.waiting_for_photos)
async def process_photos(message: Message, state: FSMContext, album: list = None):
    user_data = await state.get_data()
    name = user_data.get("name")
    age = user_data.get("age")
    city = user_data.get("city")
    gender = user_data.get("gender")
    preferably_gender = user_data.get("preferably_gender")
    description = user_data.get("description")

    if description == "Пропустить":
        description = " "

    if gender == "Мужчина":
        gender = "male"
    else:
        gender = "female"

    if preferably_gender == "Мужчины":
        preferably_gender = "male"
    else:
        preferably_gender = "female"

    caption = (
            f"{name}, {age}, {city}\n"
            f"{description}"
        )
    media_group = MediaGroupBuilder(caption=caption)

    albums_photo = []
   
    await message.answer("Твоя анкета выглядит так!", reply_markup=start_seacrh_kb)
    if album:
        for obj in album:
            if obj.photo:
                file_id = obj.photo[-1].file_id
                albums_photo.append(file_id)
                media_group.add_photo(media=file_id, type="photo")
        await message.answer_media_group(media=media_group.build())

    else:
        await message.answer_photo(message.photo[-1].file_id, caption=caption)
        albums_photo.append(message.photo[-1].file_id)
    
    if not albums_photo:
        await message.answer("отправьте хотя бы одну фотографию")

    await db.create_user(user_id=message.from_user.id, username=name, age=int(age), gender=gender, city=city,description=description, preferably_gender=preferably_gender)
    await db.add_user_photo(albums_photo, message.from_user.id)

    await state.clear()
