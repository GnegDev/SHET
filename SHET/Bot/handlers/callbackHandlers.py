from yandexgptlite import YandexGPTLite

from telebot import TeleBot
from telebot.types import CallbackQuery

from Bot import config
from Bot.handlers import commandsHandlers

from Tools import mdbHandler, keyboardBuilder

yandexgptClient = YandexGPTLite(config.YANDEX_CLOUD_ID, config.YANDEXGPT_TOKEN)

def updateInfoHandler(callback: CallbackQuery, bot: TeleBot):
    # лютый костылище
    message = callback.message
    message.from_user.id = callback.from_user.id
    
    commandsHandlers.startHandler(message, bot)

def switchExercises(callback: CallbackQuery, bot: TeleBot):
    message = callback.message
    mdbHandler.switchExercises(callback.from_user.id)
    userInfo = mdbHandler.getUserInfo(callback.from_user.id)

    weight = userInfo["weight"]
    height = userInfo["height"]
    bmi = userInfo["bmi"]
    bmr = userInfo["bmr"]

    print("Editing...")
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text=f"{callback.from_user.full_name}\n\nВес: {weight} кг\nРост: {height} см\nИМТ: {bmi}\nРекомендуемая калорийность: {bmr} ккал", reply_markup=keyboardBuilder.buildKeyboard(callback.from_user.id))
    print("Edited.")

def getExercises(callback: CallbackQuery, bot: TeleBot):
    message = callback.message
    bot.send_message(message.chat.id, text="Подбираю...")

    userInfo = mdbHandler.getUserInfo(callback.from_user.id)
    bmi = userInfo["bmi"]
    bmr = userInfo["bmr"]
    exercises = userInfo["exercises"]

    response = yandexgptClient.create_completion(f"Подбери возможные {exercises} упражнения для ИМТ {bmi} и калорийности {bmr}. Выведи только список упражнений.", "0.5")

    bot.send_message(message.chat.id, text=response)
