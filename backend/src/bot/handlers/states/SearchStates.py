from aiogram.fsm.state import State, StatesGroup

class SearchStates(StatesGroup):
    user_id = State()
    