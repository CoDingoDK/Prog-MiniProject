import csv, numpy

class Team:
    
    def __init__(self, teamname):
        self.teamname = teamname

    def
    def printRoster(self):
        print(f'Roster info for\t{self.teamname}: ')

class Player:
    def __init__(self,
                 player,
                 position,
                 gamecount,
                 winrate,
                 kda,
                 avgkills,
                 avgdeath,
                 avgassists,
                 csPerMin,
                 GPerMin,
                 kpPercent,
                 dmgPercent):
        self.name = player
        self.position = position
        self.gamecount = gamecount
        self.winrate = winrate
        self.kda = kda
        self.avgkills = avgkills
        self.avgdeath = avgdeath
        self.avgassists = avgassists
        self.csPerMin = csPerMin
        self.GPerMin = GPerMin
        self.kpPercent = kpPercent
        self.dmgPercent = dmgPercent

    def playerName(self):
        print(self.name)

    def playerData(self):
        print(f'\t{self.name}, {self.position}, {self.gamecount}, {self.winrate}, {self.kda}, {self.csPerMin}, {self.GPerMin}, {self.kpPercent},{self.dmgPercent}.')


# Player,Position,Games,Win rate,KDA,CSM,GPM,KP%,DMG%,DPM,GD@15,FB %

with open('res/data.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    array = [0 for i in range(0, 500)]
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        array[line_count] = Player(row["Player"], row["Position"], row["Games"], row["Win rate"], row["KDA"], row["CSM"], row["GPM"], row["KP%"], row["DMG%"], row["DPM"], row["GD@15"], row["FB %"])
        array[line_count].playerData()
        line_count += 1
    print(f'Processed {line_count} lines.')
    teamA = Team(input("Type your teamname\n"))
    teamA.printRoster()