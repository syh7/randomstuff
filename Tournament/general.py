import json
from pprint import pprint
from random import shuffle
from operator import itemgetter
from itertools import repeat
import math

players = []
placements = []
categories = []
tour_type = ""
stage_type = ""


def readFile():
    global players, categories, tour_type, stage_type
    data = json.load(open("players.json"))
    players = data[0]["players"]
    categories = data[0]["categories"]
    tour_type = data[0]["type"]
    stage_type = data[0]["stage"]
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
                cat_players = blindGroups(cat_players)
            elif tour_type == "seed":
                cat_players = seededGroups(cat_players)
            # print("cat_players")
            # pprint(cat_players)
            placements.append(cat_players)


def blindGroups(playerlist):
    shuffle(playerlist)
    length = playerlist.__len__()
    if length % 4 == 0 or length % 4 == 1:
        nrOfGroups = int(length / 4)
    else:
        nrOfGroups = int(math.ceil(length / 4))
    return roundRobin(playerlist, nrOfGroups)


def seededGroups(playerlist):
    playerlist.sort(key=itemgetter("strength"))
    length = playerlist.__len__()
    if length % 4 == 0 or length % 4 == 1:
        nrOfGroups = int(length / 4)
    else:
        nrOfGroups = int(math.ceil(length / 4))
    return roundRobin(playerlist, nrOfGroups)


def roundRobin(playerlist, nrOfGroups):
    pprint(playerlist)
    groups = [[] for i in repeat(None, nrOfGroups)]
    player_iterable = iter(playerlist)
    currentGroup = 0
    nextGroup = 1
    while player_iterable:
        try:
            player = next(player_iterable)
            groups[currentGroup].append(player)
            currentGroup += nextGroup
            if currentGroup == nrOfGroups:
                nextGroup = -1
                currentGroup -= 1
            elif currentGroup == -1:
                nextGroup = 1
                currentGroup += 1
        except StopIteration:
            break
    return groups


readFile()
algorithm()
saveFile()
