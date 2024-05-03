from telebot import TeleBot
from telebot.types import Message

from Tools import mdbHandler, keyboardBuilder
from Bot.handlers import commandsHandlers

def messageHandler(message: Message, bot: TeleBot):
    userInfo = mdbHandler.getUserInfo(message.from_user.id)
    messageText = message.text
    match userInfo["step"]:
        case 0:
            if messageText.isdigit():
                mdbHandler.updateUserWeight(message.from_user.id, float(messageText))
                mdbHandler.updateUserStep(message.from_user.id, 1)
                bot.send_message(message.chat.id, text="Установлен вес: " + messageText + " кг. Введите рост: ")
            else:
                bot.send_message(message.chat.id, text="Неправильный формат ввода.")
        case 1:
            if messageText.isdigit():
                mdbHandler.updateUserHeight(message.from_user.id, float(messageText))
                mdbHandler.updateUserBMI(message.from_user.id)
                mdbHandler.updateUserBMR(message.from_user.id)

                mdbHandler.updateUserStep(message.from_user.id, 2)
                bot.send_message(message.chat.id, text="Установлен рост: " + messageText + " см.")
                commandsHandlers.menuHandler(message, bot)
            else:
                bot.send_message(message.chat.id, text="Неправильный формат ввода.")