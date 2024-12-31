from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

# توکن ربات
BOT_TOKEN = "7842366836:AAFxrMQAVlHk6jXR5-eiE7buqJHkWYjPp94"

# لیست Chat ID‌ها
CHAT_IDS = [
    "5793439133",
    "7853304554"
]

# مدیریت پیام‌های دریافتی و ارسال آن‌ها به لیست Chat ID‌ها
async def forward_message(update: Update, context):
    user_message = update.message.text

    # ارسال پیام به همه آیدی‌ها
    for chat_id in CHAT_IDS:
        await context.bot.send_message(chat_id=chat_id, text=f"پیام جدید: {user_message}")

async def start(update: Update, context):
    await update.message.reply_text("سلام! این ربات پیام‌های دریافتی را به دو آیدی ارسال می‌کند.")

def main():
    # ساخت اپلیکیشن
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # اضافه کردن دستور /start
    app.add_handler(CommandHandler("start", start))

    # هندل پیام‌های متنی
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_message))

    # اجرای ربات
    app.run_polling()

if __name__ == "__main__":
    main()
