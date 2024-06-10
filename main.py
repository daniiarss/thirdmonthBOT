import asyncio

from config import dp, bot
from database.a_db import DaniiarDatabase
from handlers import setup_routers


async def main():
    db = DaniiarDatabase()
    await db.create_tables()
    router = setup_routers()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())