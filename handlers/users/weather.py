import requests
from aiogram import types
from aiogram.dispatcher.filters import Text
from loader import dp


@dp.message_handler()
async def bot_echo(message: types.Message):
    text=message.text
    api_url=f'https://api.weatherapi.com/v1/current.json?key=9e070c3df80441ffb0b113050232703&q={text}&aqi=no'
    data=requests.get(api_url)
    data=data.json()
    if len(data)>1:
        loc = f"<b>Hudud:</b>{data['location']['name']}/{data['location']['region']}/{data['location']['country']}"
        weather_data = f"<b>Yangilangan vaqt:</b>{data['current']['last_updated']}\n" \
                       f"<b>Harorat:</b>{data['current']['temp_c']}C"
        image = data['current']['condition']['icon']
        text = data['current']['condition']['text']

        javob = f"{loc}\n{weather_data}\n{text}"
        if image == "":
            await message.answer(javob)
        else:
            await message.answer_photo(photo=image[2:], caption=javob)
    else:
          await message.answer("Bunday joy topilmadi!")



