import random, time
from monopoly import player, positions, cards

BOARD_SIZE = 40

dice = [-1, -1]  # two dice to play with
game = True  # boolean to check if game is running
doubles = 0  # amount of double throws in a row
parking = 0  # amount on free parking
players = []  # list of players


def throwDice():
    return random.randint(1, 3)


def moveClosestRail(p):
    position = p.getPos()


def repairs(p, houseCost, hotelCost):
    total = 0
    housetotal = 0
    hoteltotal = 0
    for deed in p.getDeeds():
        houses = deed.getHouses()
        if houses == 5:
            total += hotelCost
            hoteltotal += 1
        else:
            total += houses*houseCost
            housetotal += houses
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
        return
        # TODO: implement opera
    elif card == cards.Community.XMAS:
        p.changeMoney(100)
    elif card == cards.Community.TAX:
        p.changeMoney(20)
    elif card == cards.Community.BIRTHDAY:
        return
        # TODO: implement birthday
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
    doubles = 0
    dice[0] = throwDice()
    dice[1] = throwDice()
    if dice[0] == dice[1]:
        doubles += 1
    else:
        doubles = 0
    print(p.getName() + " threw " + repr(dice[0] + dice[1]) + " with " + repr(doubles) + " doubles in a row.")
    p.changePos(dice[0] + dice[1])
    # Three doubles in a row is to jail
    if doubles == 3:
        p.jail()


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


p1 = player
p1.setName("p1")
while game:
    turn(p1)
    handlePosition(p1)
    time.sleep(0.5)
