from aiogram import types
from aiogram.dispatcher.filters import Text
import wikipedia
from loader import dp


@dp.message_handler()
async def bot_echo(message: types.Message):
    try:
        text=message.text
        wikipedia.set_lang('en')
        javob=wikipedia.summary(text,sentences=1)
        # javob=wikipedia.search(text)
        if javob!="":
            await message.answer(javob)
    except Exception as e:
        await message.answer("Bunday ma`lumot topilmadi!")


