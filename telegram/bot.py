import logging
import os

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Ambil token dari environment variable (lebih aman)
# Optional: load BOT_TOKEN dari file .env kalau ada
try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    # kalau python-dotenv belum terpasang, token harus diset via environment variable
    pass

TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise RuntimeError(
        "BOT_TOKEN is not set. Isi c:/telegram/.env (BOT_TOKEN=...) atau set environment variable BOT_TOKEN."
    )

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message:
        await update.message.reply_text("Halo Sandyka! Bot sudah aktif 🚀")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("/help received")
    if update.message:
        await update.message.reply_text(
            "Perintah yang tersedia:\n"
            "- /start : menyalakan bot\n"
            "- /help  : menampilkan bantuan\n"
            "- /menu  : menampilkan menu\n"
            "- /info  : informasi bot"
        )


async def menu_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message:
        await update.message.reply_text(
            "MENU:\n"
            "1) /start\n"
            "2) /help\n"
            "3) /menu\n"
            "4) /info"
        )


async def info_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message:
        await update.message.reply_text(
            "INFO BOT\n"
            "Ini adalah bot Telegram contoh yang dibuat dengan python-telegram-bot."
        )


def main() -> None:
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler(["start"], start))
    app.add_handler(CommandHandler(["help"], help_command))
    app.add_handler(CommandHandler(["menu"], menu_command))
    app.add_handler(CommandHandler(["info"], info_command))

    logger.info("Bot polling dimulai...")
    app.run_polling()


if __name__ == "__main__":
    main()

