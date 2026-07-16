from telegram import ReplyKeyboardMarkup

def admin_keyboard():
    keyboard = [
        ["➕ افزودن GIF", "📂 لیست GIFها"],
        ["✏ ویرایش GIF", "🗑 حذف GIF"],
        ["📊 آمار"]
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,
        is_persistent=True
    )
