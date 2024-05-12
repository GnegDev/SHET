from pymongo import MongoClient

print("Initalizing database...")
mdbClient = MongoClient("mongodb://host.docker.internal:27017")

database = mdbClient["SHET_DB"]["users"]
print("Database initalized")

def initializeUser(userId):
    userInfo = {"userId": userId, "step": 0, "weight": 0.0, "height": 0.0, "bmi": 0.0, "bmr": 0.0, "exercises": "кардио"}
    if not getUserInfo(userId):
        return database.insert_one(userInfo)
    else:
        query = {"userId": userId}
        newValues = {"$set": userInfo}
        return database.update_one(query, newValues)

def getUserInfo(userId):
    query = {"userId": userId}
    return database.find_one(query)

def updateUserWeight(userId, weight):
    query = {"userId": userId}
    newValues = {"$set": {"weight": weight}}
    return database.update_one(query, newValues)

def updateUserHeight(userId, height):
    query = {"userId": userId}
    newValues = {"$set": {"height": height}}
    return database.update_one(query, newValues)

def updateUserBMI(userId):
    query = {"userId": userId}

    userInfo = getUserInfo(userId)
    weight = userInfo["weight"]
    height = userInfo["height"] / 100

    newValues = {"$set": {"bmi": weight / (height ** 2)}}
    return database.update_one(query, newValues)

def updateUserBMR(userId):
    query = {"userId": userId}

    userInfo = getUserInfo(userId)
    weight = userInfo["weight"]
    height = userInfo["height"] / 100

    newValues = {"$set": {"bmr": 10 * weight + 6.25 * 100 * height - 5 * 30}}
    return database.update_one(query, newValues)

def switchExercises(userId):
    query = {"userId": userId}
    if getUserInfo(userId)["exercises"] == "кардио":
        newValues = {"$set": {"exercises": "силовые"}}
    else:
        newValues = {"$set": {"exercises": "кардио"}}
    return database.update_one(query, newValues)


def updateUserStep(userId, step):
    query = {"userId": userId}
    newValues = {"$set": {"step": step}}
    return database.update_one(query, newValues)
        