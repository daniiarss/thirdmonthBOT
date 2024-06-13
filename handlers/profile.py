from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import CallbackQuery, FSInputFile

from config import bot
from database.a_db import DaniiarDatabase
from database import sql_queries

router = Router()



@router.callback_query(lambda call: call.data == 'my_profile')
async def my_profiles_call(call: CallbackQuery,
                             db = DaniiarDatabase()):
    user = await db.execute_query(
        query=sql_queries.SELECT_PROFILE_QUERY,
        params=(
            call.from_user.id,
        ),
        fetch="all"
    )
    print(user)
    photo = FSInputFile(user[0]["PHOTO"])
    await bot.send_photo(
        chat_id=call.from_user.id,
        photo=photo,
        caption=f"Name: {user[0]['NICKNAME']}\n"
                f"Bio: {user[0]['BIO']}\n"
    )