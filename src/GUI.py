import tkinter as tk
from tkinter import *
from tkinter.font import Font


def show_frame(frame):
    frame.tkraise()


window = Tk()
width = 1280
height = 720
window.geometry('1280x720')
window.resizable(0, 0)
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

baggrund= "#313131"
fontmini = ('helvetica', 15, 'bold')
fontsmall = ('helvetica', 30, 'bold')
fontmed = ('helvetica', 45, 'bold')
fontlarge = ('helvetica', 60, 'bold')
fontdata= ('helvetica', 20, 'bold')
bghighlight = '#313131'
fground = '#313131'
texthvid = 'white'
textbg = '#313131'
textteamone = '#58C9B9'
textteamtwo = '#C65146'
f1 = Frame(window, bg=baggrund)
f2 = Frame(window, bg=baggrund)
f3 = Frame(window, bg=baggrund)
f4 = Frame(window, bg=baggrund)
f5 = Frame(window, bg=baggrund)

for frame in (f1, f2, f3, f4, f5):
    frame.grid(row=0, column=0, sticky='nsew')


# -------- Frame 1 - MAIN MENU -----------------------------------------------------------------------------------------
frame1_title = Label(f1, text="WELCOME TO\n LEAGUE SIMULATOR", fg=texthvid, bg=bghighlight,
                     font=('helvetica', 70, 'bold'))
frame1_title.place(relx=0.5, y=250, anchor='center')
frame1_PLAY = Button(f1, text='PLAY'.upper(), font=fontlarge, fg=textbg, highlightbackground=bghighlight,
                     command=lambda: show_frame(f2))
frame1_PLAY.place(relx=0.5, y=450, anchor='center')

# -------- Frame 2 - TEAM NAME SELECT ----------------------------------------------------------------------------------
teamname = ''
choose_teamname = Label(f2, text='CHOOSE', font=('helvetica', 90, 'bold'), bg='#313131', fg='white')
choose_teamname.place(relx=0.5, rely=0.23, anchor='center')
# PAGE TITLE
choose_teamname2 = tk.Label(f2, text="YOUR TEAM NAME", font=fontmed,fg=textteamone,bg=baggrund)
choose_teamname2.place(relx=0.5, rely=0.36, anchor='center')
# TEAM NAME SELECTION FIELD
teamname_entry = tk.Entry(f2, highlightbackground=bghighlight, font=fontmed)
teamname_entry.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.1, anchor='center')

# CONFIRM NAME BUTTON
teamname_submit_btn = tk.Button(f2, text='SUBMIT NAME', font=fontsmall, highlightbackground=fground, bg='white',
                                fg=textbg, command=lambda: show_frame(f3))
teamname_submit_btn.place(relx=0.5, rely=0.62, relwidth=0.3, relheight=0.09, anchor='center')
# -------- Frame 3 - PLAYER SELECT -------------------------------------------------------------------------------------
#HEADER
team_select_label = Label(f3, text="Player selection".upper(), font=fontlarge, fg='white', bg=baggrund)
team_select_label.place(relx=0.5, y=60, anchor="center")
team_vs_label = Label(f3, text='VS.'.upper(), font=fontlarge, fg=texthvid,bg=baggrund)
team_vs_label.place(x=width/2, anchor="center", y=165)

#TEAM 1
y_base = 300
y_plus=70
teamone_credits = '400'
teamone_name = 'team1'.upper()
teamonename_label = Label(f3, text=teamone_name, font=fontlarge, fg=textteamone,bg=baggrund)
teamonename_label.place(x=50, y=125)
teamone_credits_label = Label(f3, text='' + teamone_credits + '$', font=fontmed, fg=textteamone, bg=baggrund)
teamone_credits_label.place(x=50, y=y_base - 90)
top_label_teamone = Label(f3, text='TOP ', font=fontsmall, fg=texthvid, bg=baggrund)
top_label_teamone.place(x=50, y=y_base)
jngl_label_teamone = Label(f3, text='JNGL ', font=fontsmall, fg=texthvid, bg=baggrund)
jngl_label_teamone.place(x=50, y=y_base + y_plus)
mid_label_teamone = Label(f3, text='MID ', font=fontsmall, fg=texthvid, bg=baggrund)
mid_label_teamone.place(x=50, y=y_base + y_plus * 2)
adc_label_teamone = Label(f3, text='ADC ', font=fontsmall, fg=texthvid, bg=baggrund)
adc_label_teamone.place(x=50, y=y_base + y_plus * 3)
sup_label_teamone = Label(f3, text='SUPPORT ', font=fontsmall, fg=texthvid, bg=baggrund)
sup_label_teamone.place(x=50, y=y_base + y_plus * 4)
teamone_playerlist = [top_label_teamone, mid_label_teamone, jngl_label_teamone, adc_label_teamone, sup_label_teamone]


