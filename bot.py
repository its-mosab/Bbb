from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, WebAppInfo
from telegram.ext import Updater, CommandHandler, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    keyboard = [[InlineKeyboardButton("افتح التطبيق", web_app=WebAppInfo(url="https://its-mosab.github.io/Bbb/index.html"))]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('اضغط على الزر لفتح التطبيق:', reply_markup=reply_markup)

def main() -> None:
    updater = Updater("7225739052:AAF0e4cNK9WM0EZI7YnzK_S5t0tvLIOtMsQ")

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
