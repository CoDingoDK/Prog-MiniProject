from tkinter import *
from const import *


class UI:
    def __init__(self, window, client, window_name):
        self.window: Tk = window
        self.vars = {
            "team name": StringVar(self.window, "Team A"),
            "enemy team name": StringVar(self.window, "Team B"),
            "team credits": StringVar(self.window, "400$"),
            "enemy team credits": StringVar(self.window, "400$"),
            "team TOP": StringVar(self.window, "TOP"),
            "team ADC": StringVar(self.window, "ADC"),
            "team MID": StringVar(self.window, "MID"),
            "team SUPPORT": StringVar(self.window, "SUPPORT"),
            "team JUNGLE": StringVar(self.window, "JUNGLE"),
            "enemy TOP": StringVar(self.window, "TOP"),
            "enemy ADC": StringVar(self.window, "ADC"),
            "enemy MID": StringVar(self.window, "MID"),
            "enemy SUPPORT": StringVar(self.window, "SUPPORT"),
            "enemy JUNGLE": StringVar(self.window, "JUNGLE"),
            "player name": StringVar(self.window, ""),
            "player lane": StringVar(self.window, ""),
            "player winrate": StringVar(self.window, ""),
            "player kda": StringVar(self.window, ""),
            "player rating": StringVar(self.window, ""),
            "player dmgPercent": StringVar(self.window, "")
        }
        self.player_box = None
        self.combat_log_box = None
        self.window_name = window_name
        self.client = client
        self.combat_log_frame = None
        self.one_time = True
        self.configure_ui()

    def request_teamname(self, frame, textbox):
        teamname = textbox.get().upper()
        self.client.send(ACTION=CLIENT_REQUEST_TEAM_NAME, obj=teamname)
        self.show_frame(frame)

    def request_player(self):
        if self.player_box.size() > 2:
            player = self.player_box.get(ANCHOR)
            self.client.send(ACTION=CLIENT_REQUEST_PLAYER_FOR_TEAM, obj=player)

    def start_match(self):
        self.client.send(ACTION=CLIENT_REQUEST_MATCH)

    def show_frame(self, frame):
        frame.tkraise()

    def update(self):
        if self.client is not None:
            if self.client.team is not None:
                self.vars.get("team name").set(self.client.team.teamname)
                self.vars.get("team credits").set(f'{self.client.team.credits}$')
                for i in self.client.team.roster:
                    self.vars.get(f'team {i.position}').set(i.name.upper())

            if self.client.enemy_team is not None:
                self.vars.get("enemy team name").set(self.client.enemy_team.teamname)
                self.vars.get("enemy team credits").set(f'{self.client.enemy_team.credits}$')
                if self.client.enemy_team.roster:
                    for i in self.client.enemy_team.roster:
                        self.vars.get(f'enemy {i.position}').set(i.name.upper())

        player = self.client.database.search_for_player(self.player_box.get(ANCHOR))
        if player is not None:
            self.vars.get("player name").set(f'NAME: {player.name}')
            self.vars.get("player lane").set(f'LANE: {player.position}')
            self.vars.get("player winrate").set(f'WINRATE: {player.winrate}%')
            self.vars.get("player kda").set(f'KDA: {player.kda}')
            self.vars.get("player rating").set(f'RATING: {player.rating}')
            self.vars.get("player dmgPercent").set(f'DMG%: {player.dmgPercent}%')
        self.window.update()
        if self.one_time:
            if self.client.team is not None and self.client.enemy_team is not None:
                if self.client.team.is_ready() and self.client.enemy_team.is_ready():
                    self.client.send(ACTION=CLIENT_REQUEST_MATCH)
                    self.one_time = False
                    self.show_frame(self.combat_log_frame)
        if self.combat_log_box.size() == 0 and self.client.combat_log is not None:
            for log in self.client.combat_log:
                self.combat_log_box.insert(END, log)

    def get_laners(self, player_search):
        lane = player_search.get().upper()
        accepted_lanes = ("ADC", "MID", "TOP", "SUPPORT", "JUNGLE")
        if lane in accepted_lanes:
            self.player_box.delete(0, END)
            if self.client.database is not None:
                list_lane = self.client.database.get_players_from_lane(lane)
                for item in list_lane:
                    self.player_box.insert(END, item.name)
            else:
                self.player_box.delete(0, END)
                self.player_box.insert(END, "No Database received yet")
                return
        else:
            self.player_box.delete(0, END)
            self.player_box.insert(END, "Not a role, try again")

    def configure_ui(self):
        self.window.title(self.window_name)
        self.window.geometry('1280x720')
        self.window.resizable(0, 0)
        self.window.rowconfigure(0, weight=1)
        self.window.columnconfigure(0, weight=1)
        width = 1280
        background = "#313131"
        font_mini = ('helvetica', 15, 'bold')
        fontsmall = ('helvetica', 30, 'bold')
        fontmed = ('helvetica', 45, 'bold')
        font_large = ('helvetica', 60, 'bold')
        bghighlight = '#313131'
        fground = '#313131'
        text_white = 'white'
        textbg = '#313131'
        textteamone = '#58C9B9'
        textteamtwo = '#C65146'

        start_frame = Frame(self.window, bg=background)
        teamname_frame = Frame(self.window, bg=background)
        teamroster_frame = Frame(self.window, bg=background)
        self.combat_log_frame = Frame(self.window, bg=background)

        for frame in (start_frame, teamname_frame, teamroster_frame, self.combat_log_frame):
            frame.grid(row=0, column=0, sticky='nsew')

        # -------- Frame 1 - MAIN MENU ------------------------------------------------------------------------------
        frame1_title = Label(start_frame, text="WELCOME TO\n LEAGUE SIMULATOR", fg=text_white, bg=bghighlight,
                             font=('helvetica', 70, 'bold'))
        frame1_title.place(relx=0.5, y=250, anchor='center')
        frame1_PLAY = Button(start_frame, text='PLAY'.upper(), font=font_large, fg=textbg, highlightbackground=bghighlight,
                             command=lambda: self.show_frame(teamname_frame))
        frame1_PLAY.place(relx=0.5, y=450, anchor='center')

        # -------- Frame 2 - TEAM NAME SELECT -----------------------------------------------------------------------
        choose_teamname = Label(teamname_frame, text='CHOOSE', font=('helvetica', 90, 'bold'), bg='#313131', fg='white')
        choose_teamname.place(relx=0.5, rely=0.23, anchor='center')
        # PAGE TITLE
        choose_teamname2 = Label(teamname_frame, text="YOUR TEAM NAME", font=fontmed,fg=textteamone,bg=background)
        choose_teamname2.place(relx=0.5, rely=0.36, anchor='center')
        # TEAM NAME SELECTION FIELD
        teamname_entry = Entry(teamname_frame, highlightbackground=bghighlight, font=fontmed)
        teamname_entry.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.1, anchor='center')
        # CONFIRM NAME BUTTON
        teamname_submit_btn = Button(teamname_frame, text='SUBMIT NAME', font=fontsmall, highlightbackground=fground, bg='white',
                                     fg=textbg, command=lambda: self.request_teamname(teamroster_frame, teamname_entry))
        teamname_submit_btn.place(relx=0.5, rely=0.62, relwidth=0.3, relheight=0.09, anchor='center')

        # -------- Frame 3 - PLAYER SELECT --------------------------------------------------------------------
        # HEADER
        team_select_label = Label(teamroster_frame, text="Player selection".upper(), font=font_large, fg='white', bg=background)
        team_select_label.place(relx=0.5, y=60, anchor="center")
        team_vs_label = Label(teamroster_frame, text='VS.'.upper(), font=font_large, fg=text_white,bg=background)
        team_vs_label.place(x=width/2, anchor="center", y=165)

        # TEAM 1
        y_base = 300
        y_plus = 70
        teamonename_label = Label(teamroster_frame, textvariable=self.vars.get("team name"), font=font_large, fg=textteamone,bg=background)
        teamonename_label.place(x=50, y=125)
        teamone_credits_label = Label(teamroster_frame, textvariable=self.vars.get("team credits"), font=fontmed, fg=textteamone, bg=background)
        teamone_credits_label.place(x=50, y=y_base - 90)
        top_label_teamone = Label(teamroster_frame, textvariable=self.vars.get("team TOP"), font=fontsmall, fg=text_white, bg=background)
        top_label_teamone.place(x=50, y=y_base)
        jngl_label_teamone = Label(teamroster_frame, textvariable=self.vars.get("team JUNGLE"), font=fontsmall, fg=text_white, bg=background)
        jngl_label_teamone.place(x=50, y=y_base + y_plus)
        mid_label_teamone = Label(teamroster_frame, textvariable=self.vars.get("team MID"), font=fontsmall, fg=text_white, bg=background)
        mid_label_teamone.place(x=50, y=y_base + y_plus * 2)
        adc_label_teamone = Label(teamroster_frame, textvariable=self.vars.get("team ADC"), font=fontsmall, fg=text_white, bg=background)
        adc_label_teamone.place(x=50, y=y_base + y_plus * 3)
        sup_label_teamone = Label(teamroster_frame, textvariable=self.vars.get("team SUPPORT"), font=fontsmall, fg=text_white, bg=background)
        sup_label_teamone.place(x=50, y=y_base + y_plus * 4)

        # TEAM 2
        t2x = 900
        teamtwoname_label = Label(teamroster_frame, textvariable=self.vars.get("enemy team name"), font=font_large, fg=textteamtwo,bg=background)
        teamtwoname_label.place(x=t2x,y=125)
        teamtwo_credits_label = Label(teamroster_frame, textvariable=self.vars.get("enemy team credits"), font=fontmed, fg=textteamtwo, bg=background)
        teamtwo_credits_label.place(x=t2x, y=y_base - 90)
        top_label_teamtwo = Label(teamroster_frame, textvariable=self.vars.get("enemy TOP"), font=fontsmall, fg=text_white, bg=background)
        top_label_teamtwo.place(x=t2x, y=y_base)
        jngl_label_teamtwo = Label(teamroster_frame, textvariable=self.vars.get("enemy JUNGLE"), font=fontsmall, fg=text_white, bg=background)
        jngl_label_teamtwo.place(x=t2x, y=y_base + y_plus)
        mid_label_teamtwo = Label(teamroster_frame, textvariable=self.vars.get("enemy MID"), font=fontsmall, fg=text_white, bg=background)
        mid_label_teamtwo.place(x=t2x, y=y_base + y_plus * 2)
        adc_label_teamtwo = Label(teamroster_frame, textvariable=self.vars.get("enemy ADC"), font=fontsmall, fg=text_white, bg=background)
        adc_label_teamtwo.place(x=t2x, y=y_base + y_plus * 3)
        sup_label_teamtwo = Label(teamroster_frame, textvariable=self.vars.get("enemy SUPPORT"), font=fontsmall, fg=text_white, bg=background)
        sup_label_teamtwo.place(x=t2x, y=y_base + y_plus * 4)

        # MIDDLE SECTION
        midx = 450
        player_search = Entry(teamroster_frame, font =fontsmall,highlightbackground=background, width=10)
        player_search.place(x=midx, y=230)
        self.player_box = Listbox(teamroster_frame, font=font_mini,width=20,height=15)
        self.player_box.place(x=midx,y=280)
        search_btn = Button(teamroster_frame, text='SEARCH', font=font_mini, fg=textbg, bg='white', highlightbackground=background,
                            command=lambda: self.get_laners(player_search))
        search_btn.place(x=midx+290, y=255, anchor='center')
        pick_btn = Button(teamroster_frame, text='CONFIRM', font=font_mini, fg=textbg, bg='white', highlightbackground=background,
                          command=lambda: self.request_player())
        pick_btn.place(x=width/2+50, y=618)

        stat1_label = Label(teamroster_frame, textvariable=self.vars.get("player name"),font=font_mini, bg=background, fg=text_white)
        stat1_label.place(x=width/2+50, y=300)
        stat1_label = Label(teamroster_frame, textvariable=self.vars.get("player lane"), font=font_mini, bg=background, fg=text_white)
        stat1_label.place(x=width/2+50, y=350)
        stat2_label = Label(teamroster_frame, textvariable=self.vars.get("player winrate"), font=font_mini, bg=background, fg=text_white)
        stat2_label.place(x=width/2+50, y=350+50)
        stat3_label = Label(teamroster_frame, textvariable=self.vars.get("player kda"), font=font_mini, bg=background, fg=text_white)
        stat3_label.place(x=width/2+50, y=350+100)
        stat4_label = Label(teamroster_frame, textvariable=self.vars.get("player price"), font=font_mini, bg=background, fg=text_white)
        stat4_label.place(x=width/2+50, y=350+150)
        stat5_label = Label(teamroster_frame, textvariable=self.vars.get("player rating"), font=font_mini, bg=background, fg=text_white)
        stat5_label.place(x=width/2+50, y=350+150)
        stat6_label = Label(teamroster_frame, textvariable=self.vars.get("player dmgPercent"), font=font_mini, bg=background, fg=text_white)
        stat6_label.place(x=width/2+50, y=350+200)

        # -------- Frame 4 - MATCH PAGE --------------------------------------------------------------------------------
        teamselect_label = Label(self.combat_log_frame, text="MATCH".upper(), font=font_large, fg='white', bg=background)
        teamselect_label.place(relx=0.5, y=60, anchor="center")
        teamvs_label = Label(self.combat_log_frame, text='VS.'.upper(), font=font_large, fg=text_white, bg=background)
        teamvs_label.place(x=width/2, anchor="center", y=165)
        teamonename_label = Label(self.combat_log_frame, textvariable=self.vars.get("team name"), font=font_large, fg=textteamone, bg=background)
        teamonename_label.place(x=50, y=125)
        teamtwoname_label = Label(self.combat_log_frame, textvariable=self.vars.get("enemy team name"), font=font_large, fg=textteamtwo, bg=background)
        teamtwoname_label.place(x=t2x, y=125)

        self.combat_log_box = Listbox(self.combat_log_frame, width=100, height=23, bg='grey', fg=text_white)
        self.combat_log_box.place(relx=0.5, y=450, anchor='center')

        self.show_frame(start_frame)

