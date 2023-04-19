from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.types import InputFile

from loader import dp,bot


@dp.message_handler(commands=['rasm', 'image'])
async def bot_echo(message: types.Message):
    # 1-usul
    # await message.answer_photo(
    #     photo="AgACAgIAAxkBAAIEhGQ2lWvK9SV5ERg9IZJbHPwXjjtMAAIMxzEbTnS5SRVo8c2ZPmzpAQADAgADeQADLwQ",
    #     caption="Zo`r rasm")
    # 2-usul
    # await message.reply_photo(photo="https://stimg.cardekho.com/images/carexteriorimages/930x620/Lamborghini/Urus/4418/Lamborghini-Urus-V8/1621927166506/front-left-side-47.jpg?tr=h-48",caption="urldan olingan rasm")
    # await bot.send_photo(chat_id=5281060766,photo="AgACAgIAAxkBAAIEhGQ2lWvK9SV5ERg9IZJbHPwXjjtMAAIMxzEbTnS5SRVo8c2ZPmzpAQADAgADeQADLwQ")
    # 3-usul
    file=InputFile(path_or_bytesio="documents/file_9.jpg")
    await message.answer_document(document=file)

@dp.message_handler(commands=["media"])
async def mediadef(ms:types.Message):
    media=types.MediaGroup()
    media.attach_photo(InputFile(path_or_bytesio="documents/file_9.jpg"))
    media.attach_photo("AgACAgIAAxkBAAIEhGQ2lWvK9SV5ERg9IZJbHPwXjjtMAAIMxzEbTnS5SRVo8c2ZPmzpAQADAgADeQADLwQ")
    media.attach_photo("https://imageio.forbes.com/specials-images/imageserve/5d35eacaf1176b0008974b54/0x0.jpg?format=jpg&crop=4560,2565,x790,y784,safe&width=1200")
    media.attach_video(InputFile(path_or_bytesio="videos/file_7.mp4"))
    await ms.answer_media_group(media)

@dp.message_handler(content_types=types.ContentType.PHOTO)
async def bot_echo(message: types.Message):
    file_id = message.photo[-1].file_id
    await message.photo[-1].download()
    await message.answer(file_id)


@dp.message_handler(content_types=types.ContentType.VIDEO)
async def bot_echo(message: types.Message):
    file_id = message.video.file_id
    await message.video.download()
    await message.answer(file_id)


@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def bot_echo(message: types.Message):
    file_id = message.document.file_id
    await message.document.download()
    await message.answer(file_id)
