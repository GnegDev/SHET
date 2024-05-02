from yandexgptlite import YandexGPTLite

from telebot import TeleBot
from telebot.types import CallbackQuery

from Bot import config
from Bot.handlers import commandsHandlers

from Tools import mdbHandler

yandexgptClient = YandexGPTLite(config.YANDEX_CLOUD_ID, config.YANDEXGPT_TOKEN)

def updateInfoHandler(callback: CallbackQuery, bot: TeleBot):
    # лютый костылище
    message = callback.message
    message.from_user.id = callback.from_user.id
    
    commandsHandlers.startHandler(message, bot)

def getExercises(callback: CallbackQuery, bot: TeleBot):
    message = callback.message
    bot.send_message(message.chat.id, text="Подбираю...")

    userInfo = mdbHandler.getUserInfo(callback.from_user.id)
    bmi = userInfo["bmi"]
    bmr = userInfo["bmr"]

    response = yandexgptClient.create_completion(f"Подобрать упражнения для ИМТ {bmi} и калорийности {bmr}.", 0.5)

    bot.send_message(message.chat.id, text=response)
