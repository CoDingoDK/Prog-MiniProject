import tkinter as tk
from tkinter import *
from tkinter.font import Font



def show_frame(frame):
    frame.tkraise()



window = Tk()
window.geometry('1000x600')
window.state('zoomed')



window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
baggrund= "#313131"
fontmini = ('helvetica',15,'bold')
fontsmall = ('helvetica', 30, 'bold')
fontmed = ('helvetica', 45, 'bold')
fontlarge = ('helvetica', 75, 'bold')
fontdata= ('helvetica',20,'bold')
bghighlight = '#313131'
fground = '#313131'
texthvid = 'white'
textbg = '#313131'
textteam = '#58C9B9'
f1 = Frame(window, bg = baggrund)
f2 = Frame(window, bg = baggrund)
f3 = Frame(window, bg = baggrund)
f4 = Frame(window, bg = baggrund)
f5 = Frame(window, bg = baggrund)
f6 = Frame(window, bg = baggrund)
f7 = Frame(window, bg = baggrund)
for frame in (f1, f2, f3, f4, f5, f6, f7):
    frame.grid(row = 0, column= 0, sticky='nsew')


# -------- Frame 1 ----------
frame1_title = Label(f1, text="WELCOME TO\n LEAGUE SIMULATOR",fg =texthvid,bg = bghighlight,font=('helvetica',60,'bold'))
frame1_title.place(relx=0.155, y=100)
frame1_singleplayer = Button(f1, text='Singleplayer'.upper(),
                             font =fontmed,
                             fg = textbg,
                             highlightbackground=bghighlight,
                             command =lambda: show_frame(f2))
frame1_singleplayer.place(relx=0.3, y=325)
frame1_multiplayer = Button(f1, text='multiplayer'.upper(),
                            font =fontmed,
                            fg = textbg,
                            highlightbackground=bghighlight,
                            command =lambda: show_frame(f7))
frame1_multiplayer.place(relx=0.315, y=425)


# -------- Frame 2 ----------
teamname = ''
def potato(frame):
    global teamname
    teamname = frame2_entry.get().upper()
    frame3_title = tk.Label(f3, text='Team: '.upper()+ teamname, font=fontlarge,justify=LEFT, fg=textteam, bg=bghighlight)
    frame3_title.place(x=50, y=50)
    frame.tkraise()

frame2_choose = Label(f2, text='CHOOSE', font=('helvetica',75,'bold'),bg= '#313131',fg='white',)
frame2_choose.place(relx = 0.35, rely= 0.15)
#PAGE TITLE
frame2_title = tk.Label(f2, text="YOUR TEAM NAME", font=fontmed,fg='white',bg=baggrund)
frame2_title.place(relx=0.3, rely=0.3)
#TEAM NAME SELCETION FIELD
frame2_entry = tk.Entry(f2,highlightbackground=bghighlight)
frame2_entry.place(relx=0.26,rely=0.5, relwidth=0.5, relheight=0.1)
# CONFIRM NAME BUTTON
frame2_submitbtn = tk.Button(f2, text='SUBMIT NAME',
                       font=fontsmall,
                       highlightbackground=fground,
                       command =lambda: potato(f3),)
frame2_submitbtn.place(relx=0.356,rely=0.62, relwidth=0.3, relheight=0.09)



# -------- Frame 3 ----------

adc = ''.upper()
mid = ''.upper()
support = '' .upper()
top = ''.upper()
jungle = ''.upper()
credits = '300$'

#PLAYER LABELS
frame3_players = Label(f3,text= 'current roster'.upper(), font=fontmed,justify=LEFT,bg=baggrund, fg=texthvid)
frame3_players.place(x=50, y=180)
frame3_adc = Label(f3,text= 'adc: '.upper()+ adc, font=fontsmall,justify=LEFT,bg=baggrund, fg=texthvid)
frame3_adc.place(x=50, y=250)
frame3_support = Label(f3,text= 'Support: '.upper()+support, font=fontsmall,justify=LEFT,bg=baggrund, fg=texthvid)
frame3_support.place(x=50,y=300)
frame3_mid = Label(f3,text='mid: '.upper() +mid, font=fontsmall,bg=baggrund,justify=LEFT, fg=texthvid)
frame3_mid.place(x=50,y=350)
frame3_jungle = Label(f3,text='jungle: '.upper() + jungle, font=fontsmall,justify=LEFT,bg=baggrund, fg=texthvid)
frame3_jungle.place(x=50,y=400)
frame3_top = Label(f3,text= 'top: '.upper() + top, font=fontsmall,justify=LEFT,bg=baggrund, fg=texthvid)
frame3_top.place(x=50,y=450)

