import csv, numpy as np
import os
from operator import itemgetter, attrgetter

def clear(): os.system('cls')


class Player:
    def __init__(self,
                 player,
                 position,
                 gamecount,
                 winrate,
                 kda,
                 csPerMin,
                 GPerMin,
                 kpPercent,
                 dmgPercent):
        self.name = player
        self.position = position
        self.gamecount = gamecount
        self.winrate = winrate
        self.kda = kda
        self.csPerMin = csPerMin
        self.GPerMin = GPerMin
        self.kpPercent = kpPercent
        self.dmgPercent = dmgPercent
        self.rating = round(int(gamecount) * (float(winrate.rstrip("%")) / 100), 2)

    def playerName(self):
        print(self.name)

    def playerLane(self):
        return self.position

    def __str__(self):
        return (
            f'Name: {self.name:<15}\tRating: {self.rating:<5}\tLane: {self.position:<9}\tGames: {self.gamecount:<5}\tWinrate: {self.winrate:<7}\tKDA: {self.kda:<5}\tCS per min: {self.csPerMin:<5}\tG per min: {self.GPerMin:<5}\tKill Particip.: {self.kpPercent:<5}\tDmg%: {self.dmgPercent}')


class Team:
    def __init__(self, teamname):
        self.roster = []
        self.teamname = teamname
        self.lanes = ["MID", "TOP", "ADC", "JUNGLE", "SUPPORT"]

    def addToRoster(self, p: Player):
        # print(f'{p.name} wants to join as {p.position}')
        if self.roster:
            if all(x.position.lower() != p.position.lower() for x in self.roster):
                # print(f'  This team does not have a {p.position}, adding {p.name}')
                self.roster.append(p)
        else:
            # print(f'  This team does not have a {p.position}, adding {p.name}')
            self.roster = [p]

    def __str__(self):
        res = ""
        if self.roster:
            for i in self.roster:
                if isinstance(i, Player):
                    res += f'{i.name} as {i.position}, '
        return f'Roster info for\t{self.teamname}: {res.rstrip(", ")}.'

    def unoccupiedLanes(self):
        res = []
        for i in self.lanes:
            if all(i.lower() != p.position.lower() for p in self.roster):
                res.append(i)

        return res


# Player,Position,Games,Win rate,KDA,CSM,GPM,KP%,DMG%,DPM,GD@15,FB %

class Database:

    def __init__(self, data: [Player]):
        self.database = data

    # TOP,MID,ADC,SUPPORT,JUNGLE
    def getAllLaners(self, lane):
        res = []
        for i in self.database:
            if isinstance(i, Player):
                if i.position == lane:
                    res.append(i)
        return res

    def searchForPlayer(self, player):
        for i in self.database:
            if i.name.lower() == player.lower():
                return i


with open('res/data.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    array = []
    for row in csv_reader:
        # print(f'Column names are {", ".join(row)}')
        array.append(
            Player(row["Player"], row["Position"], row["Games"], row["Win rate"], row["KDA"], row["CSM"], row["GPM"],
                   row["KP%"], row["DMG%"]))
        # print(array[line_count])
    # print(f'Processed {line_count} lines.')
    db = Database(array)
    teamA = Team(input("Welcome to league manager 2020 - Type your teamname: "))
    credits = 500

    while teamA.unoccupiedLanes():
        print(f'you have {credits} credits you can use to purchase pro players')
        i = 1
        for row in teamA.unoccupiedLanes():
            print(f' {i}) {row}')
            i += 1
        selected = int(input("Type the number of the lane you want to buy players from: "))
        clear()
        listoflaners = db.getAllLaners(teamA.unoccupiedLanes()[selected-1])
        listoflaners.sort(key=lambda wa: wa.rating, reverse=True)
        i = 1
        for laners in listoflaners:
            print(f'{i}) {laners}')
            i += 1
        selected = int(input("List of top laners - Type a player number to purchase them for your team roster: "))
        teamA.addToRoster(listoflaners[selected-1])
        clear()
        print(teamA)


