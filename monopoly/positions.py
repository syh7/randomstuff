JAIL_POS = 10
PARKING_POS = 20
GOTOJAIL_POS = 30
TAX_POS = [4, 38]
COMMUNITY_POS = [2, 17, 33]
UTILITIES_POS = [4, 12, 28]
STATIONS_POS = [5, 15, 25, 35]
CHANCES_POS = [7, 22, 36]


class Deed:
    number = 0
    owner = ""
    houses = 0
    mortgage = False

    def addHouse(self):
        self.houses += 1

    def removeHouse(self):
        self.houses -= 1

    def bankrupt(self):
        self.mortgage = True

    def setOwner(self, newowner):
        self.owner = newowner

    def __init__(self, number):
        self.number = number
