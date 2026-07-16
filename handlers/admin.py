from telegram import Update
from telegram.ext import ContextTypes

from config import ADMIN_ID


async def handle_message(update: Update,
                         context: ContextTypes.DEFAULT_TYPE):

    if update.effective_user.id != ADMIN_ID:
        return

    text = update.message.text

    if text == "➕ افزودن GIF":

        await update.message.reply_text(
            "🎬 لطفاً GIF را ارسال کن."
        )

        return

    if text == "📂 لیست GIFها":

        await update.message.reply_text(
            "هنوز GIFی ثبت نشده."
        )

        return

    if text == "🗑 حذف GIF":

        await update.message.reply_text(
            "کد GIF را ارسال کن."
        )

        return

    if text == "✏ ویرایش GIF":

        await update.message.reply_text(
            "کد GIF را ارسال کن."
        )

        return

    if text == "📊 آمار":

        await update.message.reply_text(
            "آمار بعداً اضافه می‌شود."
        )

        return
