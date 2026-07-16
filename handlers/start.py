from telegram import Update
from telegram.ext import ContextTypes

from config import ADMIN_ID
from keyboards import admin_keyboard
from database import (
    get_gif,
    increase_download,
)


async def start(update: Update,
                context: ContextTypes.DEFAULT_TYPE):

    user = update.effective_user

    # اگر لینک start داشت
    if context.args:

        code = context.args[0]

        gif = get_gif(code)

        if not gif:

            await update.message.reply_text(
                "❌ این GIF پیدا نشد."
            )

            return

        increase_download(code)

        await update.message.reply_animation(
            animation=gif[2]
        )

        return

    # مدیر
    if user.id == ADMIN_ID:

        await update.message.reply_text(
            "🎬 پنل مدیریت GIF",
            reply_markup=admin_keyboard()
        )

        return

    # کاربر عادی

    await update.message.reply_text(
        "👋 به ربات خوش آمدید."
    )
