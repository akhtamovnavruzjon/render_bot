import asyncio
import logging
from loader import dp, bot
from aiogram import Router
from handlers import setup_hendler
from middleware.throt import ThrottMiddleware


async def main()->None:

    main_router=setup_hendler()
    dp.include_router(main_router)

    dp.message.middleware(ThrottMiddleware(slow_mode_delay=3))

    logging.info("Bot ishga tushdi...")
    await dp.start_polling(bot)

if __name__=="__main__":
   logging.basicConfig(level=logging.INFO)
   asyncio.run(main())

