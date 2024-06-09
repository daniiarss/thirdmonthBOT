from aiogram import Bot, Dispatcher
from decouple import config


TOKEN = config('TOKEN_KEY')
bot = Bot(token=TOKEN)
dp = Dispatcher()