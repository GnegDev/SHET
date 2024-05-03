from telebot import TeleBot


from Bot import config
from Bot.handlers import commandsHandlers, messagesHandlers, callbackHandlers

print("Initialization...")

bot = TeleBot(config.TELEGRAM_TOKEN)

def register_handlers():
    bot.register_message_handler(commandsHandlers.startHandler, commands=['start'], pass_bot=True)
    bot.register_message_handler(commandsHandlers.menuHandler, commands=['menu'], pass_bot=True)

    bot.register_message_handler(messagesHandlers.messageHandler, content_types=['text'], pass_bot=True)

    bot.register_callback_query_handler(callbackHandlers.updateInfoHandler, func=lambda callback: callback.data == 'updateInfo', pass_bot=True)
    bot.register_callback_query_handler(callbackHandlers.getExercises, func=lambda callback: callback.data == 'getExercises', pass_bot=True)

def main():
    register_handlers()
    bot.infinity_polling()

if __name__ == "__main__":
    print("Bot started")
    main()