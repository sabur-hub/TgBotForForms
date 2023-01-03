from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp


@dp.message_handler(Command('about'))
async def about(message: types.Message):
    text = """it's bot created for p3109 group can take information about lessons time and list user's """
    await message.answer(text=text)
