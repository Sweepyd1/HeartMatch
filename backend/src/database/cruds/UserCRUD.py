import random

# from schemas.users import UserWithPhotos
from sqlalchemy import delete, update
from sqlalchemy.future import select

from ..database import DatabaseManager
from ..models import Action, Gender, History, Photos, User, UserWithPhotos


class UserCRUD:

    db_manager:DatabaseManager

    async def create_user(self, user_id:int, username:str, age:int, gender:str, city:str,description:str,preferably_gender:str) -> User:
        async with self.db_manager.get_session() as session:

            new_user = User(
                user_id=user_id,
                username=username,
                age=age,
                gender=gender,
                city=city,
                description=description,
                preferably_gender=preferably_gender,
                )

            session.add(new_user)
            await session.commit()
            await session.refresh(new_user)
            return new_user


    async def add_user_photo(self, photos_id:list[str], user_id:str) -> None:
        async with self.db_manager.get_session() as session:

            for photo_id in  photos_id:
                new_photo = Photos(
                    photo_id=photo_id,
                    user_id=user_id,
                    photo_url=photo_id
                    )
                session.add(new_photo)

            await session.commit()

    async def get_pair(self, user_id: int) -> UserWithPhotos:
        async with self.db_manager.get_session() as session:
            self_user_result = await session.execute(select(User).where(User.user_id == user_id))
            self_user:User = self_user_result.scalars().first()

            if not self_user:
                return None

            get_pair_result = await session.execute(select(User).where(User.is_active == True, User.user_id != user_id))
            get_pair_users = get_pair_result.scalars().all()



            random_user = random.choice(get_pair_users)
            
            photos_query = select(Photos).where(Photos.user_id == random_user.user_id)
            photos_result = await session.execute(photos_query)
            photos = photos_result.scalars().all()


            return UserWithPhotos(random_user, photos)



    async def get_my_profile(self, user_id:int) -> UserWithPhotos:
        async with self.db_manager.get_session() as session:
            user_query = select(User).where(User.user_id == user_id)
            user_result = await session.execute(user_query)
            user:User = user_result.scalars().first()

            if not user:
                return None

            photos_query = select(Photos).where(Photos.user_id == user.user_id)
            photos_result = await session.execute(photos_query)
            photos = photos_result.scalars().all()

            return UserWithPhotos(user, photos)

    async def is_exist_user(self, user_id:int) -> bool:
         async with self.db_manager.get_session() as session:
                query = select(User).where(User.user_id == user_id)
                result = await session.execute(query)
                user = result.scalar_one_or_none()
                return user is not None


    async def check_user_in_temporary_history(self, user_id:int):
        async with self.db_manager.get_session() as session:
            ...


    async def like_user(self,user_id:int, selected_user_id:int):
        async with self.db_manager.get_session() as session:
            new_history = History(
                user_id=user_id,
                action=Action.like,
                selected_user_id=selected_user_id
            )
            session.add(new_history)

            await session.commit()
    

    async def dislike_user(self,user_id:int, selected_user_id:int):
         async with self.db_manager.get_session() as session:
            new_history = History(
                user_id=user_id,
                action=Action.dislike,
                selected_user_id=selected_user_id
            )
            session.add(new_history)

            await session.commit()

    async def get_matches(self,):
        async with self.db_manager.get_session() as session:
            query = await session.execute(select(History))


    async def change_selection(self,):
        ...


######################### update user data##############################


    async def update_name(self, user_id: int, new_name: str):
            async with self.db_manager.get_session() as session:
                await session.execute(
                    update(User)
                    .where(User.user_id == user_id)
                    .values(username=new_name)
                )
                await session.commit()

    async def update_age(self, user_id: int, new_age: int):
        async with self.db_manager.get_session() as session:
                await session.execute(
                    update(User)
                    .where(User.user_id == user_id)
                    .values(age=new_age)
                )
                await session.commit()

    async def update_gender(self, user_id: int, new_gender: str):
        
            if new_gender == "м":
                gender = Gender.male
            elif new_gender == "ж":
                gender = Gender.female
            else:
                raise ValueError("Некорректное значение пола")

            async with self.db_manager.get_session() as session:
                await session.execute(
                    update(User)
                    .where(User.user_id == user_id)
                    .values(gender=gender)
                )
                await session.commit()

    async def update_city(self, user_id: int, new_city: str):
            async with self.db_manager.get_session() as session:
                await session.execute(
                    update(User)
                    .where(User.user_id == user_id)
                    .values(city=new_city)
                )
                await session.commit()

    async def update_description(self, user_id: int, new_description: str):
            async with self.db_manager.get_session() as session:
                await session.execute(
                    update(User)
                    .where(User.user_id == user_id)
                    .values(description=new_description)
                )
                await session.commit()

    async def update_preferably_gender(self, user_id: int, new_preferably_gender: str):
            
            if new_preferably_gender == "м":
                gender = Gender.male
            elif new_preferably_gender == "ж":
                gender = Gender.female
            else:
                raise ValueError("Некорректное значение пола")

            async with self.db_manager.get_session() as session:
                await session.execute(
                    update(User)
                    .where(User.user_id == user_id)
                    .values(preferably_gender=gender)
                )
                await session.commit()

    async def update_photos(self, user_id: int, new_photos: list[str]):
        async with self.db_manager.get_session() as session:

            await session.execute(
                delete(Photos).where(Photos.user_id == user_id))
            
            
            for file_id in new_photos:
                new_photo = Photos(
                    photo_id=file_id,  
                    user_id=user_id,
                    photo_url=file_id
                )
                session.add(new_photo)
            
            await session.commit()

    async def deactivate_account(self,user_id: int):
        async with self.db_manager.get_session() as session:
            await session.execute(
                    update(User)
                    .where(User.user_id == user_id)
                    .values(is_active=False)
                )
            await session.commit()

    async def activate_account(self,user_id: int):
        async with self.db_manager.get_session() as session:
            await session.execute(
                    update(User)
                    .where(User.user_id == user_id)
                    .values(is_active=True)
                )
            await session.commit()
         
