from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
)

from config import BOT_TOKEN

from handlers.start import start
from handlers.menu import menu_callback


def main():

    app = Application.builder().token(BOT_TOKEN).build()

    # Команда /start
    app.add_handler(
        CommandHandler(
            "start",
            start
        )
    )

    # Обработка нажатий на кнопки
    app.add_handler(
        CallbackQueryHandler(
            menu_callback
        )
    )

    print("Бот запущен.")

    app.run_polling()


if __name__ == "__main__":
    main()