from aiogram.filters import Filter
from aiogram import types
from data.config import ADMINS

#ADMINlar tekshiruvi
class IsADMINFilter(Filter):
    async def __call__(self,message:types.Message)->bool:
        return str(message.from_user.id) in ADMINS
