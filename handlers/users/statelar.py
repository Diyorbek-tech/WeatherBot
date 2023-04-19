from aiogram import types
from aiogram.dispatcher.filters import Text
from loader import dp
from aiogram.dispatcher import FSMContext
from states.Royxatdan_otish import Royhatdan_otish
yosh_re=r'^([1-9][0-9])$'



@dp.message_handler(commands=['signup'])
async def bot_echo(message: types.Message):
    await Royhatdan_otish.ism.set()
    await message.answer("ismingizni kiriting..")

@dp.message_handler(state=Royhatdan_otish,commands=['start','help'])
async def bot_echo(message: types.Message,state:FSMContext):
    await message.answer("xatolik")


@dp.message_handler(state=Royhatdan_otish.ism)
async def bot_echo(message: types.Message,state:FSMContext):

    ism=message.text
    await state.update_data({"ism":ism})
    current_state=state.get_state()
    print(current_state)

    await Royhatdan_otish.yosh.set()
    await message.answer("yoshingizni kiriting..")

@dp.message_handler(state=Royhatdan_otish.yosh,regexp=yosh_re)
async def bot_echo(message: types.Message,state:FSMContext):

    yosh=message.text
    await state.update_data({"yosh":yosh})
    current_state=state.get_state()
    print(current_state)
    await Royhatdan_otish.tel.set()
    await message.answer("telingizni kiriting..")

@dp.message_handler(state=Royhatdan_otish.yosh)
async def bot_echo(message: types.Message,state:FSMContext):
    await message.answer("Yoshingizni to`g`ri kiriting!!")

@dp.message_handler(state=Royhatdan_otish.tel)
async def bot_echo(message: types.Message,state:FSMContext):

    tel=message.text
    await state.update_data({"tel":tel})
    current_state=state.get_state()
    print(current_state)
    data=await state.get_data()

    await state.finish()
    await message.answer(f"{data['ism']}\n{data['yosh']}\n{data['tel']}")