roles = [frame3_adc, frame3_support, frame3_mid, frame3_jungle, frame3_top]
#BUTTONS
buttonx = 600
frame3_credits = Label(f3,text= 'credits: '.upper() + credits, font=fontsmall,justify=LEFT,bg=baggrund, fg=textteam)
frame3_credits.place(x=buttonx,y=195)
frame3_training = tk.Button(f3, text='Training'.upper(),font=fontmed,justify=LEFT,bg=baggrund, fg=textbg,highlightbackground=bghighlight,command =lambda: show_frame(f4))
frame3_training.place(x=buttonx,y=250)
frame3_shop = tk.Button(f3, text='player shop'.upper(),font=fontmed,justify=LEFT,bg=baggrund, fg=textbg,highlightbackground=bghighlight,command =lambda: show_frame(f5))
frame3_shop.place(x=buttonx,y=320)
frame3_tournament = tk.Button(f3, text='tournament'.upper(),font=fontmed,justify=LEFT,bg=baggrund, fg=textbg,highlightbackground=bghighlight,command =lambda: show_frame(f6))
frame3_tournament.place(x=buttonx,y=390)
frame3_mainmenu = tk.Button(f3, text='main menu'.upper(),font=fontmed,justify=LEFT,bg=baggrund, fg=textbg,highlightbackground=bghighlight,command =lambda: show_frame(f2))
frame3_mainmenu.place(x=buttonx,y=460)


# -------- Frame 4 ----------
frame4_title = tk.Label(f4, text='training'.upper(), font=fontlarge,bg= bghighlight,fg=texthvid)
frame4_title.pack(fill='x')
frame4_btn = tk.Button(f4, text='home'.upper(),font=fontsmall,justify=LEFT,bg=baggrund, fg=textbg,highlightbackground=bghighlight,command =lambda: show_frame(f3))
frame4_btn.place(x=10, y=16)

# -------- Frame 5 Shop ----------

#TITLE
frame4_title = tk.Label(f5, text='shop'.upper(), font=fontlarge,bg= baggrund,fg=texthvid)
frame4_title.place(x=400, y=10)
frame4_btn = tk.Button(f5, text='home'.upper(),font=fontsmall,justify=LEFT,bg=baggrund, fg=textbg,highlightbackground=bghighlight,command =lambda: show_frame(f3))
frame4_btn.place(x=10, y=16)

#MIDDLE BOX SECTION
my_listbox = Listbox(f5, width=15, height= 12, font=fontsmall)
my_listbox.place(x=380,y=150)
adclist = ['adc1', 'adc2', 'adc3']
toplist = ['top1', 'top2', 'top3']
supportlist = ["support1", "support2", 'support3']
midlist = ['mid1','mid2','mid3']
junglelist = ['jungle1','jungle2','jungle3','jungle 4', 'jungle 5', 'jungle 6', 'jungle 7','jungle 8', 'jungle 9', 'jungle 10', 'jungle 11']


def getadc():
    my_listbox.delete(0, END)
    for item in adclist:
        my_listbox.insert(END, item.upper())


def gettop():
    my_listbox.delete(0, END)
    for item in toplist:
        my_listbox.insert(END, item.upper())


def getsupport():
    my_listbox.delete(0, END)
    for item in supportlist:
     my_listbox.insert(END, item.upper())


def getmid():
    my_listbox.delete(0, END)
    for item in midlist:
        my_listbox.insert(0, item.upper())


def getjungle():
    my_listbox.delete(0, END)
    for item in junglelist:
        my_listbox.insert(END, item.upper())

#LEFT SIDE MENU
btnx= 60
searchlabel = Label(f5, text='SEARCH FOR', font = fontsmall, fg= texthvid, bg= baggrund)
searchlabel.place(x=50, y=150)

