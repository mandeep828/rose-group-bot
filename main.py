import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        user = update.message.from_user
        chat = update.message.chat

        if user and not user.is_bot:
            username = user.username or ""
            first_name = user.first_name or ""
            name_combined = f"{first_name} {username}".lower()
            if "rose" in name_combined:
                try:
                    await context.bot.ban_chat_member(chat_id=chat.id, user_id=user.id)
                    await update.message.reply_text(f"Banned user {first_name} ({username}) for using 'rose' in name.")
                except Exception as e:
                    print(f"Failed to ban user: {e}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL & filters.ChatType.GROUPS, handle_message))
    print("Bot started...")
    app.run_polling()