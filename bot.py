
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

# Команда /start
async def start(update: Update, context):
    await update.message.reply_text("Привет! Я AvodaIsraelBot. Чем могу помочь?")

# Команда /help
async def help_command(update: Update, context):
    await update.message.reply_text("Я могу ответить на твои вопросы. Напиши мне что-нибудь!")

# Обработка всех текстовых сообщений
async def handle_message(update: Update, context):
    user_message = update.message.text
    response = f"Ты написал: {user_message}"
    await update.message.reply_text(response)

# Основной код
if __name__ == "__main__":
    TOKEN = "8126776097:AAHZ_OK9Y_4LFyCMP_99c7Tc3uC8Wfd6v-w"  # Твой токен
    app = ApplicationBuilder().token(TOKEN).build()

    # Добавляем обработчики команд
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("AvodaIsraelBot запущен!")
    app.run_polling()
