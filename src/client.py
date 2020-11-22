import socket
import pickle
import threading
from const import *
from helpers import s_print
from networking_classes import Packet
from helpers import setup_database


class Client:
    def __init__(self, port, debug):
        self.debug = debug
        if self.debug:
            s_print(f'Client initialized')
        self.sock = socket.socket()
        self.addr = ('127.0.0.1', port)  # Bind socket to localhost
        self.sock.connect(self.addr)  # Connect to that address
        self.database = setup_database() # Load data from res/data.csv into a database(ie. a collection of players
        self.team = None
        self.enemy_team = None
        self.combat_log = None
        self.isRunning = True
        self.receiverThread = threading.Thread(target=self.receiver)
        self.receiverThread.setName(f'Client Receiver on port {port}')
        self.receiverThread.start()  # Start a thread that receives data from the server

    def receiver(self):
        # while program is active
        while self.isRunning:
            try:
                # Receive serialized object
                pickled_obj = self.sock.recv(50000)
            except ConnectionAbortedError or ConnectionResetError:
                if self.debug:
                    s_print(f'CLIENT @ {self.sock.getsockname()}: Exiting')
                break
            # Deserialize object
            try:
                packet = pickle.loads(pickled_obj)
            except EOFError:
                break
            # Check what action was received
            self.receiver_handler(packet)
            if packet.ACTION == CLIENT_REQUEST_EXIT:
                if self.debug:
                    s_print(f'CLIENT @ {self.sock.getsockname()}: Exiting')
                self.isRunning = False
                break
            if self.debug:
                s_print(f'CLIENT @ {self.sock.getsockname()}: received packet from server at {self.addr}')
        self.sock.close()


    def send(self, ACTION, obj=None):
        # Make a packet. If no obj is specified, default is None, sometimes an object isn't necessary
        packet = Packet(ACTION, obj)
        # Serialize the packet
        pickled_packet = pickle.dumps(packet)
        # Send it
        self.sock.send(pickled_packet)
        if self.debug:
            s_print(f'CLIENT @ {self.sock.getsockname()}: sent packet to server at {self.addr}')

    def receiver_handler(self, packet):
        if packet.ACTION == SERVER_UPDATE_DATABASE:  # If server sent an update to the database, replace current
            self.database = packet.data

        elif packet.ACTION == SERVER_UPDATE_TEAMS:  # If server sent update to teams, replace current
            self.team = packet.data[0]
            self.enemy_team = packet.data[1]

        elif packet.ACTION == SERVER_UPDATE_MATCH:  # If server sent a combat log, replace current
            self.combat_log = packet.data