#TEAM 2
t2x = 900
teamtwo_name = 'team2'.upper()
teamtwoname_label = Label(f3, text=teamtwo_name, font=fontlarge, fg=textteamtwo,bg=baggrund)
teamtwoname_label.place(x=t2x,y=125)
teamtwo_credits_label = Label(f3, text='' + teamone_credits + '$', font=fontmed, fg=textteamtwo, bg=baggrund)
teamtwo_credits_label.place(x=t2x, y=y_base - 90)
top_label_teamtwo = Label(f3, text='TOP ', font=fontsmall, fg=texthvid, bg=baggrund)
top_label_teamtwo.place(x=t2x, y=y_base)
jngl_label_teamtwo = Label(f3, text='JNGL ', font=fontsmall, fg=texthvid, bg=baggrund)
jngl_label_teamtwo.place(x=t2x, y=y_base + y_plus)
mid_label_teamtwo = Label(f3, text='MID ', font=fontsmall, fg=texthvid, bg=baggrund)
mid_label_teamtwo.place(x=t2x, y=y_base + y_plus * 2)
adc_label_teamtwo = Label(f3, text='ADC ', font=fontsmall, fg=texthvid, bg=baggrund)
adc_label_teamtwo.place(x=t2x, y=y_base + y_plus * 3)
sup_label_teamtwo = Label(f3, text='SUPPORT ', font=fontsmall, fg=texthvid, bg=baggrund)
sup_label_teamtwo.place(x=t2x, y=y_base + y_plus * 4)
teamtwo_playerlist = [top_label_teamtwo, mid_label_teamtwo, jngl_label_teamtwo, adc_label_teamtwo, sup_label_teamtwo]


#MIDDLE SECTION
midx=450
player_search = Entry(f3, font =fontsmall,highlightbackground=baggrund, width=10)
player_search.place(x=midx, y=230)

adc_list = ['adc1', 'adc2', 'adc3']
top_list = ['top1', 'top2', 'top3']
support_list = ["support1", "support2", 'support3']
mid_list = ['mid1', 'mid2', 'mid3']
jgl_list = ['jungle1', 'jungle2', 'jungle3', 'jungle 4', 'jungle 5', 'jungle 6', 'jungle 7', 'jungle 8', 'jungle 9',
            'jungle 10', 'jungle 11']
wrong_list = ['WRONG SEARCH', 'OPTION TRY:', 'adc', 'top', 'mid', 'jungle', 'support']


def get_adc():
    if "adc" == player_search.get().lower():
        player_box.delete(0, END)
        for item in adc_list:
            player_box.insert(END, item.upper())
    elif "top" == player_search.get().lower():
        player_box.delete(0,END)
        for item in top_list:
            player_box.insert(END, item.upper())
    elif "mid" == player_search.get().lower():
        player_box.delete(0,END)
        for item in mid_list:
            player_box.insert(END, item.upper())
    elif "support" == player_search.get().lower():
        player_box.delete(0,END)
        for item in support_list:
            player_box.insert(END, item.upper())
    elif "jungle" == player_search.get().lower():
        player_box.delete(0,END)
        for item in jgl_list:
            player_box.insert(END, item.upper())
    else:
        player_box.delete(0,END)
        for item in wrong_list:
            player_box.insert(END, item.upper())


player_box = Listbox(f3, font=fontmini,width=20,height=15)
player_box.place(x=midx,y=280)
search_btn = Button(f3, text='SEARCH', font=fontmini, fg=textbg, bg='white', highlightbackground=baggrund,
                    command=lambda:get_adc())
search_btn.place(x=midx+290, y=255, anchor='center')
pick_btn = Button(f3, text='CONFIRM', font=fontmini, fg=textbg, bg='white', highlightbackground=baggrund,
                  command=lambda: show_frame(f4))
pick_btn.place(x=width/2+50, y=618)

price= '100$'
lane = 'top'
player = 'Faker'
winrate = '37%'
kda = '2.3'
rating = '1.23'
dmgPercent = '23%'

stat1_label = Label(f3, text=''+player+'\'s stats',font=fontmini, bg=baggrund, fg=texthvid)
stat1_label.place(x=width/2+50, y=300)
stat1_label = Label(f3, text='LANE: '+lane, font=fontmini, bg=baggrund, fg=texthvid)
stat1_label.place(x=width/2+50, y=350)
stat2_label = Label(f3, text='WINRATE: '+winrate, font=fontmini, bg=baggrund, fg=texthvid)
stat2_label.place(x=width/2+50, y=350+50)
stat3_label = Label(f3, text='KDA: '+kda, font=fontmini, bg=baggrund, fg=texthvid)
stat3_label.place(x=width/2+50, y=350+100)
stat4_label = Label(f3, text='PRICE: '+price, font=fontmini, bg=baggrund, fg=texthvid)
stat4_label.place(x=width/2+50, y=350+150)
stat5_label = Label(f3, text='RATING: '+rating, font=fontmini, bg=baggrund, fg=texthvid)
stat5_label.place(x=width/2+50, y=350+150)
stat6_label = Label(f3, text='DAMAGE% : '+dmgPercent, font=fontmini, bg=baggrund, fg=texthvid)
stat6_label.place(x=width/2+50, y=350+200)

# -------- Frame 4 - MATCH PAGE ----------------------------------------------------------------------------------------
teamselect_label = Label(f4, text="MATCH".upper(), font=fontlarge, fg='white', bg=baggrund)
teamselect_label.place(relx=0.5, y=60, anchor="center")
teamvs_label = Label(f4, text='VS.'.upper(), font=fontlarge, fg=texthvid, bg=baggrund)
teamvs_label.place(x=width/2, anchor="center", y=165)
teamonename_label = Label(f4, text=teamone_name, font=fontlarge, fg=textteamone, bg=baggrund)
teamonename_label.place(x=50, y=125)
teamtwoname_label = Label(f4, text=teamtwo_name, font=fontlarge, fg=textteamtwo, bg=baggrund)
teamtwoname_label.place(x=t2x, y=125)

gameplay = ['First action', 'Second action', 'Third Action', 'Something happened', 'X TEAM WON']

gamelog = Listbox(f4, width=100, height=23, bg='grey', fg=texthvid)
gamelog.place(relx=0.5, y=450, anchor='center')
for item in gameplay:
    gamelog.insert(END, item)
# -------- Frame 5 --------------------------------------------------------------------------------


show_frame(f1)
window.mainloop()

