from telegram import Update
from telegram.ext import ContextTypes

from config import ADMIN_ID
from keyboards import admin_keyboard


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text(
            "👋 خوش اومدی.\n\nاین ربات خصوصی است."
        )
        return

    await update.message.reply_text(
        "🎬 پنل مدیریت GIF",
        reply_markup=admin_keyboard()
    )
