from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def get_ua_menu():

    keyboard = [
        [
            InlineKeyboardButton("Мамба", callback_data="ua:mamba"),
            InlineKeyboardButton("ВКДВ/ ТГДВ", callback_data="ua:vkdv")
        ],
        [
            InlineKeyboardButton("Бебо/Лоло", callback_data="ua:beboo"),
            InlineKeyboardButton("Лоло", callback_data="ua:beboo")
        ],
        [
            InlineKeyboardButton("LovePlanet", callback_data="ua:loveplanet")
        ],
        [
            InlineKeyboardButton("ОКЗ", callback_data="ua:okz")
        ],
        [
            InlineKeyboardButton("⬅ Назад", callback_data="back")
        ]
    ]

    return InlineKeyboardMarkup(keyboard)