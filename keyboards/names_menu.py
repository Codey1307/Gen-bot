from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def get_names_menu():

    keyboard = [
        [
            InlineKeyboardButton(
                "Фамилии",
                callback_data="names:surnames"
            )
        ],
        [
            InlineKeyboardButton(
                "⬅ Назад",
                callback_data="back"
            )
        ]
    ]

    return InlineKeyboardMarkup(keyboard)