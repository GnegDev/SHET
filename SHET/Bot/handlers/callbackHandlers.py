import requests
from telebot import TeleBot
from telebot.types import CallbackQuery

from Bot import config
from Bot.handlers import commandsHandlers

from Tools import mdbHandler

def updateInfoHandler(callback: CallbackQuery, bot: TeleBot):
    # лютый костылище
    message = callback.message
    message.from_user.id = callback.from_user.id
    
    commandsHandlers.startHandler(message, bot)

def getExercises(callback: CallbackQuery, bot: TeleBot):
    message = callback.message
    bot.send_message(message.chat.id, text="глып")

    userInfo = mdbHandler.getUserInfo(callback.from_user.id)
    bmi = userInfo["bmi"]
    bmr = userInfo["bmr"]

    headers = {
        'Authorization': f'Bearer {config.YANDEXGPT_TOKEN}',
        'Content-Type': 'application/json'
    }

    data = {
        'query': f'Подобрать упражнения для ИМТ {bmi} и калорийности {bmr}'
    }

    response = requests.post('https://api.aicloud.sbercloud.ru/public/v1/public_inference/gpt-3.5-turbo', headers=headers, json=data)
    #exercises = response.json()['replies'][0]['text']

    print(response)

    #bot.send_message(message.chat.id, text=exercises)
