import json

def GetClicks():
    with open("data/data.json", "r") as file:
        data = json.load(file)
        if not "clicks" in data:
            return "db_error"
        clicks = data["clicks"]
        return clicks

def SetClicks(amount):
    with open("data/data.json", "r") as file:
        data = json.load(file)
        if not "clicks" in data:
            return "db_error"
        data["clicks"] = amount
        with open("data/data.json", "w") as file:
            json.dump(data, file)
            return data["clicks"]
            
def IncrementClicks():
    clicks = GetClicks()
    return SetClicks(clicks + 1)

def GetUpgrades():
    with open("data/data.json", "r") as file:
        data = json.load(file)
        if not "upgrades" in data:
            return "db_error"
        upgrades = data["upgrades"]
        return upgrades

def GetActiveUpgrades():
    upgrades = GetUpgrades()
    active = upgrades["active"]
    return active

def GetOwnedUpgrades():
   upgrades = GetUpgrades()
   owned = upgrades["owned"]
   return owned
