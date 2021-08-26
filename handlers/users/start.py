import asyncpg
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.menu import menu, rehabilitation_sub, it_health_sub, vitamins
import time
from loader import dp, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    try:
        user = await db.add_user(telegram_id=message.from_user.id,
                                 full_name=message.from_user.full_name,
                                 username=message.from_user.username)
    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(telegram_id=message.from_user.id)

    count = await db.count_users()

    # Забираем как список или как словарь
    user_data = list(user)
    user_data_dict = dict(user)

    # Забираем напрямую как из списка или словаря
    username = user.get("username")
    full_name = user[2]
    await message.answer(
        "\n".join([
            f'Привет, {message.from_user.full_name}! \nСегодня ты можешь получить скидку более 75% на многие популярные товары для здоровья, если сделаешь заказ здесь в Телеграме через меня🤩✅\nИспользуй возможность СЕГОДНЯ🔥🔥🔥',
        ])
    )
    #await message.answer(f"Привет, {message.from_user.full_name}!\nСегодня ты можешь получить скидку более 75% на многие популярные товары для здоровья, если сделаешь заказ здесь в Телеграме через меня🤩✅\nИспользуй возможность СЕГОДНЯ🔥🔥🔥")
    time.sleep(7)
    await message.answer(f"Пожалуйста, выбери одну из следующих категорий👇",
    reply_markup=menu)


@dp.message_handler(text="🏃‍♂️Реабилитация")
async def get_rehabilitation(message: types.Message):
    await message.answer("Хорошо👍Теперь выбери одно из следующих👇",
    reply_markup=rehabilitation_sub)


@dp.message_handler(text="📱IT Здоровье")
async def get_rehabilitation(message: types.Message):
    await message.answer("Хорошо👍Теперь выбери одно из следующих👇",
    reply_markup=it_health_sub)

@dp.message_handler(text="💪Витамины и минералы")
async def get_rehabilitation(message: types.Message):
    await message.answer("Хорошо👍Теперь выбери одно из следующих👇",
    reply_markup=vitamins)
# import asyncpg
# from aiogram import types
# from aiogram.dispatcher.filters.builtin import CommandStart
#
# from loader import dp, db


# @dp.message_handler(CommandStart())
# async def bot_start(message: types.Message):
#     try:
#         user = await db.add_user(telegram_id=message.from_user.id,
#                                  full_name=message.from_user.full_name,
#                                  username=message.from_user.username)
#     except asyncpg.exceptions.UniqueViolationError:
#         user = await db.select_user(telegram_id=message.from_user.id)
#
#     count = await db.count_users()
#
#     # Забираем как список или как словарь
#     user_data = list(user)
#     user_data_dict = dict(user)
#
#     # Забираем напрямую как из списка или словаря
#     username = user.get("username")
#     full_name = user[2]
#
#     await message.answer(
#         "\n".join(
#             [
#                 f'Привет, {message.from_user.full_name}!',
#                 f'Ты был занесен в базу',
#                 f'В базе <b>{count}</b> пользователей',
#                 "",
#                 f"<code>User: {username} - {full_name}",
#                 f"{user_data=}",
#                 f"{user_data_dict=}</code>"
#             ]))
