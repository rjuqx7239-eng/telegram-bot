from telegram.ext import ApplicationBuilder

def setup_telegram_bot(token):
    app = ApplicationBuilder().token(token).build()
    return app
