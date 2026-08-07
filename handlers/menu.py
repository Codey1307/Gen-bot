from telegram import Update
from telegram.ext import ContextTypes

from keyboards.main_menu import get_main_menu
from keyboards.ua_menu import get_ua_menu
from keyboards.amount_menu import get_amount_menu
from keyboards.names_menu import get_names_menu
from keyboards.photos_menu import get_photos_menu
from keyboards.photo_amount_menu import get_photo_amount_menu

from handlers.cities import generate_cities
from handlers.useragents import generate_useragents
from handlers.names import generate_surnames
from handlers.photos import send_random_photo


async def menu_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    data = query.data

    # ==========================================================
    # ГЛАВНОЕ МЕНЮ
    # ==========================================================

    if data == "cities":

        await query.edit_message_text(
            text="🏙 <b>Генератор городов</b>\n\nВыберите количество:",
            reply_markup=get_amount_menu("cities"),
            parse_mode="HTML"
        )

    elif data == "ua":

        await query.edit_message_text(
            text="📱 <b>Генератор User-Agent</b>\n\nВыберите сервис:",
            reply_markup=get_ua_menu(),
            parse_mode="HTML"
        )

    elif data == "names":

        await query.edit_message_text(
            text="👤 <b>Генератор Фамилий</b>\n\nВыберите раздел:",
            reply_markup=get_names_menu(),
            parse_mode="HTML"
        )

    elif data == "photos":

        await query.edit_message_text(
            text="📷 <b>Фото</b>\n\nВыберите человека:",
            reply_markup=get_photos_menu(),
            parse_mode="HTML"
        )

    elif data == "settings":

        await query.edit_message_text(
            text="⚙ Настройки\n\nРаздел находится в разработке."
        )

    # ==========================================================
    # ГОРОДА
    # ==========================================================

    elif data.startswith("cities:"):

        amount = int(data.split(":")[1])

        cities = generate_cities(amount)

        text = f"🏙 <b>Сгенерировано {len(cities)} город(ов)</b>\n\n"

        for city in cities:

            text += (
                f"📍 <b>{city['name']}</b>\n"
                f"{city['latitude']}, {city['longitude']}\n\n"
            )

        await query.edit_message_text(
            text=text,
            reply_markup=get_amount_menu("cities"),
            parse_mode="HTML"
        )

    # ==========================================================
    # USER AGENT
    # ==========================================================

    elif data.startswith("ua:"):

        parts = data.split(":")

        if len(parts) == 2:

            source = parts[1]

            await query.edit_message_text(
                text=f"📱 <b>{source.upper()}</b>\n\nВыберите количество:",
                reply_markup=get_amount_menu(f"ua:{source}"),
                parse_mode="HTML"
            )

        elif len(parts) == 3:

            source = parts[1]
            amount = int(parts[2])

            agents = generate_useragents(source, amount)

            text = f"📱 <b>{source.upper()}</b>\n\n"

            for i, agent in enumerate(agents, start=1):
                text += f"{i}.\n<code>{agent}</code>\n\n"

            await query.edit_message_text(
                text=text,
                reply_markup=get_amount_menu(f"ua:{source}"),
                parse_mode="HTML"
            )

    # ==========================================================
    # ФАМИЛИИ
    # ==========================================================

    elif data.startswith("names:"):

        parts = data.split(":")

        if len(parts) == 2:

            mode = parts[1]

            await query.edit_message_text(
                text="👤 <b>Генератор фамилий</b>\n\nВыберите количество:",
                reply_markup=get_amount_menu(f"names:{mode}"),
                parse_mode="HTML"
            )

        elif len(parts) == 3:

            mode = parts[1]
            amount = int(parts[2])

            if mode == "surnames":

                surnames = generate_surnames(amount)

                text = f"👤 <b>Сгенерировано {len(surnames)} фамилий</b>\n\n"

                for i, surname in enumerate(surnames, start=1):
                    text += f"{i}. <code>{surname}</code>\n"

                await query.edit_message_text(
                    text=text,
                    reply_markup=get_amount_menu(f"names:{mode}"),
                    parse_mode="HTML"
                )

   # ==========================================================
# ФОТО
# ==========================================================

    elif data.startswith("photo:"):

        folder = data.split(":", 1)[1]

        await query.edit_message_text(
        text=(
            f"📷 <b>{folder}</b>\n\n"
            "Выберите количество фотографий:"
        ),
        reply_markup=get_photo_amount_menu(folder),
        parse_mode="HTML"
    )

    elif data.startswith("photo_send:"):

        _, folder, amount = data.split(":")

        await send_random_photo(
        update=update,
        context=context,
        folder_name=folder,
        amount=int(amount),
    )

    # ==========================================================
    # НАЗАД
    # ==========================================================

    elif data == "back":

        await query.edit_message_text(
            text=(
                "🤖 <b>Generator Bot</b>\n\n"
                "Выберите нужный генератор."
            ),
            reply_markup=get_main_menu(),
            parse_mode="HTML"
        )