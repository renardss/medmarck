from dataclasses import dataclass
from data import config
from typing import List
from aiogram.types import LabeledPrice
from aiogram.types.inline_keyboard import InlineKeyboardMarkup


@dataclass
class Item:
    title: str
    description: str
    start_parameter: str
    currency: str
    prices: List[LabeledPrice]
    provider_data: dict = None
    photo_url: str = None
    photo_size: int = None
    photo_width: int = None
    photo_height: int = None
    need_name: bool = False
    need_phone_number: bool = False
    need_email: bool = False
    need_shipping_address: bool = False
    is_flexible: bool = False
    provider_token: str = config.PROVIDER_TOKEN
    reply_markup: InlineKeyboardMarkup = None

    def generate_invoice(self):
        return self.__dict__