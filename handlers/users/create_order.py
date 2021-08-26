from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import pre_checkout_query, ShippingQuery
from data.items import KNEE_SUPPORT, KNEE_SUPPORT_MESH, ELBOW_SUPPORT, WRIST_SUPPORT, WHEY_PROTEIN, OMEGA3, VITAMIN_C, \
    MULTISIX, POST_FAST_SHIPPING, POST_REGULAR_SHIPPING
from data.items import CEREBREMED, VIRLAZA
from loader import dp, bot


@dp.message_handler(text="🦵Для ног")
async def show_invoices(message: types.Message):
    await bot.send_invoice(message.from_user.id,
                           **KNEE_SUPPORT.generate_invoice(),
                           payload="123456",
                           )
    await bot.send_invoice(message.from_user.id,
                           **KNEE_SUPPORT_MESH.generate_invoice(),
                           payload="123457",
                           )


@dp.message_handler(text="🖐Для рук")
async def show_invoices(message: types.Message):
    await bot.send_invoice(message.from_user.id,
                           **ELBOW_SUPPORT.generate_invoice(),
                           payload="234567",
                           )
    await bot.send_invoice(message.from_user.id,
                           **WRIST_SUPPORT.generate_invoice(),
                           payload="234568",
                           )


@dp.message_handler(text="💪Спортивное питание")
async def show_invoices(message: types.Message):
    await bot.send_invoice(message.from_user.id,
                           **WHEY_PROTEIN.generate_invoice(),
                           payload="234569",
                           )
    await bot.send_invoice(message.from_user.id,
                           **OMEGA3.generate_invoice(),
                           payload="234579",
                           )


@dp.message_handler(text="🍏Витамины")
async def show_invoices(message: types.Message):
    await bot.send_invoice(message.from_user.id,
                           **MULTISIX.generate_invoice(),
                           payload="234581",
                           )
    await bot.send_invoice(message.from_user.id,
                           **VITAMIN_C.generate_invoice(),
                           payload="234582",
                           )


@dp.message_handler(text="🌿Биодобавки")
async def show_invoices(message: types.Message):
    await bot.send_invoice(message.from_user.id,
                           **CEREBREMED.generate_invoice(),
                           payload="234581",
                           )
    await bot.send_invoice(message.from_user.id,
                           **VIRLAZA.generate_invoice(),
                           payload="234582",
                           )


@dp.shipping_query_handler()
async def choose_shipping(query: types.ShippingQuery):
    if query.shipping_address.country_code == "RU":
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        shipping_options=[
                                            POST_REGULAR_SHIPPING,
                                            POST_FAST_SHIPPING
                                        ],
                                        ok=True)


@dp.pre_checkout_query_handler()
async def process_pre_checkout_query(query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query_id=query.id,
                                        ok=True)
    await bot.send_message(chat_id=query.from_user.id,
                           text="Спасибо за заказ! Мы будем информировать вас об обновлениях доставки!")