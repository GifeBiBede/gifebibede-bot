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
    # -------------------------
    # افزودن GIF
    # -------------------------

    if text == "➕ افزودن GIF":

        waiting_for_gif[user_id] = True

        await update.message.reply_text(
            "🎬 GIF را ارسال کن."
        )

        return

    # -------------------------
    # ذخیره کد
    # -------------------------

    if user_id in waiting_for_code:

        code = text.strip()

        file_id = waiting_for_code[user_id]

        try:

            add_gif(code, file_id)

        except Exception:

            await update.message.reply_text(
                "❌ این کد قبلاً ثبت شده."
            )

            return

        waiting_for_code.pop(user_id)

        link = f"https://t.me/{BOT_USERNAME}?start={code}"

        await update.message.reply_text(
            f"""✅ GIF ذخیره شد.

🔗 {link}"""
        )

        return
    # -------------------------
    # لیست
    # -------------------------

    if text == "📂 لیست GIFها":

        gifs = list_gifs()

        if not gifs:

            await update.message.reply_text(
                "هیچ GIFی ثبت نشده."
            )

            return

        msg = ""

        for code, downloads in gifs:

            msg += f"• {code} | دانلود: {downloads}\n"

        await update.message.reply_text(msg)

        return
