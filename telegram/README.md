# Telegram Bot (python-telegram-bot)

## Prasyarat
- Python 3.9+
- Token Telegram bot dari **@BotFather**

## Setup
1) Install dependensi:
```bash
pip install -r requirements.txt
```

2) Buat file `.env` di folder ini:
```env
BOT_TOKEN=PASTE_TOKEN_DISINI
```

> `.env` **tidak akan ikut ter-upload** ke GitHub karena sudah di-`gitignore`.

## Menjalankan bot
```bash
python bot.py
```

Bot akan menjalankan **polling**.

## Perintah
- `/start`
- `/help`
- `/menu`
- `/info`

## Menambah Handler Baru
Karena struktur masih sederhana (semua handler ada di `bot.py`), langkahnya:
1. Buat fungsi async handler baru, misalnya `async def my_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:`
2. Tambahkan pendaftaran handler di `main()`:
```python
app.add_handler(CommandHandler(["mycommand"], my_command))
```

Kalau nanti kamu ingin memisahkan handler ke folder `handlers/`, pola ini bisa dipindahkan per file lalu diregistrasikan dari `bot.py`.


