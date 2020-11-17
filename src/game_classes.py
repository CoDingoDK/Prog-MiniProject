import csv


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
        self.isDrafted = False
        self.position = position
        self.gamecount = gamecount
        self.winrate = winrate
        self.kda = kda
        self.csPerMin = csPerMin
        self.GPerMin = GPerMin
        self.kpPercent = kpPercent
        self.dmgPercent = dmgPercent
        self.rating = round(int(gamecount) * (float(winrate.rstrip("%")) / 100), 2)
        self.price = 0

    def player_name(self):
        return self.name

    def player_lane(self):
        return self.position

    def __str__(self):
        return (
            f'Name: {self.name:<15} price: {self.price:<3} Rating: {self.rating:<5} Lane: {self.position:<9} Games: {self.gamecount:<5} Winrate: {self.winrate:<7} KDA: {self.kda:<5} CS per min: {self.csPerMin:<5} G per min: {self.GPerMin:<5} Kill Particip.: {self.kpPercent:<5} Dmg%: {self.dmgPercent}')

    def __eq__(self, other):
        return self.name.lower() == other.name.lower()


class Team:
    def __init__(self, teamname):
        self.roster = []
        self.teamname = teamname
        self.lanes = ["MID", "TOP", "ADC", "JUNGLE", "SUPPORT"]

    def add_to_roster(self, p: Player):
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
        return f'{self.teamname} roster: {res.rstrip(", ")}.'

    def unoccupied_lanes(self):
        res = []
        for i in self.lanes:
            if all(i.lower() != p.position.lower() for p in self.roster):
                res.append(i)

        return res


class Database:
    def __init__(self, data: [Player]):
        self.data = data

    # TOP,MID,ADC,SUPPORT,JUNGLE
    def get_players_from_lane(self, lane):
        res = []
        for i in self.data:
            if i.position == lane:
                res.append(i)
        return res.sort(key=lambda p: p.rating, reverse=False)

    def search_for_player(self, player):
        for i in self.data:
            if i.name.lower() == player.lower():
                return i

    def draft_player(self, player):
        drafted_player = None
        for i, p in enumerate(self.data):
            if p == player:
                if not p.isDrafted:
                    p.isDrafted = True
                    drafted_player = p
        return drafted_player

