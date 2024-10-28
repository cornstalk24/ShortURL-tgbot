import os
import clck
from telegram import Update, BotCommand
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Приветствие при запуске бота"""
    await update.message.reply_text("Привет! Отправь мне ссылку, и я сокращу её.")

async def shorten_link(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Сокращает ссылку и отправляет пользователю."""
    original_url = update.message.text.strip()

    if not original_url.startswith("http"):
        await update.message.reply_text("Пожалуйста, отправьте правильный URL, начинающийся с http или https.")
        return

    try:
        short_url = clck.ru(original_url)
        if short_url:
            await update.message.reply_text(f"Сокращенная ссылка: {short_url}")
        else:
            await update.message.reply_text("Не удалось сократить ссылку. Попробуйте позже.")
    except Exception as e:
        # Отправляем сообщение об ошибке пользователю и выводим её в лог
        await update.message.reply_text("Произошла ошибка при сокращении ссылки. Попробуйте позже.")
        print(f"Ошибка при сокращении ссылки: {e}")

# Функция для регистрации команд в BotFather
async def post_init(application: Application) -> None:
    bot_commands = [
        BotCommand("start", "Начало работы с ботом"),
    ]
    await application.bot.set_my_commands(bot_commands)

def main() -> None:
    """Запуск бота"""
    bot_token = os.getenv("BOT_TOKEN")
    if not bot_token:
        raise ValueError("Токен бота не задан. Укажите BOT_TOKEN в переменных окружения.")

    # создаем приложение 
    application = Application.builder().token(bot_token).post_init(post_init).build()

    # добавляем обработчики команд и сообщений
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, shorten_link))

    # Запускаем бота до нажатия Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
