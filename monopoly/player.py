position = 0
money = 1000
jailed = False
jailedThrows = 0
name = ""
jailfree = 0
deeds = []


def setName(newname):
    global name
    name = newname


def getName():
    return name


def jail():
    global jailed, position
    jailed = True
    position = 10
    print(name + " is put in jail.")


def setFree():
    global jailed
    jailed = False
    print(name + " IS FINALLY FREEEEEE")
    print(jailed)
    resetJailedThrows()


def updateJailedThrows():
    global jailedThrows
    jailedThrows += 1
    print(name + " has been in jail for " + repr(jailedThrows) + " turns.")


def resetJailedThrows():
    global jailedThrows
    jailedThrows = 0


def isJailed():
    return jailed


def isJailFree():
    global jailfree
    if jailfree > 0:
        jailfree -= 1
        return True
    else:
        return False


def recvJailFree():
    global jailfree
    jailfree += 1


def getPos():
    return position


def getMoney():
    return money


def setPos(newpos):
    global position
    position = newpos
    print(name + " is now on tile " + repr(position))
    if position == 0:
        changeMoney(200)
        print(name + "ended on start and collects 200!")


def setMoney(newmoney):
    global money
    money = newmoney


def changePos(newpos):
    global position
    position = position + newpos
    if position > 39:
        position = position % 40
        changeMoney(200)
        print(name + " has just passed start and collects 200!")

    print(name + " is now on tile " + repr(position))


def changeMoney(newmoney):
    global money
    money += newmoney
    print(name + " now has " + repr(money) + " in their bank account.")


def getDeeds():
    return deeds


def addDeed(deed):
    global deeds
    deeds.push(deed)
