import sqlite3

from aiogram import Router, types
from aiogram.filters import Command
from aiogram.utils.deep_linking import create_start_link

from config import bot
from database.a_db import DaniiarDatabase
from database import sql_queries
from keyboards.start import start_menu_keyboard

router = Router()


@router.message(Command("start"))
async def start_menu(message: types.Message,
                     db=DaniiarDatabase()):
    command = message.text
    token = command.split()
    print(token)
    if len(token) > 1:
        await process_reference_link(token=token[1], message=message)

    await db.execute_query(
        query=sql_queries.INSERT_USER_QUERY,
        params=(
            None,
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
            None,
            0,
        ),
        fetch="none"
    )
    await bot.send_message(
        chat_id=message.chat.id,
        text=f"Hello {message.from_user.first_name}\n"
             f"Im 42-2-bot, i can register u in profile mode\n"
             f"new features coming soon...",
        reply_markup=await start_menu_keyboard()
    )


async def process_reference_link(token, message, db=DaniiarDatabase()):
    link = await create_start_link(bot=bot, payload=token)

    inviter = await db.execute_query(
        query=sql_queries.SELECT_USER_BY_LINK_QUERY,
        params=(
            link,
        ),
        fetch="one"
    )
    print(inviter)

    if inviter['TELEGRAM_ID'] == message.from_user.id:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="Hi, u can not use ur own link"
        )
        return

    try:
        await db.execute_query(
            query=sql_queries.UPDATE_USER_BALANCE_COLUMN_QUERY,
            params=(
                inviter['TELEGRAM_ID'],
            ),
            fetch="none"
        )
        await db.execute_query(
            query=sql_queries.INSERT_REFERENCE_QUERY,
            params=(
                None,
                inviter['TELEGRAM_ID'],
                message.from_user.id,
            ),
            fetch="none"
        )
    except sqlite3.IntegrityError:
        pass