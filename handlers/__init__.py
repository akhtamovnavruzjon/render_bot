from aiogram import Router
from .users import user_r

def setup_hendler()->Router:
    main_router = Router()
    main_router.include_routers(user_r)

    return main_router