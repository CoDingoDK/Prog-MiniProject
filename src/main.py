import csv, numpy as np

from operator import itemgetter, attrgetter

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
        self.rating = round(int(gamecount)*(float(winrate.rstrip("%"))/100),2)

    def playerName(self):
        print(self.name)

    def playerLane(self):
        return self.position

    def __str__(self):
        return (f'Name: {self.name:<15}\tRating: {self.rating:<5}\tLane: {self.position:<9}\tGames: {self.gamecount:<5}\tWinrate: {self.winrate:<7}\tKDA: {self.kda:<5}\tCS per min: {self.csPerMin:<5}\tG per min: {self.GPerMin:<5}\tKill Particip.: {self.kpPercent:<5}\tDmg%: {self.dmgPercent}')


class Team:
    def __init__(self, teamname):
        self.roster = []
        self.teamname = teamname

    def addToRoster(self, p: Player):
        # print(f'{p.name} wants to join as {p.position}')
        if self.roster:
            if all(x.position != p.position for x in self.roster):
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
        array.append(Player(row["Player"], row["Position"], row["Games"], row["Win rate"], row["KDA"], row["CSM"], row["GPM"], row["KP%"], row["DMG%"]))
        # print(array[line_count])
    # print(f'Processed {line_count} lines.')
    teamA = Team(input("Type your teamname\n"))

    teamA.addToRoster(array[15])
    teamA.addToRoster(array[156])
    teamA.addToRoster(array[12])
    teamA.addToRoster(array[216])
    teamA.addToRoster(array[25])
    teamA.addToRoster(array[48])

    DB = Database(array)

    subarray = DB.getAllLaners("TOP")
    subarray.sort(key=lambda wa: wa.rating, reverse=True)
    for i in subarray:
        print(i)
