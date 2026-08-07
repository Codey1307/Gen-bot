import random
import zipfile
import tempfile
from pathlib import Path

from telegram.ext import ContextTypes

from keyboards.photo_amount_menu import get_photo_amount_menu

PHOTO_DIR = Path("data/photos")

photo_queue = {}


def get_photos(folder_name: str):

    folder = PHOTO_DIR / folder_name

    if not folder.exists():
        return []

    extensions = {
        ".jpg",
        ".jpeg",
        ".png",
        ".webp",
        ".bmp"
    }

    return sorted(
        [
            p for p in folder.iterdir()
            if p.is_file() and p.suffix.lower() in extensions
        ]
    )


def get_next_photos(folder_name: str, amount: int):

    global photo_queue

    photos = get_photos(folder_name)

    if not photos:
        return []

    if folder_name not in photo_queue:
        photo_queue[folder_name] = []

    result = []

    while len(result) < amount:

        if not photo_queue[folder_name]:

            shuffled = photos.copy()
            random.shuffle(shuffled)

            photo_queue[folder_name] = shuffled

        result.append(photo_queue[folder_name].pop())

    return result


async def send_random_photo(
    update,
    context: ContextTypes.DEFAULT_TYPE,
    folder_name: str,
    amount: int,
):

    query = update.callback_query

    photos = get_photos(folder_name)

    if not photos:

        await query.message.reply_text(
            "❌ В папке нет фотографий."
        )
        return

    amount = min(amount, len(photos))

    selected = get_next_photos(folder_name, amount)

    # удаляем старую клавиатуру
    await query.message.delete()

    # -------------------------------------------------
    # Одно фото
    # -------------------------------------------------

    if amount == 1:

        photo = selected[0]

        with open(photo, "rb") as file:

            await context.bot.send_document(
                chat_id=query.message.chat.id,
                document=file,
                filename=photo.name,
                caption=f"📷 {photo.name}"
            )

    # -------------------------------------------------
    # ZIP
    # -------------------------------------------------

    else:

        with tempfile.NamedTemporaryFile(
            suffix=".zip",
            delete=False
        ) as temp:

            zip_path = Path(temp.name)

        with zipfile.ZipFile(
            zip_path,
            "w",
            compression=zipfile.ZIP_DEFLATED
        ) as archive:

            for photo in selected:

                archive.write(
                    photo,
                    arcname=photo.name
                )

        with open(zip_path, "rb") as file:

            await context.bot.send_document(
                chat_id=query.message.chat.id,
                document=file,
                filename=f"{folder_name}_{amount}.zip",
                caption=f"📦 {amount} случайных фотографий"
            )

        zip_path.unlink(missing_ok=True)

    # -------------------------------------------------
    # Показываем меню снова
    # -------------------------------------------------

    await context.bot.send_message(
        chat_id=query.message.chat.id,
        text=(
            f"📷 <b>{folder_name}</b>\n\n"
            "Выберите количество фотографий:"
        ),
        reply_markup=get_photo_amount_menu(folder_name),
        parse_mode="HTML"
    )