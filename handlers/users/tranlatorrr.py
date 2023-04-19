import requests

from aiogram import types
from aiogram.dispatcher.filters import Text
from loader import dp
from translate import Translator

@dp.message_handler()
async def bot_echo(message: types.Message):
    text=message.text
    tr=Translator(to_lang='uz',from_lang="en")
    javob=tr.translate(text)
    await message.answer(javob)