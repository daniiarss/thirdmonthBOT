import logging
import asyncio
from config import dp, bot
from database.a_db import DaniiarDatabase
from handlers import setup_routers
from database.sql_queries import CREATE_USER_TABLE_QUERY
import sqlite3

logging.basicConfig(level=logging.INFO)

async def create_users_table():
    db = DaniiarDatabase()
    await db.execute_query(CREATE_USER_TABLE_QUERY, fetch="none")

async def main():
    await create_users_table()
    router = setup_routers()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
