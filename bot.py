import os
import logging
import google.generativeai as genai
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "YOUR_GEMINI_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_TELEGRAM_BOT_TOKEN")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    try:
        response = model.generate_content(user_message)
        reply_text = response.text
    except Exception as e:
        reply_text = "မှားယွင်းမှုတစ်ခု ဖြစ်သွားပါတယ်။ ကျေးဇူးပြု၍ ခဏနေမှ ထပ်ကြိုးစားပါ။"

    await update.message.reply_text(reply_text)

if __name__ == '__main__':
    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    message_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message)
    application.add_handler(message_handler)

    print("Bot စတင်အလုပ်လုပ်နေပါပြီ...")
    application.run_polling()


