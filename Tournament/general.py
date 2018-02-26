import json
from pprint import pprint
from random import shuffle

players = []
placements = []
categories = []
tour_type = ""


def readFile():
    global players, categories, tour_type
    data = json.load(open("players.json"))
    players = data[0]["players"]
    categories = data[0]["categories"]
    tour_type = data[0]["type"]
    # pprint(players)
    # pprint(categories)


def saveFile():
    global placements
    print("\n\nPlacements:\n")
    pprint(placements)
    # Right now prints for testing purposes. Should save to a file instead.


def algorithm():
    global players, categories, placements, tour_type
    for category in categories:
        cat_players = []
        for player in players:
            if player["category"] == category:
                cat_players.append(player)
        if cat_players.__len__() > 0:
            if tour_type == "blind":
                shuffle(cat_players)
            elif tour_type == "seed":
                cat_players = seedBrackets(cat_players)
            # print("cat_players")
            # pprint(cat_players)
            placements.append(cat_players)


def sortList(playerlist):
    return playerlist


def seedBrackets(playerlist):
    if playerlist.__len__() % 2 == 1:
        pass
    else:
        pass
    return []


readFile()
algorithm()
saveFile()
