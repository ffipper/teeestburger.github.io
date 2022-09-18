from aiogram.types import Message, ShippingOption, ShippingQuery, LabeledPrice, PreCheckoutQuery
from aiogram.types.message import ContentType

from messages import MESSAGES
from config import PAYMENTS_TOKEN, item_url
from main import dp, bot
from keyboards import keyboard


@dp.message_handler(Command('start'))
async def start(message: Message):
	await bot.send_message(message.chat.id,
		'Еустируем веб апп',
		reply_markup=keyboard)

PRICE = {
	'1': [LabeledPrice(label='Item1', amount=120)],
	'2': [LabeledPrice(label='Item2', amount=120)],
	'3': [LabeledPrice(label='Item3', amount=120)],
	'4': [LabeledPrice(label='Item4', amount=120)],
	'5': [LabeledPrice(label='Item5', amount=120)],
	'6': [LabeledPrice(label='Item6', amount=120)],
}



@dp.message.handler(content_types='web_app_data')
async def buy_process(web_app_massage):
	await bot.send_invoice(message.chat.id,
		title='Title',
		description='Title',
		provider_token=PAYMENTS_TOKEN,
		currency='rub',
		need_email=True,
		need_phone_number=True,
		prices=PRICE[f'{web_app_massage.web_app_data.data}'],
		start_parameter='examle',
		payload='some_invoice')

	@dp.pre_checkout_query_handler(lambda q: True)
	async def checkout_procces(pre_checkout_query: PreCheckoutQuery):
		await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

	@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
	async def successful_payment(message: Message):
		await bot.send_message(message.chat.id,
			'Платеж совершен успешно!')