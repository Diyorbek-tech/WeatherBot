
from aiogram import types
from aiogram.dispatcher.filters import Text
from loader import dp
file_id='AgACAgIAAxkBAAIBGmQkJjUKraWxuK7xVtPUHMSejMLKAAKexjEbgWQhScZfYoyTxSwYAQADAgADeQADLwQ'

@dp.message_handler(commands=['photo','image'])
async def bot_echo(message: types.Message):
    await message.answer_photo(photo=f'{file_id}')


@dp.message_handler(content_types='document')
async def bot_echo(message: types.Message):
    await message.document.download()
    await message.answer("siz document yubordingiz")

@dp.message_handler(content_types='text')
async def bot_echo(message: types.Message):
    await message.answer("siz text yubordingiz")

@dp.message_handler(content_types='photo')
async def bot_echo(message: types.Message):
    fileid= message.photo[-1].file_id
    await message.answer(text=f"{fileid}")
    await message.answer_photo(photo=f'{fileid}')




@dp.message_handler(content_types='video')
async def bot_echo(message: types.Message):
    file_id=message.video.file_id
    await message.answer("siz video yubordingiz"+file_id)
    await message.answer_video(video=f'{file_id}',caption="zor video")
