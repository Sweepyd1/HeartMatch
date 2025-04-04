from aiogram import F, Router
from aiogram.fsm.context import FSMContext


from aiogram.types import FSInputFile, Message
from aiogram.utils.media_group import MediaGroupBuilder
from database.models import UserWithPhotos
from loader import db, bot

from ..keyboards.search_kb import search_kb
from ..keyboards.find import find_kb
from .states.MessageStates import MessageStates

search_router = Router()


async def search_pair(message: Message):
    user: UserWithPhotos = await db.get_pair(message.from_user.id)

    await message.answer("🔎", reply_markup=search_kb)
    caption = f"{user.username}, {user.age}, {user.city}\n{user.description}"

    default_photo_path = "assets/default_photo.png"

    if not user.photos:
        default_photo = FSInputFile(default_photo_path)
        await message.answer_photo(photo=default_photo, caption=caption)

    else:
        media_group = MediaGroupBuilder(caption=caption)
        for file in user.photos:
            media_group.add_photo(media=file, type="photo")
        await message.answer_media_group(media=media_group.build())
    return user.user_id


@search_router.message(F.text == "Начать искать")
async def get_profile(message: Message, state: FSMContext):
    selected_user_id = await search_pair(message=message)
    await state.update_data(selected_user_id=selected_user_id)

    print(selected_user_id)


@search_router.message(F.text == "Продолжить искать")
async def get_profile_still(message: Message, state: FSMContext):
    selected_user_id = await search_pair(message=message)
    await state.update_data(selected_user_id=selected_user_id)

    print(selected_user_id)


@search_router.message(F.text == "👍")
async def like(message: Message, state: FSMContext):
    data = await state.get_data()
    selected_user_id = data.get("selected_user_id")

    if not selected_user_id:
        await message.answer("Сначала начните поиск!")
        selected_user_id = await search_pair(message=message)
        await state.update_data(selected_user_id=selected_user_id)
        return

    await db.like_user(message.from_user.id, selected_user_id)
    try:
        if message.from_user.username:
            username_link = f'<a href="https://t.me/{message.from_user.username}">@{message.from_user.username}</a>'
        else:
            username_link = message.from_user.url

        await bot.send_message(
            chat_id=selected_user_id,
            text=f"💌 Ваш профиль понравился {username_link} Загляните в анкету!",
            reply_markup=find_kb,
            parse_mode="HTML",
        )
    except Exception as e:
        print(f"Не удалось отправить уведомление: {e}")

    new_selected_id = await search_pair(message=message)
    await state.update_data(selected_user_id=new_selected_id)


@search_router.message(F.text == "👎")
async def dislike(message: Message, state: FSMContext):
    data = await state.get_data()
    selected_user_id = data.get("selected_user_id")
    if not selected_user_id:
        await message.answer("Сначала начните поиск!")
        selected_user_id = await search_pair(message=message)
        await state.update_data(selected_user_id=selected_user_id)
        return
    await db.dislike_user(message.from_user.id, selected_user_id)

    new_selected_id = await search_pair(message=message)
    await state.update_data(selected_user_id=new_selected_id)


@search_router.message(F.text == "💬")
async def send_message(message: Message, state: FSMContext):
    data = await state.get_data()
    selected_user_id = data.get("selected_user_id")

    if not selected_user_id:
        await message.answer("Сначала начните поиск!")
        selected_user_id = await search_pair(message=message)
        await state.update_data(selected_user_id=selected_user_id)
        return

    await state.update_data(temp_selected_user=selected_user_id)

    await state.set_state(MessageStates.waiting_for_message)
    await message.answer("Напишите сообщение для пользователя:")


@search_router.message(MessageStates.waiting_for_message)
async def get_message(message: Message, state: FSMContext):
    data = await state.get_data()
    selected_user_id = data.get("temp_selected_user")

    if not selected_user_id:
        await message.answer("Ошибка: пользователь не найден")
        await state.clear()
        return

    username = message.from_user.username
    username_link = (
        f'<a href="https://t.me/{username}">{username}</a>'
        if username
        else "Пользователь"
    )

    try:
        await bot.send_message(
            chat_id=selected_user_id,
            text=f"📩 Новое сообщение от {username_link}:\n\n{message.text}",
            parse_mode="HTML",
        )
        await message.answer("✅ Сообщение успешно отправлено!")
    except Exception as e:
        await message.answer("❌ Не удалось отправить сообщение")
        print(f"Ошибка отправки: {e}")

    await state.set_state(None)

    new_selected_id = await search_pair(message=message)
    await state.update_data(selected_user_id=new_selected_id)


@search_router.message(F.text == "Посмотреть")
async def check_likes(message: Message, state: FSMContext):
    await message.answer("Ты нажал посмотреть будет логика")


