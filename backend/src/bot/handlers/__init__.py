from aiogram import Router
from .register import reg_router
from .search import search_router
from .edit_profile import edit_profile
main_router = Router()
main_router.include_router(reg_router)
main_router.include_router(search_router)
main_router.include_router(edit_profile)
