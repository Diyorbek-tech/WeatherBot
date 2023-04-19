import requests
from aiogram import types
from aiogram.dispatcher.filters import Text
from loader import dp
import json


@dp.message_handler()
async def bot_echo(message: types.Message):
    text = message.text
    data = requests.get(url=f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/{text}.json")
    javob = data.json()
    await message.answer(javob[text]['uzs'])