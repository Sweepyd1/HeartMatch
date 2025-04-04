from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from config import DATABASE_URL, TOKEN
from database.Crud import Crud
from database.database import DatabaseManager
from fastapi import FastAPI
from server.api import router
bot = Bot(token=TOKEN)
app = FastAPI()
app.include_router(router)

storage = MemoryStorage()
dp = Dispatcher(storage=storage)

db = Crud(DatabaseManager(DATABASE_URL))

# observer = Observer(db, bot)
