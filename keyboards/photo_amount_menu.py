from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def get_photo_amount_menu(folder_name: str):

    keyboard = [
        [
            InlineKeyboardButton("1", callback_data=f"photo_send:{folder_name}:1"),
            InlineKeyboardButton("2", callback_data=f"photo_send:{folder_name}:2"),
            InlineKeyboardButton("3", callback_data=f"photo_send:{folder_name}:3"),
            InlineKeyboardButton("4", callback_data=f"photo_send:{folder_name}:4"),
            InlineKeyboardButton("5", callback_data=f"photo_send:{folder_name}:5"),
        ],
        [
            InlineKeyboardButton("⬅ Назад", callback_data="photos")
        ]
    ]

    return InlineKeyboardMarkup(keyboard)