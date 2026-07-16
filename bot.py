from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
)

from config import BOT_TOKEN
from database import create_tables
from handlers import (
    start,
    handle_message,
)

def main():
    create_tables()

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(
            filters.ALL,
            handle_message
        )
    )

    print("Bot Started...")

    app.run_polling()


if __name__ == "__main__":
    main()
