from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData



web_app = WebAppInfo (url="https://ffipper.github.io/teeestburger.github.io/")

keyboard = ReplyKeyboardMarkup (

keyboard=[

 [KeyboardButton(text="Site", web_app=web_app)]

],
resize_keyboard=True

)

cb= CallbackData('btn', 'action')
key = InlineKeyboardMarkup(
	inline_keyboard=[[InlineKeyboardButton('Pay', CallbackData='btn:buy')]]
	)