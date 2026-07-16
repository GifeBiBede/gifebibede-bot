from telegram import Update
from telegram.ext import ContextTypes

from config import ADMIN_ID, BOT_USERNAME
from keyboards import admin_keyboard
from database import (
    add_gif,
    list_gifs,
    delete_gif
)

# حافظه موقت
waiting_for_gif = {}
waiting_for_code = {}


async def handle_message(update: Update,
                         context: ContextTypes.DEFAULT_TYPE):

    if update.effective_user.id != ADMIN_ID:
        return

    user_id = update.effective_user.id

    # -------------------------
    # دریافت GIF
    # -------------------------

    if update.message.animation:

        if user_id not in waiting_for_gif:
            return

        waiting_for_code[user_id] = update.message.animation.file_id

        waiting_for_gif.pop(user_id)

        await update.message.reply_text(
            "✏ حالا یک کد برای این GIF وارد کن.\n\nمثال:\ncat001"
        )

        return

    # -------------------------
    # متن
    # -------------------------

    text = update.message.text
