from telebot import TeleBot
from telebot.types import Message

from Tools import mdbHandler, keyboardBuilder

def startHandler(message: Message, bot: TeleBot):
    mdbHandler.initializeUser(message.from_user.id)
    bot.send_message(message.chat.id, text="Введите вес: ")

def menuHandler(message: Message, bot: TeleBot):
    userInfo = mdbHandler.getUserInfo(message.from_user.id)

    weight = userInfo["weight"]
    height = userInfo["height"]
    bmi = userInfo["bmi"]
    bmr = userInfo["bmr"]

    bot.send_message(message.chat.id, text=f"{message.from_user.full_name}\n\nВес: {weight} кг\nРост: {height} см\nИМТ: {bmi}\nРекомендуемая калорийность: {bmr} ккал", reply_markup=keyboardBuilder.buildKeyboard(message.from_user.id))

