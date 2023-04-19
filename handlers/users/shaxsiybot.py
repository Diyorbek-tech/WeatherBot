from aiogram import types
from aiogram.dispatcher.filters import Text
from loader import dp,bot
from data.config import ADMINS
from filters.admins import AdminFilter


@dp.message_handler(AdminFilter())
async def bot_echo(message: types.Message):
    user=message.forward_from_chat.id
    print("dfgdfg",user)
    await bot.send_message(chat_id=user,text=message.text)
@dp.message_handler()
async def bot_echo(message: types.Message):
    id=message.from_user.id
    await bot.forward_message(chat_id=ADMINS[0],from_chat_id=id,message_id=message.message_id)


