from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

# Функция для старта
async def start(update: Update, context):
    # Кнопки для выбора
    keyboard = [
        ["🔎 Ищу работу", "📢 Предлагаю работу"],  # Русский
        ["🔎 Looking for a job", "📢 Offering a job"],  # English
        ["🔎 מחפש עבודה", "📢 מציע עבודה"]  # Hebrew
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    await update.message.reply_text(
        "Выберите, пожалуйста, вариант:\n\n"
        "Choose an option:\n\n"
        "בחרו אפשרות:",
        reply_markup=reply_markup
    )

# Функция обработки ответа
async def handle_response(update: Update, context):
    text = update.message.text

    # Ответы на русском
    if text in ["🔎 Ищу работу", "🔎 Looking for a job", "🔎 מחפש עבודה"]:
        await update.message.reply_text("Вы ищете работу! Расскажите, какая работа вам нужна.")
    elif text in ["📢 Предлагаю работу", "📢 Offering a job", "📢 מציע עבודה"]:
        await update.message.reply_text("Вы предлагаете работу! Напишите, какую вакансию вы хотите опубликовать.")
    else:
        await update.message.reply_text(
            "Извините, я не понял ваш выбор.\n\nSorry, I didn't understand your choice.\n\nמצטער, לא הבנתי את הבחירה שלך."
        )

# Основной код
if __name__ == "__main__":
    app = ApplicationBuilder().token("8126776097:AAHZ_OK9Y_4LFyCMP_99c7Tc3uC8Wfd6v-w").build()

    # Обработчик команды /start
    app.add_handler(CommandHandler("start", start))
    # Обработчик текстовых сообщений
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_response))

    print("AvodaIsraelBot запущен!")
    app.run_polling()
