from aiogram.fsm.state import State, StatesGroup

class RegistrationStates(StatesGroup):
    waiting_for_name = State()
    waiting_for_age = State()
    waiting_for_city = State()
    waiting_for_gender = State()
    waiting_for_preferably_gender = State()
    waiting_for_description = State()
    waiting_for_photos = State()
