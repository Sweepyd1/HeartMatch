
#скрипт для создания фейковой наполненной базы ланных
import random

from faker import Faker
from models import Gender, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:sweepy2006@localhost:5432/datebot"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

fake = Faker('ru_RU')
random.seed(42)

def create_fake_users(amount=1000):
    cities = ['Москва', 'Санкт-Петербург', 'Новосибирск', 'Екатеринбург', 'Казань',
              'Нижний Новгород', 'Челябинск', 'Самара', 'Омск', 'Ростов-на-Дону']

    for _ in range(amount):

        user_id = random.randint(1, 1739614869054)

        age = random.randint(18, 45)
        gender = random.choice(list(Gender))


        if random.random() < 0.7:
            preferably_gender = Gender.male if gender == Gender.female else Gender.female
        else:
            preferably_gender = random.choice(list(Gender))

        user = User(
            user_id=user_id,
            username=fake.user_name() + str(user_id)[-4:],
            age=age,
            gender=gender,
            city=random.choice(cities),
            description=fake.sentence(nb_words=10),
            preferably_gender=preferably_gender,
            created_at=fake.date_time_between(start_date='-2y', end_date='now')
        )

        session.add(user)

    try:
        session.commit()
        print(f"Успешно создано {amount} пользователей!")
    except Exception as e:
        session.rollback()
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    create_fake_users()
