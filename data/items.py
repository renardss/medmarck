from aiogram import types
from aiogram.types import LabeledPrice, ShippingOption
from utils.misc.item import Item

KNEE_SUPPORT = Item(
    title="Bamboo Yarn Adjustable knee Support",
    description="Highly breathable knee support of bamboo yarn for rehabilitation, intense training, or daily support",
    currency="RUB",
    prices=[
     LabeledPrice(
         label="Bamboo Yarn Adjustable knee Support",
         amount=1988_06
     )
    ],
    start_parameter="create_invoice_knee_support",
    photo_url="https://medmarck.com/wp-content/uploads/2021/07/1453203797.jpg",
    photo_size=600,
    need_shipping_address=True,
    need_email=True,
    need_phone_number=True,
    is_flexible=True
)

KNEE_SUPPORT_MESH = Item(
    title="High Breathable Mesh Knee Support",
    description="Highly breathable mesh knee support for rehabilitation, intense training, or daily support",
    currency="RUB",
    prices=[
     LabeledPrice(
         label="High Breathable Mesh Knee Support",
         amount=2356_09
     )
    ],
    start_parameter="create_invoice_knee_support_mesh",
    photo_url="https://medmarck.com/wp-content/uploads/2021/07/1453203574.jpg",
    photo_size=600,
    need_shipping_address=True,
    need_email=True,
    need_phone_number=True,
    is_flexible=True
)

ELBOW_SUPPORT = Item(
    title="Многофункциональная повязка",
    description="Регулируемый многофункциональный ремешок для поддержки локтя, голени и лодыжки. Лучше всего подходит для людей на реабилитации, после травм или спортсменов, которые занимаются интенсивными тренировками.",
    currency="RUB",
    prices=[
     LabeledPrice(
         label="Elbow_and_Ankle",
         amount=2356_09
     )
    ],
    start_parameter="create_invoice_elbow_ankle_support",
    photo_url="https://medmarck.com/wp-content/uploads/2021/07/1453193951.jpg",
    photo_size=600,
    need_shipping_address=True,
    need_email=True,
    need_phone_number=True,
    is_flexible=True
)

WRIST_SUPPORT = Item(
    title="Повязка для запястье",
    description="Повязка на запястье из высококачественного дышащего материала, поддерживающего после травм и во время интенсивных нагрузок. Регулируемый размер: 130 ~ 230 мм",
    currency="RUB",
    prices=[
     LabeledPrice(
         label="Wrist_support",
         amount=1788_06
     )
    ],
    start_parameter="create_invoice_wrist_support",
    photo_url="https://medmarck.com/wp-content/uploads/2021/07/Wrist-Wrap.png",
    photo_size=600,
    need_shipping_address=True,
    need_email=True,
    need_phone_number=True,
    is_flexible=True
)

WHEY_PROTEIN = Item(
    title="Сывороточный протеин TOPSIX",
    description="Протеин исключительно из растворимого Carbery Carbelac 80\n🔥Содержание белка 80%\n🔥2,2 г лейцина на дозу\n🔥4,6 г BCAA на дозу\n🔥Всего 9% углеводов",
    currency="RUB",
    prices=[
     LabeledPrice(
         label="Whey_protein",
         amount=5891_98
     )
    ],
    start_parameter="create_invoice_whey_support",
    photo_url="https://medmarck.com/wp-content/uploads/2021/07/wheyprotein.png",
    photo_size=600,
    need_shipping_address=True,
    need_email=True,
    need_phone_number=True,
    is_flexible=True
)


OMEGA3 = Item(
    title="Mega 3 Omega",
    description="90 капсул. Mega 3 Omega - это пищевая добавка с очень чистой концентрацией жирных кислот Омега-3 EPA и DHA. Он содержит 70% концентрированных жирных кислот омега-3 рыбьего жира, пищевой желатин, глицерин и d-альфа-токоферол.",
    currency="RUB",
    prices=[
     LabeledPrice(
         label="Omega",
         amount=1389_00
     )
    ],
    start_parameter="create_invoice_omega",
    photo_url="https://ibb.co/JsWNZTh",
    photo_size=600,
    need_shipping_address=True,
    need_email=True,
    need_phone_number=True,
    is_flexible=True
)

MULTISIX = Item(
    title="Мультивитаминный комплекс",
    description="Мультивитаминная пищевая добавка в гранулах, доступная в 30 стиках по 3 г. Специально разработан для удовлетворения повышенной потребности в витаминах и минералах при занятиях спортом, в эксклюзивной формуле для орального применения с очень приятным вкусом.",
    currency="RUB",
    prices=[
     LabeledPrice(
         label="Multisix",
         amount=989_00
     )
    ],
    start_parameter="create_invoice_multisix",
    photo_url="https://medmarck.com/wp-content/uploads/2021/07/multisix.png",
    photo_size=600,
    need_shipping_address=True,
    need_email=True,
    need_phone_number=True,
    is_flexible=True
)

VITAMIN_C = Item(
    title="Витамин C",
    description="Пищевая добавка витамина C в гранулах со вкусом апельсина, доступная в 30 стиках по 3 г для орального применения. Мы рекомендуем брать палку в конце тяжелого физического упражнения или когда мышцы особенно напряжены. Принимать по 2 палочки в день прямо в рот или растворять в воде, желательно перед едой или непосредственно перед приёмом пищи.",
    currency="RUB",
    prices=[
     LabeledPrice(
         label="Vitaminc",
         amount=1299_00
     )
    ],
    start_parameter="create_invoice_vitaminc",
    photo_url="https://medmarck.com/wp-content/uploads/2021/07/vitaminc.png",
    photo_size=600,
    need_shipping_address=True,
    need_email=True,
    need_phone_number=True,
    is_flexible=True
)

CEREBREMED = Item(
    title="Cerebremed",
    description="Препарат для улучшения состояния и функций мозга. Полностью органическая формула. Уникальный авторский состав и технология обработки лекарственных растений.",
    currency="RUB",
    prices=[
     LabeledPrice(
         label="Cerebremed",
         amount=7999_00
     )
    ],
    start_parameter="create_invoice_cerebremed",
    photo_url="https://medmarck.com/wp-content/uploads/2021/07/Cerebremed.png",
    photo_size=600,
    need_shipping_address=True,
    need_email=True,
    need_phone_number=True,
    is_flexible=True,
)

VIRLAZA = Item(
    title="Virlaza",
    description="Травяной и минеральный экстракт. Питьевая добавка на основе растительных и минеральных экстрактов. Набор жидких полифениловых добавок.",
    currency="RUB",
    prices=[
     LabeledPrice(
         label="Virlaza",
         amount=8789_00
     )
    ],
    start_parameter="create_invoice_virlaza",
    photo_url="https://medmarck.com/wp-content/uploads/2021/07/Virlaza.png",
    photo_size=600,
    need_shipping_address=True,
    need_email=True,
    need_phone_number=True,
    is_flexible=True,
)


POST_REGULAR_SHIPPING = types.ShippingOption(
    id="post_reg",
    title="Post delivery",
    prices=[
        types.LabeledPrice(
            "Fast delivery", 1000_0
        )
    ]
)

POST_FAST_SHIPPING = types.ShippingOption(
    id="post_fast",
    title="Express Delivery",
    prices=[
        types.LabeledPrice(
            "Express delivery - DHL", 3000_0
        )
    ]
)