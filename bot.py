
import logging
from telegram import Update, InputFile
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

logging.basicConfig(level=logging.INFO)
TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
         "Привет 👋\n"
        "Я — Татьяна, архитектор и GSR-специалист.\n\n"
        "Ты здесь, потому что чувствуешь, что с пространством — что-то не то.\n\n"
        "Если ты ловишь себя на раздражении дома — скорее всего, дело не в тебе, а в среде.\n"
        "Вот чеклист, с которым работают мои клиенты ⤵️"
    )
    with open("5_errors_interior_state_detailed.pdf", "rb") as f:
        await update.message.reply_document(document=InputFile(f))
"Хочешь больше таких материалов и неожиданных откровений?\n\n"
        "🔗 Подписывайся на канал: @tm_ad_gsr\n\n"

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
