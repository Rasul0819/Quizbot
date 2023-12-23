from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardMarkup,KeyboardButton


yes = KeyboardButton(text='Awa',)
no = KeyboardButton(text='Yaq')

first = InlineKeyboardButton(text='a',callback_data='a')
second = InlineKeyboardButton(text='b',callback_data='b')
third = InlineKeyboardButton(text='c',callback_data='c')
fourth = InlineKeyboardButton(text='d',callback_data='d')


menu = ReplyKeyboardMarkup().add(yes,no)
inline_btns = InlineKeyboardMarkup().add(first,second,third,fourth)