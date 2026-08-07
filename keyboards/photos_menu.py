from pathlib import Path

from telegram import InlineKeyboardButton, InlineKeyboardMarkup


PHOTO_DIR = Path("data/photos")


def get_photos_menu():

    keyboard = []

    if PHOTO_DIR.exists():

        folders = sorted(
            [
                folder
                for folder in PHOTO_DIR.iterdir()
                if folder.is_dir()
            ],
            key=lambda x: x.name.lower()
        )

        for folder in folders:

            keyboard.append(
                [
                    InlineKeyboardButton(
                        folder.name,
                        callback_data=f"photo:{folder.name}"
                    )
                ]
            )

    keyboard.append(
        [
            InlineKeyboardButton(
                "⬅ Назад",
                callback_data="back"
            )
        ]
    )

    return InlineKeyboardMarkup(keyboard)