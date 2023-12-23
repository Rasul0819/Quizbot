
from aiogram import Bot,Dispatcher,types
from aiogram.utils import executor
from keyboard import menu,inline_btns
from data import show_questions

api = '6758328786:AAHDOg93AOLYFUic3hSDais9o4KeO6GqLtY'
bot = Bot(token=api)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(messsage:types.Message):
    await messsage.answer('Asslamu aleykum',reply_markup=menu)

@dp.message_handler(text='Awa')
async def send_questions(message:types.Message):
    await message.answer(f'Al onda baslaymiz\n{show_questions()}')














if __name__ == '__main__':
    executor.start_polling(
        dp,
        skip_updates=True,
        )