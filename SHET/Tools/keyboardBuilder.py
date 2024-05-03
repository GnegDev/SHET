from telebot import types

def buildKeyboard():
    keyboard = types.InlineKeyboardMarkup()
    buttons = [
        types.InlineKeyboardButton(text="Изменить вес и рост", callback_data="updateInfo"),
        types.InlineKeyboardButton(text="Получить упражнения", callback_data="getExercises")
    ]

    for button in buttons:
        keyboard.add(button)

    return keyboard