# interesting board positions
JAIL_POS = 10
PARKING_POS = 20
GOTOJAIL_POS = 30
TAX_POS = [4, 38]
COMMUNITY_POS = [2, 17, 33]
UTILITIES_POS = [4, 12, 28]
STATIONS_POS = [5, 15, 25, 35]
CHANCES_POS = [7, 22, 36]


class Deed:

    def addHouse(self, p):
        if self.houses == 5:
            print(p.getName() + " tried to upgrade his property but it's full already.")
            return
        if self.houses == 4:
            print(p.getName() + " bought a hotel on deed " + repr(self.number) + "for the cost of " + repr(self.hotelCost))
            p.changeMoney(-self.hotelCost)
        else:
            print(p.getName() + " bought a house on deed " + repr(self.number) + "for the cost of " + repr(self.houseCost))
            p.changeMoney(-self.houseCost)
        self.houses += 1

    def removeHouse(self, p):
        if self.houses == 0:
            print(p.getName() + " tried to sell a house on deed " + repr(self.number) + " which doesn't have houses.")
            raise ValueError
        if self.houses == 5:
            print(p.getName() + " sold a hotel for and got: " + repr(self.hotelCost))
            p.changeMoney(self.hotelCost/2)
        else:
            print(p.getName() + " sold a house for and got: " + repr(self.houseCost))
            p.changeMoney(self.houseCost/2)
        self.houses -= 1

    def getHouses(self):
        return self.houses

    def getRent(self, name):
        if self.mortgage or name == self.owner:
            return 0
        else:
            return self.cost[self.houses]

    def bankrupt(self, p):
        if self.houses > 0:
            print("can't bankrupt if you still have houses left")
            raise NotImplementedError
        self.mortgage = True
        p.changeMoney(self.cost[0]/2)

    def setOwner(self, newowner):
        self.owner = newowner

    def __init__(self, number, cost, houseCost, hotelCost):
        self.number = number  # id number
        self.cost = cost  # array with cost for different housing
        self.houseCost = houseCost  # cost of adding a house
        self.hotelCost = hotelCost  # cost of upgrading to a hotel
        self.houses = 0  # number of houses
        self.owner = ""  # which player owns the property
        self.mortgage = False  # see if the property is mortgaged, in which case players won't pay for rent
