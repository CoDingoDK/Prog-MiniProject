import threading
from game_classes import *
from client import Client
from helpers import s_print
from server import Server
from const import *
import time
import GUI
from GUI import UI
from tkinter import Tk,Toplevel

if __name__ == "__main__":
    tkinter_master1 = Tk()
    tkinter_master2 = Tk()
    port = 56005
    server = Server(port, debug=False)
    client1 = Client(port, debug=False)
    client2 = Client(port, debug=False)
    time.sleep(1)
    ui1 = UI(tkinter_master1, client1, "Client A")
    ui2 = UI(tkinter_master2, client2, "Client B")
    ui1.client.send(ACTION=CLIENT_REQUEST_CONNECT)
    ui2.client.send(ACTION=CLIENT_REQUEST_CONNECT)
    ui1.client.send(ACTION=CLIENT_REQUEST_DATABASE)
    ui2.client.send(ACTION=CLIENT_REQUEST_DATABASE)
    while True:
        time.sleep(0.1)
        ui1.update()
        ui2.update()

