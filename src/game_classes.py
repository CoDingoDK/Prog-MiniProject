from tkinter import StringVar


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
        self.credits = 400
        self.teamname = teamname
        self.lanes = ["MID", "TOP", "ADC", "JUNGLE", "SUPPORT"]

    def add_to_roster(self, p: Player):
        if self.roster:
            if all(x.position.lower() != p.position.lower() for x in self.roster):
                if p.price <= self.credits:
                    self.roster.append(p)
                    self.credits -= p.price
        else:
            if p.price <= self.credits:
                self.roster = [p]
                self.credits -= p.price

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
            if all(i.upper() != p.position.upper() for p in self.roster):
                res.append(i)

        return res

    def get_player_power_from_lanes(self, *lanes):
        res = []
        for lane in lanes:
            for i in self.roster:
                if lane.upper() == i.position.upper():
                    res.append(int(i.rating))
        return res

    def is_ready(self):
        if len(self.roster) == 5:
            return True
        return False

class Database:
    def __init__(self, data: [Player]):
        self.data = data

    # TOP,MID,ADC,SUPPORT,JUNGLE
    def get_players_from_lane(self, lane):
        res = []
        for i in self.data:
            if i.position.upper() == lane.upper() and not i.isDrafted:
                res.append(i)
        res.sort(key=lambda p: p.rating, reverse=False)
        return res

    def search_for_player(self, player_name):
        for i in self.data:
            if i.name.upper() == player_name.upper():
                return i

    def draft_player(self, player):
        selected_player = None
        if isinstance(player, str):
            selected_player = self.search_for_player(player)
        elif isinstance(player, Player):
            selected_player = player
        else:
            return selected_player
        drafted_player = None
        for i, p in enumerate(self.data):
            if p == selected_player:
                if not p.isDrafted:
                    p.isDrafted = True
                    drafted_player = p
        return drafted_player

