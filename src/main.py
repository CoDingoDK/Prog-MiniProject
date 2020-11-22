import threading

from client import Client
from server import Server
from const import *
import time
from GUI import UI
from tkinter import Tk

if __name__ == "__main__":
    # Make tkinter windows
    tkinter_master1 = Tk()
    tkinter_master2 = Tk()
    port = 56005
    # Create independent Server and Client objects
    server = Server(port, debug=False)
    client1 = Client(port, debug=False)
    client2 = Client(port, debug=False)
    time.sleep(1)
    # Establish the UI for each window, and attach each client to a window
    ui1 = UI(tkinter_master1, client1, "Client A")
    ui2 = UI(tkinter_master2, client2, "Client B")

    # Ask the server to connect, and receive a database of players
    ui1.client.send(ACTION=CLIENT_REQUEST_CONNECT)
    ui2.client.send(ACTION=CLIENT_REQUEST_CONNECT)
    ui1.client.send(ACTION=CLIENT_REQUEST_DATABASE)
    ui2.client.send(ACTION=CLIENT_REQUEST_DATABASE)
    while True:
        # limit the framerate a bit, so the performance doesn't take a hit.
        time.sleep(0.1)
        try:
            ui1.update()
        except Exception:
            ui1.client.send(ACTION=CLIENT_REQUEST_EXIT)
            break
        try:
            ui2.update()
        except Exception:
            ui2.client.send(ACTION=CLIENT_REQUEST_EXIT)
            break
    # To exemplify that all threads are being properly closed down on program exit
    # the following print statement should only return the main thread, feel free to uncomment below to test it
    # time.sleep(1)
    # print(threading.enumerate())