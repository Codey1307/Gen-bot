from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def get_amount_menu(prefix: str):

    keyboard = [
        [
            InlineKeyboardButton("1", callback_data=f"{prefix}:1"),
            InlineKeyboardButton("2", callback_data=f"{prefix}:2"),
            InlineKeyboardButton("3", callback_data=f"{prefix}:3")
        ],
        [
            InlineKeyboardButton("4", callback_data=f"{prefix}:4"),
            InlineKeyboardButton("5", callback_data=f"{prefix}:5")
        ],
        [
            InlineKeyboardButton("⬅ Назад", callback_data="back")
        ]
    ]

    return InlineKeyboardMarkup(keyboard)