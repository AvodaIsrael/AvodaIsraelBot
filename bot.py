from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import smtplib
from email.mime.text import MIMEText

# Настройки почты
EMAIL_ADDRESS = "liza.neveleva@gmail.com"  # Почта получателя
EMAIL_PASSWORD = "LiNeRU1987"  # Пароль приложения
RECIPIENT_EMAIL = "liza.neveleva@gmail.com"  # Получатель

# Временное хранилище данных
user_data = {}

# Вопросы для кандидатов
candidate_questions = [
    "Как тебя зовут? / What's your name? / מה שמך?",
    "Номер телефона / Phone number / מספר טלפון",
    "Какой статус в Израиле? / What's your status in Israel? / מה המעמד שלך בישראל?",
    "В каком городе живёшь? / Where do you live? / באיזו עיר אתה גר?",
    "Готов ли к переезду? / Are you ready to relocate? / האם אתה מוכן לעבור דירה?",
    "Есть ли автомобиль? / Do you have a car? / האם יש לך רכב?",
    "Есть водительские права? / Do you have a driving license? / האם יש לך רישיון נהיגה?",
    "В какой сфере ищешь работу? / What field are you looking for a job in? / באיזה תחום אתה מחפש עבודה?",
    "Какой рабочий опыт есть? / What is your work experience? / מה הניסיון המקצועי שלך?",
    "Есть ли особые предпочтения по графику? / Any preferences for the schedule? / האם יש לך העדפות מסוימות בלוח זמנים?",
]

# Вопросы для работодателей
employer_questions = [
    "Как называется фирма? / What's the company name? / מה שם החברה?",
    "На какую должность ищете сотрудника? / What position are you hiring for? / לאיזו משרה אתה מחפש עובד?",
    "Когда сотрудник должен приступить к работе? / When should the employee start? / מתי העובד צריך להתחיל לעבוד?",
    "Адрес работы с указанием города / Work address with city / כתובת העבודה כולל עיר",
    "Контактное лицо: имя и номер телефона / Contact person: name and phone / איש קשר: שם ומספר טלפון",
    "Какой график работы? / What's the work schedule? / מה לוח הזמנים לעבודה?",
    "Какая заработная плата? Как часто выплачивается? / Salary? How often is it paid? / מה השכר? באיזו תדירות הוא משולם?",
    "Есть ли подвозка или оплата проезда? / Is there transportation or travel reimbursement? / האם יש הסעות או החזר נסיעות?",
    "Трудоустройство официальное? / Is the employment official? / האם ההעסקה רשמית?",
    "Дополнительные требования к опыта кандидата / Additional requirements for experience / דרישות נוספות לניסיון",
]

# Функция отправки email
def send_email(subject, body):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = RECIPIENT_EMAIL

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)

# Стартовая команда
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["🔎 Ищу работу / Looking for a job / מחפש עבודה"],
        ["📢 Предлагаю работу / Offering a job / מציע עבודה"],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    await update.message.reply_text(
        "Выберите, пожалуйста, вариант:\n\nChoose an option:\n\nבחרו אפשרות:",
        reply_markup=reply_markup,
    )

# Обработка ответа
async def handle_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    user_id = update.message.chat_id

    # Если пользователь ищет работу
    if "Ищу работу" in user_input or "Looking for a job" in user_input or "מחפש עבודה" in user_input:
        user_data[user_id] = {"type": "candidate", "answers": []}
        await update.message.reply_text(candidate_questions[0])
    # Если пользователь предлагает работу
    elif "Предлагаю работу" in user_input or "Offering a job" in user_input or "מציע עבודה" in user_input:
        user_data[user_id] = {"type": "employer", "answers": []}
        await update.message.reply_text(employer_questions[0])
    else:
       await update.message.reply_text(
    "Извините, я не понял ваш выбор.\n\n"
    "Sorry, I didn't understand your choice.\n\n"
    "מצטער, לא הבנתי את הבחירה שלך."
)
