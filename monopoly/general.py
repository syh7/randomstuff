import random, time
from monopoly import player, positions, cards, Gui

BOARD_SIZE = 40

dice = [-1, -1]  # two dice to play with
game = True  # boolean to check if game is running
doubles = 0  # amount of double throws in a row
parking = 0  # amount on free parking
players = []  # list of players
utilities = positions.Utilities()  # object for utilities
railroads = positions.Railroads()  # object for railroads
deeds = []  # list for all properties


def throwDice():
    return random.randint(1, 3)


def makeDeeds():
    global deeds
    deeds.append(positions.Deed(1, "Old Kent Road", {2, 10, 30, 90, 160, 250}, 60, 50, 30, 30))
    deeds.append(positions.Deed(3, "Whitechapel Road", {4, 20, 60, 180, 360, 450}, 60, 50, 30, 30))
    deeds.append(positions.Deed(6, "The Angel Islington", {6, 30, 90, 270, 400, 550}, 100, 50, 50, 50))
    deeds.append(positions.Deed(8, "Euston Road", {6, 30, 90, 270, 400, 550}, 100, 50, 50, 50))
    deeds.append(positions.Deed(9, "Pentonville Road", {8, 40, 100, 300, 450, 600}, 120, 60, 50, 50))
    deeds.append(positions.Deed(11, "Pall Mall", {10, 50, 150, 450, 625, 750}, 140, 70, 100, 100))
    deeds.append(positions.Deed(13, "Whitehall", {10, 50, 150, 450, 625, 750}, 140, 70, 100, 100))
    deeds.append(positions.Deed(14, "Northumberland Avenue", {12, 60, 180, 500, 700, 900}, 160, 80, 100, 100))
    deeds.append(positions.Deed(16, "Bow Street", {14, 70, 200, 550, 750, 950}, 180, 90, 100, 100))
    deeds.append(positions.Deed(18, "Marlborough Street", {14, 70, 200, 550, 750, 950}, 180, 90, 100, 100))
    deeds.append(positions.Deed(19, "Vine Street", {16, 80, 220, 600, 800, 1000}, 200, 100, 100, 100))
    deeds.append(positions.Deed(21, "Strand", {18, 90, 250, 700, 875, 1050}, 220, 110, 150, 150))
    deeds.append(positions.Deed(23, "Fleet Street", {18, 90, 250, 700, 875, 1050}, 220, 110, 150, 150))
    deeds.append(positions.Deed(24, "Trafalgar Square", {20, 100, 300, 750, 925, 1100}, 240, 120, 150, 150))
    deeds.append(positions.Deed(26, "Leicester Square", {22, 110, 330, 800, 975, 1150}, 260, 130, 150, 150))
    deeds.append(positions.Deed(28, "Coventry Street", {22, 110, 330, 800, 975, 1150}, 260, 130, 150, 150))
    deeds.append(positions.Deed(29, "Piccadilly", {24, 120, 360, 850, 1025, 1200}, 280, 140, 150, 150))
    deeds.append(positions.Deed(31, "Regent Street", {26, 130, 390, 900, 1100, 1275}, 300, 150, 200, 200))
    deeds.append(positions.Deed(33, "Oxford Street", {26, 130, 390, 900, 1100, 1275}, 300, 150, 200, 200))
    deeds.append(positions.Deed(34, "Bond Street", {28, 150, 450, 1000, 1200, 1400}, 320, 160, 200, 200))
    deeds.append(positions.Deed(37, "Park Lane", {35, 175, 500, 1100, 1300, 1500}, 350, 175, 200, 200))
    deeds.append(positions.Deed(39, "Mayfair", {50, 200, 600, 1400, 1700, 2000}, 400, 200, 200, 200))


def getDeedByNumber(number):
    global deeds
    for deed in deeds:
        if deed.getNumber() == number:
            return deed
    raise FileNotFoundError


def checkStreet(deed):
    global deeds
    if deed.getNumber() in {1, 3}:
        return getDeedByNumber(1).getOwner() == getDeedByNumber(3).getOwner()
    elif deed.getNumber() in {6, 8, 9}:
        return getDeedByNumber(6).getOwner() == getDeedByNumber(8).getOwner() == getDeedByNumber(9).getOwner()
    elif deed.getNumber() in {11, 13, 14}:
        return getDeedByNumber(11).getOwner() == getDeedByNumber(13).getOwner() == getDeedByNumber(14).getOwner()
    elif deed.getNumber() in {16, 18, 19}:
        return getDeedByNumber(16).getOwner() == getDeedByNumber(18).getOwner() == getDeedByNumber(19).getOwner()
    elif deed.getNumber() in {21, 23, 24}:
        return getDeedByNumber(21).getOwner() == getDeedByNumber(23).getOwner() == getDeedByNumber(24).getOwner()
    elif deed.getNumber() in {26, 28, 29}:
        return getDeedByNumber(26).getOwner() == getDeedByNumber(28).getOwner() == getDeedByNumber(29).getOwner()
    elif deed.getNumber() in {31, 33, 34}:
        return getDeedByNumber(31).getOwner() == getDeedByNumber(33).getOwner() == getDeedByNumber(34).getOwner()
    elif deed.getNumber() in {37, 39}:
        return getDeedByNumber(37).getOwner() == getDeedByNumber(39).getOwner()
    raise FileNotFoundError


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
    rent = 2 * railroads.getRent(road, p.getName())  # double price because chance card
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
    global parking, players
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


def payUtility(p):
    global utilities
    road = utilities.getRoad(p.getPos())
    multiplier = utilities.getMultiplier(road, p.getName())
    rent = multiplier * (dice[0] + dice[1])
    print(p.getName() + " has to pay " + repr(rent) + " rent.")
    p.changeMoney(-rent)
    return


def payDeed(p):
    position = p.getPos()

    deed = getDeedByNumber(position)
    owner = deed.getOwner()
    if owner == p.getName() or deed.getMortgaged():
        return
    rent = deed.getRent(p.getName())
    if deed.getHouses() == 0:
        if checkStreet(deed):
            rent *= 2
    p.changeMoney(-rent)
    global players
    for pl in players:
        if pl.getName() == owner:
            pl.changeMoney(rent)
            return
    raise ValueError


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


def getPlayer(name):
    global players
    for pl in players:
        if pl.getName() == name:
            return pl
    raise LookupError


def handlePosition(p):
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
        payUtility(p)
    else:
        payDeed(p)
        # TODO: implement buying stuff (auction if no interest - includes original player)


makeDeeds()
p1 = player
p1.setName("p1")
players.append(p1)

gui = Gui

while game:
    for pla in players:
        turn(pla)
        while doubles > 0:
            turn(pla)
        doubles = 0
