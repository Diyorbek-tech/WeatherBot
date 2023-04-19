import requests
from aiogram import types
from aiogram.dispatcher.filters import Text
from loader import dp


@dp.message_handler()
async def bot_echo(message: types.Message):
    text=message.text
    api_url='https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/uzb-muhammadsodikmu.min.json'
    data=requests.get(api_url)
    data=data.json()
    javob=""

    for i in data['quran']:
       if  str(i['chapter'])==str(text):
           javob+=f"<b>{i['verse']}</b>){i['text']}\n"
    await message.answer(javob)