from telebot import types

from Tools import mdbHandler

def buildKeyboard(userId):
    keyboard = types.InlineKeyboardMarkup()

    buttons = [
        types.InlineKeyboardButton(text="Изменить вес и рост", callback_data="updateInfo"),
        types.InlineKeyboardButton(text="Получить упражнения", callback_data="getExercises"),
        types.InlineKeyboardButton(text=f"Тип тренировок: {mdbHandler.getUserInfo(userId)["exercises"]}", callback_data="switchExercises")
    ]

    for button in buttons:
        keyboard.add(button)

    return keyboard