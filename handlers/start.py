from telegram import Update
from telegram.ext import ContextTypes

from keyboards.main_menu import get_main_menu


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = (
        "🤖 <b>Generator Bot</b>\n\n"
        "Добро пожаловать.\n\n"
        "Выберите нужный генератор."
    )

    await update.message.reply_text(
        text,
        reply_markup=get_main_menu(),
        parse_mode="HTML"
    )