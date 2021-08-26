from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("contact", "Связаться с нами"),
            types.BotCommand("delivery", "Информация о доставке"),
            types.BotCommand("about", "О нас"),
            types.BotCommand("support", "Поддержка")
        ]
    )
