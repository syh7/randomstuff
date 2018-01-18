# interesting board positions
JAIL_POS = 10
PARKING_POS = 20
GOTOJAIL_POS = 30
TAX_POS = [4, 38]
COMMUNITY_POS = [2, 17, 33]
UTILITIES_POS = [12, 28]
STATIONS_POS = [5, 15, 25, 35]
CHANCES_POS = [7, 22, 36]


class Deed:

    def addHouse(self, p):
        if self.houses == 5:
            print(p.getName() + " tried to upgrade his property but it's full already.")
            return
        if self.houses == 4:
            print(p.getName() + " bought a hotel on deed " + repr(self.number) + "for the cost of " + repr(
                self.hotelCost))
            p.changeMoney(-self.hotelCost)
        else:
            print(p.getName() + " bought a house on deed " + repr(self.number) + "for the cost of " + repr(
                self.houseCost))
            p.changeMoney(-self.houseCost)
        self.houses += 1

    def removeHouse(self, p):
        if self.houses == 0:
            print(p.getName() + " tried to sell a house on deed " + repr(self.number) + " which doesn't have houses.")
            raise ValueError
        if self.houses == 5:
            print(p.getName() + " sold a hotel for and got: " + repr(self.hotelCost))
            p.changeMoney(self.hotelCost / 2)
        else:
            print(p.getName() + " sold a house for and got: " + repr(self.houseCost))
            p.changeMoney(self.houseCost / 2)
        self.houses -= 1

    def getHouses(self):
        return self.houses

    def getRent(self, name):
        # you don;t pay rent for your own property or when it's mortgaged
        if self.mortgaged or name == self.owner:
            return 0
        else:
            return self.rent[self.houses]

    def mortgage(self, p):
        if self.houses > 0:
            print("can't bankrupt if you still have houses left")
            raise NotImplementedError
        if self.mortgaged:
            print("can't mortgage twice")
            raise NotImplementedError
        self.mortgaged = True
        p.changeMoney(self.price / 2)

    def unmortgage(self, p):
        if not self.mortgaged:
            print("You can't mortgage deed " + repr(self.number) + " without mortgaging it first.")
            raise NotImplementedError
        self.mortgaged = False
        p.changeMoney(-self.price)

    def getPrice(self):
        return self.price

    def setOwner(self, newowner):
        self.owner = newowner

    def getOwner(self):
        return self.owner

    def __init__(self, number, rent, price, houseCost, hotelCost):
        self.number = number  # id number
        self.rent = rent  # array with cost for different housing
        self.price = price  # how much the deed costs
        self.houseCost = houseCost  # cost of adding a house
        self.hotelCost = hotelCost  # cost of upgrading to a hotel
        self.houses = 0  # number of houses
        self.owner = ""  # which player owns the property
        self.mortgaged = False  # see if the property is mortgaged, in which case players won't pay for rent


class Railroads:

    def getOwner(self, road):
        return self.owners[self.roads.index(road)]

    def getRoad(self, number):
        if number == 5:
            return self.roads[0]
        elif number == 15:
            return self.roads[1]
        elif number == 25:
            return self.roads[2]
        elif number == 35:
            return self.roads[3]
        else:
            raise ValueError

    def mortgage(self, road, p):
        index = self.roads.index(road)
        if self.owners[index] != p.getName():
            print(p.getName() + " can't mortgage a " + road + " you don't own")
            raise ValueError
        if self.mortgaged[index]:
            print("can't mortgage twice")
            raise ValueError
        p.changeMoney(self.price/2)
        self.mortgaged[index] = True

    def buy(self, road, p):
        index = self.roads.index(road)
        if self.owners[index] != "":
            print(p.getName() + " tried to buy " + road + " even though it's owned by " + self.owners[index])
            raise ValueError
        self.owners[index] = p.getName()
        p.changeMoney(-self.price)

    def getRent(self, road, name):
        index = self.roads.index(road)
        owner = self.owners[index]
        # you don't pay rent for your own property
        if owner == name or self.mortgaged[index]:
            return 0
        rent = 12.5  # this is 12.5 because we will do x2 at least once, but the lowest price is 25
        for x in self.owners:
            if x == owner:
                rent = 2*rent
        return rent

    def __init__(self):
        self.owners = ["", "", "", ""]  # list for owners of respective places
        self.roads = ["Reading Railroad", "Pennsylvania RailRoad", "B&O Railroad", "Short Line"]
        self.mortgaged = [False, False, False, False]
        self.numbers = [5, 15, 25, 35]
        self.price = 200


class Utilities:

    def getOwner(self, road):
        return self.owners[self.roads.index(road)]

    def mortgage(self, road, p):
        index = self.roads.index(road)
        if self.owners[index] != p.getName():
            print(p.getName() + " can't mortgage " + road + " if they don't own it.")
            raise ValueError
        if self.mortgaged[index]:
            print("can't mortgage twice")
            raise ValueError
        p.changeMoney(self.price / 2)
        self.mortgaged[index] = True

    def getRoad(self, number):
        if number == 12:
            return self.roads[0]
        elif number == 28:
            return self.roads[1]
        else:
            raise ValueError

    def buy(self, road, p):
        index = self.roads.index(road)
        if self.owners[index] != "":
            print(p.getName() + " tried to buy " + road + " even though it's owned by " + self.owners[index])
            raise ValueError
        self.owners[index] = p.getName()
        p.changeMoney(-self.price)

    def getMultiplier(self, road, name):
        index = self.roads.index(road)
        owner = self.owners[index]
        # you don't pay rent for your own property
        if owner == name or self.mortgaged[index]:
            return 0
        if self.owners[0] == self.owners[1]:
            return 10
        else:
            return 4

    def __init__(self):
        self.owners = ["", ""]  # list for owners of respective places
        self.roads = ["Water Works", "Electric Company"]
        self.mortgaged = [False, False]
        self.numbers = [12, 28]
        self.price = 150
