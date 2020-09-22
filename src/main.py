import csv, numpy as np


class Database:
    def __init__(self, database):
        self.database = database

    # TOP,MID,ADC,SUPPORT,JUNGLE
    def getAllLaners(self, lane):
        res = []
        for i in self.database:
            if isinstance(i,Player):
                i.position == lane
                res.append(i)
        return res

    def searchForPlayer(self, player):
        for i in self.database:
            if i.name.lower() == player.lower():
                return i

            
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
        self.ranking = round(int(gamecount)*(float(winrate.rstrip("%"))/100),2)

    def playerName(self):
        print(self.name)

    def playerLane(self):
        return self.position

    def playerData(self):
        print(f'Name: {self.name:<15}\tLane: {self.position:<9}\tGames: {self.gamecount:<5}\tWinrate: {self.winrate:<7}\tKDA: {self.kda:<5}\tCS per min: {self.csPerMin:<5}\tG per min: {self.GPerMin:<5}\tKill Particip.: {self.kpPercent:<5}\tDmg%: {self.dmgPercent}')


class Team:
    def __init__(self, teamname):
        self.roster = []
        self.teamname = teamname

    def addToRoster(self, p: Player):
        print(f'{p.name} wants to join as {p.position}')
        if self.roster:
            if all(x.position != p.position for x in self.roster):
                print(f'  This team does not have a {p.position}, adding {p.name}')
                self.roster.append(p)
        else:
            print(f'  This team does not have a {p.position}, adding {p.name}')
            self.roster = [p]

    def printRoster(self):
        res = ""
        if self.roster:
            for i in self.roster:
                if isinstance(i, Player):
                    res += f'{i.name} as {i.position}, '
        print(f'Roster info for\t{self.teamname}: {res}')


# Player,Position,Games,Win rate,KDA,CSM,GPM,KP%,DMG%,DPM,GD@15,FB %

with open('res/data.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    array = [Player for i in range(0, 500)]
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        array[line_count] = Player(row["Player"], row["Position"], row["Games"], row["Win rate"], row["KDA"], row["CSM"], row["GPM"], row["KP%"], row["DMG%"])
        array[line_count].playerData()
        line_count += 1
    print(f'Processed {line_count} lines.')
    teamA = Team(input("Type your teamname\n"))

    teamA.addToRoster(array[line_count-1])
    teamA.addToRoster(array[line_count-2])
    teamA.addToRoster(array[line_count-2])

    teamA.addToRoster(array[line_count-3])
    teamA.addToRoster(array[line_count-4])
    teamA.addToRoster(array[line_count-5])


    teamA.printRoster()
    DB = Database(array)
