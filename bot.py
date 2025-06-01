
import logging
from telegram import Update, InputFile
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

logging.basicConfig(level=logging.INFO)
TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я — Татьяна, архитектор и GSR-специалист.\n\n"
        "Вот PDF, с которого начинают мои клиенты:"
    )
    with open("5_errors_interior_state_detailed.pdf", "rb") as f:
        await update.message.reply_document(document=InputFile(f))

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
