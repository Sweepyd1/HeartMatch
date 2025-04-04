from database.models import UserWithPhotos
from loader import db
from aiogram.utils.media_group import MediaGroupBuilder
from bot.keyboards.start import main_kb
from aiogram.types import Message

async def get_profile(user_id, message:Message):
    user: UserWithPhotos = await db.get_my_profile(user_id)

    if user is None:
        await message.answer("Пожалуйста, создайте анкету!", reply_markup=main_kb)
     

    caption = f"{user.username}, {user.age}, {user.city}\n{user.description}"

    media_group = MediaGroupBuilder(caption=caption)

    for file in user.photos:
        print(file)
        media_group.add_photo(media=file, type="photo")
    await message.answer_media_group(media=media_group.build())