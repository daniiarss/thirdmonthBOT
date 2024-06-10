from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from decouple import config

storage = MemoryStorage()
TOKEN = config('TOKEN_KEY')
bot = Bot(token=TOKEN)
dp = Dispatcher(storage=storage)
DATABASE_URL = config('DATABASE_URL', default="sqlite:///profiles.db")
MEDIA_PATH = config('MEDIA')
