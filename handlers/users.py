from aiogram import Router,types
from aiogram.filters import Command
from filters.filters import IsADMINFilter

user_r=Router()


#ADMINLAR uchun
@user_r.message(Command("start"),IsADMINFilter())
async def start(message:types.Message):
    await message.reply(f"Salom janob")

@user_r.message(Command("start"))
async def start(message:types.Message):
    await message.reply(f"Salom {message.from_user.full_name}")

@user_r.message()
async def exo(message:types.Message):
    await message.answer(message.text)
