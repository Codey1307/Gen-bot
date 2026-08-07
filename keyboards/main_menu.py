from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def get_main_menu():

    keyboard = [

        [
            InlineKeyboardButton(
                "🏙 Города",
                callback_data="cities"
            )
        ],

        [
            InlineKeyboardButton(
                "📱 User-Agent",
                callback_data="ua"
            )
        ],

        [
            InlineKeyboardButton(
                "👤 ФИО",
                callback_data="names"
            )
        ],
        
        [
            InlineKeyboardButton(
                "📷 Фото",
                callback_data="photos"
            )
        ],

        [
            InlineKeyboardButton(
                "⚙ Настройки",
                callback_data="settings"
            )
        ]

    ]

    return InlineKeyboardMarkup(keyboard)