searchbtn_adc = Button(f5, text="ADC", font=fontsmall, highlightbackground= bghighlight, command=lambda: getadc())
searchbtn_adc.place(x=btnx+40,y=200)
searchbtn_top = Button(f5, text="TOP", font=fontsmall,highlightbackground= bghighlight, command=lambda: gettop())
searchbtn_top.place(x=btnx+40,y=260)
searchbtn_support = Button(f5, text="SUPPORT", font=fontsmall, highlightbackground= bghighlight, command=lambda: getsupport())
searchbtn_support.place(x=btnx,y=320)
searchbtn_mid = Button(f5, text="MID", font=fontsmall, highlightbackground= bghighlight, command=lambda: getmid())
searchbtn_mid.place(x=btnx+40,y=380)
searchbtn_jungle = Button(f5, text="JUNGLE", font=fontsmall, highlightbackground= bghighlight, command=lambda: getjungle())
searchbtn_jungle.place(x=btnx+10,y=440)

#RIGHT SIDE MENU
datalabel = Label(f5, text='player stats'.upper(), font = fontsmall, fg= texthvid, bg= baggrund)
datalabel.place(x=700, y=150)
data1, data2, data3, data4, data5, data6 = '1.000$', '2', '3', '4', '5', '6'

data1label = Label(f5, text='rating : '.upper() +data1, font = fontdata, fg= texthvid, bg= baggrund)
data1label.place(x=700, y=200)
data2label = Label(f5, text='kda: '.upper()+ data2, font = fontdata, fg= texthvid, bg= baggrund)
data2label.place(x=700, y=250)
data3label = Label(f5, text='winrate: '.upper()+ data3, font = fontdata, fg= texthvid, bg= baggrund)
data3label.place(x=700, y=300)
data4label = Label(f5, text='kp %: '.upper()+ data4, font = fontdata, fg= texthvid, bg= baggrund)
data4label.place(x=700, y=350)
data5label = Label(f5, text='dmg %: '.upper()+ data5, font = fontdata, fg= texthvid, bg= baggrund)
data5label.place(x=700, y=400)
data6label = Label(f5, text='Gold per min: '.upper()+ data6, font = fontdata, fg= texthvid, bg= baggrund)
data6label.place(x=700, y=450)

#BUY BUTTON

def buyplayer(frame):
    x = my_listbox.get(ANCHOR)
    if supportlist.__contains__(my_listbox.get(ANCHOR).lower()):
        frame3_support.config(text='SUPPORT: '.upper() +my_listbox.get(ANCHOR))
        frame.tkraise()
    elif adclist.__contains__(my_listbox.get(ANCHOR).lower()):
        frame3_adc.config(text='ADC: '.upper() +my_listbox.get(ANCHOR))
        frame.tkraise()
    elif toplist.__contains__(my_listbox.get(ANCHOR).lower()):
        frame3_top.config(text='TOP: '.upper() + my_listbox.get(ANCHOR))
        frame.tkraise()
    elif midlist.__contains__(my_listbox.get(ANCHOR).lower()):
        frame3_mid.config(text='MID: '.upper() + my_listbox.get(ANCHOR))
        frame.tkraise()
    elif junglelist.__contains__(my_listbox.get(ANCHOR).lower()):
        frame3_jungle.config(text='JUNGLE: '.upper() + my_listbox.get(ANCHOR))
        frame.tkraise()

buybutton = Button(f5, text='BUY PLAYER', font=('helvetica',35,'bold'), highlightbackground=bghighlight,fg=textbg,
                   command=lambda: buyplayer(f3))
buybutton.place(x=700, y=500)

# -------- Frame 6 Tournament ----------
frame4_title = tk.Label(f6, text='tournament'.upper(), font=fontlarge,bg= baggrund,fg=textbg)
frame4_title.pack(fill='x')
frame4_btn = tk.Button(f6, text='home'.upper(),font=fontsmall,justify=LEFT,bg=baggrund, fg=textbg,highlightbackground=bghighlight,command =lambda: show_frame(f3))
frame4_btn.place(x=10, y=16)

# -------- Frame 7 Multiplayer ----------
frame4_title = tk.Label(f7, text='multiplayer'.upper(), font=fontlarge,bg= baggrund,fg=texthvid)
frame4_title.pack(fill='x')
frame4_btn = tk.Button(f7, text='back'.upper(),font=fontsmall,justify=LEFT,bg=baggrund, fg=textbg,highlightbackground=bghighlight,command =lambda: show_frame(f1))
frame4_btn.place(x=10, y=16)


show_frame(f1)
window.mainloop()



#image path: /Users/kasper/Documents/GitHub/Prog-MiniProject/src/res/mirageA.jpg
