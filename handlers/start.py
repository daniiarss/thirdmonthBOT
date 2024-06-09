from aiogram import Router, types
from aiogram.filters import Command
from config import bot
from models.users import add_user, user_exists

router = Router()

@router.message(Command("start"))
async def start_menu(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name

    if not user_exists(user_id):
        add_user(user_id, username, first_name, last_name)

    await bot.send_message(
        chat_id=message.chat.id,
        text="Добро пожаловать! Вы успешно зарегистрированы."
    )
