import tkinter as tk

HEIGHT = 700
WIDTH = 800



root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='white')
canvas.pack()

frame = tk.Frame(root, bg='#80c1ff')
frame.place(relx=0.1, relwidth=0.8, rely=0.1, relheight=0.1)

button = tk.Button(frame, text="test button", bg='gray')
button.place(relx=0.1, rely=0.1, relwidth=0.25, relheight=0.8)

entry = tk.Entry(frame, bg='green')
entry.place(relx=0.4, rely=0.225, relwidth=0.55, relheight=0.6)

frame2 = tk.Frame(root, bg='light grey')
frame2.place(relx=0.1, relwidth=0.8, rely=0.25, relheight=0.7)

label = tk.Label(frame2, text="This is a label", bg='white')
label.place(relx=0.3, rely=0.05, relwidth=0.45, relheight=0.25)

root.mainloop()