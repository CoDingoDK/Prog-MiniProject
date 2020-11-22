import socket
import pickle
import threading
from const import *
from game_classes import *
from helpers import s_print
from networking_classes import Packet
from helpers import setup_database
class Client:
    def __init__(self, port, debug):
        self.debug = debug
        if self.debug:
            s_print(f'Client initialized')
        self.sock = socket.socket()
        self.addr = ('127.0.0.1', port)
        self.sock.connect(self.addr)
        self.database = setup_database()
        self.team = None
        self.enemy_team = None
        self.combat_log = None
        self.isRunning = True
        self.receiverThread = threading.Thread(target=self.receiver)
        self.receiverThread.setName(f'Client Receiver on port {port}')
        self.receiverThread.start()

    def receiver(self):
        while self.isRunning:
            try:
                pickled_obj = self.sock.recv(50000)
            except ConnectionAbortedError:
                break
            except ConnectionResetError:
                if self.debug:
                    s_print(f'CLIENT @ {self.sock.getsockname()}: Exiting')
                break
            packet = pickle.loads(pickled_obj)
            self._receiver_handler(packet)
            if packet.ACTION == CLIENT_REQUEST_EXIT:
                if self.debug:
                    s_print(f'CLIENT @ {self.sock.getsockname()}: Exiting')
                self.isRunning = False
                break
            if self.debug:
                s_print(f'CLIENT @ {self.sock.getsockname()}: received packet from server at {self.addr}')
        self.sock.close()

    def send(self, ACTION, obj=None):
        packet = Packet(ACTION, obj)
        pickled_packet = pickle.dumps(packet)
        self.sock.send(pickled_packet)
        if self.debug:
            s_print(f'CLIENT @ {self.sock.getsockname()}: sent packet to server at {self.addr}')

    def _receiver_handler(self, packet):
        if packet.ACTION == SERVER_UPDATE_DATABASE:
            self.database = packet.data

        elif packet.ACTION == SERVER_UPDATE_TEAMS:
            self.team = packet.data[0]
            self.enemy_team = packet.data[1]

        elif packet.ACTION == SERVER_UPDATE_MATCH:
            self.combat_log = packet.data
