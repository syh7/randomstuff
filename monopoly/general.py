import random, time
from monopoly import player, positions, cards

BOARD_SIZE = 40

dice = [-1, -1]  # two dice to play with
game = True  # boolean to check if game is running
doubles = 0  # amount of double throws in a row
parking = 0  # amount on free parking
players = []  # list of players
utilities = positions.Utilities()  # object for utilities
railroads = positions.Railroads()  # object for railroads


def throwDice():
    return random.randint(1, 3)


def moveClosestRail(p):
    global railroads
    position = p.getPos()
    # switch on chance places
    if position == 7:
        p.setPos(5)
    elif position == 22:
        p.setPos(25)
    elif position == 36:
        p.setPos(35)
    else:
        print("chance card at a no change card road")
        raise ValueError

    position = p.getPos()
    road = railroads.getRoad(position)
    rent = 2*railroads.getRent(road, p.getName())  # double price because chance card
    print(p.getName() + " has to pay " + repr(rent) + " rent.")
    p.changeMoney(-rent)


def repairs(p, houseCost, hotelCost):
    total = 0
    housetotal = 0
    hoteltotal = 0
    for deed in p.getDeeds():
        nrOfHouses = deed.getHouses()
        if nrOfHouses == 5:
            total += hotelCost
            hoteltotal += 1
        else:
            total += nrOfHouses * houseCost
            housetotal += nrOfHouses
    print(p.getName() + " has to pay " + repr(total) + " for " + repr(housetotal) + " houses and " + repr(hoteltotal) +
          " hotels.")
    p.changeMoney(-total)


def getChance(p):
    global parking
    card = random.choice(list(cards.Chance))
    print("event card: " + card.value)
    position = p.getPos()
    if card == cards.Chance.START:
        p.setPos(0)
        p.changeMoney(200)
    elif card == cards.Chance.RAIL1 or card == cards.Chance.RAIL2:
        moveClosestRail(p)
    elif card == cards.Chance.DIVIDEND:
        p.changeMoney(50)
    elif card == cards.Chance.JAIL:
        p.jail()
    elif card == cards.Chance.FREE:
        p.recvJailFree()
    elif card == cards.Chance.BACK:
        p.setPos(position - 3)
        if position - 3 == 0:
            p.changeMoney(200)
    elif card == cards.Chance.REPAIRS:
        repairs(p, 25, 100)
    elif card == cards.Chance.TAX:
        p.changeMoney(-15)
        parking += 15
    elif card == cards.Chance.READING:
        if position > 6:
            p.changeMoney(200)
        p.setPos(5)
    elif card == cards.Chance.BOARDWALK:
        p.setPos(39)
    elif card == cards.Chance.CHAIRMAN:
        global players
        for pl in players:
            pl.changeMoney(50)
        p.changeMoney(-50 * len(players))
    elif card == cards.Chance.BUILDING:
        p.changeMoney(150)
    elif card == cards.Chance.CROSSWORD:
        p.changeMoney(100)
    else:
        print("ERROR: event card has wrong code." + card.value)
        raise ValueError


def getCommunity(p):
    global parking
    card = random.choice(list(cards.Community))
    print("community card: " + card.value)
    if card == cards.Community.START:
        p.setPos(0)
        p.changeMoney(200)
    elif card == cards.Community.BANK:
        p.changeMoney(200)
    elif card == cards.Community.DOCTOR:
        p.changeMoney(-50)
        parking += 50
    elif card == cards.Community.JAIL:
        p.jail()
    elif card == cards.Community.FREE:
        p.recvJailFree()
    elif card == cards.Community.STOCK:
        p.changeMoney(50)
    elif card == cards.Community.OPERA:
        global players
        for pl in players:
            pl.changeMoney(-50)
        p.changeMoney(50 * len(players))
    elif card == cards.Community.XMAS:
        p.changeMoney(100)
    elif card == cards.Community.TAX:
        p.changeMoney(20)
    elif card == cards.Community.BIRTHDAY:
        global players
        for pl in players:
            pl.changeMoney(-20)
        p.changeMoney(20 * len(players))
    elif card == cards.Community.INSURANCE:
        p.changeMoney(100)
    elif card == cards.Community.HOSPITAL:
        p.changeMoney(-100)
        parking += 100
    elif card == cards.Community.SCHOOL:
        p.changeMoney(-150)
        parking += 150
    elif card == cards.Community.CONSULT:
        p.changeMoney(25)
    elif card == cards.Community.REPAIRS:
        repairs(p, 45, 115)
    elif card == cards.Community.BEAUTY:
        p.changeMoney(10)
    elif card == cards.Community.HERITAGE:
        p.changeMoney(100)
    else:
        print("ERROR: event card has wrong code." + card.value)
        raise ValueError


def getParking(p):
    global parking
    print("Parking received: " + repr(parking))
    p.changeMoney(parking)
    parking = 0


def onUtility(p):
    global utilities
    road = utilities.getRoad(p.getPos())
    multiplier = utilities.getMultiplier(road, p.getName())
    rent = multiplier * (dice[0] + dice[1])
    print(p.getName() + " has to pay " + repr(rent) + " rent.")
    p.changeMoney(-rent)
    return


def turn(p):
    # If the player is jailed, no chance to do anything but get out of jail.
    if p.isJailed():
        dice[0] = throwDice()
        dice[1] = throwDice()
        print(p.getName() + " threw " + repr(dice[0]) + " and " + repr(dice[1]))
        if dice[0] == dice[1]:
            p.setFree()
        else:
            p.updateJailedThrows()
        return

    # Player is not in jail, thus regular throw.
    global doubles
    dice[0] = throwDice()
    dice[1] = throwDice()
    if dice[0] == dice[1]:
        doubles += 1
    else:
        doubles = 0
    print(p.getName() + " threw " + repr(dice[0] + dice[1]) + " with " + repr(doubles) + " doubles in a row.")
    # Three doubles in a row is to jail
    if doubles == 3:
        doubles = 0
        p.jail()
    else:
        p.changePos(dice[0] + dice[1])
    handlePosition(p)


def handlePosition(p):
    # TODO: implement buying stuff
    # TODO: regular deeds
    position = p.getPos()
    if position == positions.GOTOJAIL_POS:
        p.jail()
    elif position in positions.TAX_POS:
        print(p.getName() + " has to pay 200 tax.")
        p.changeMoney(-200)
    elif position in positions.CHANCES_POS:
        getChance(p)
    elif position in positions.COMMUNITY_POS:
        getCommunity(p)
    elif position == positions.PARKING_POS:
        getParking(p)
    elif position in positions.UTILITIES_POS:
        onUtility(p)


p1 = player
p1.setName("p1")
players.append(p1)
while game:
    for pla in players:
        turn(pla)
        while doubles > 0:
            turn(pla)
        doubles = 0
