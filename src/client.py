import socket, pickle
import threading
from const import *
from game_classes import Database, Team
from helpers import s_print
from networking_classes import Packet


class Client:
    def __init__(self, port):
        s_print(f'Client initialized')
        self.sock = socket.socket()
        self.addr = ('127.0.0.1', port)
        self.sock.connect(self.addr)
        self.database: [Database] = []
        self.team: [Team] = []
        self.enemy_team: [Team] = []
        self.ongoing_match = None
        self.match_history = None
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
                s_print(f'CLIENT @ {self.sock.getsockname()}: Exiting')
                break
            packet = pickle.loads(pickled_obj)
            self._receiver_handler(packet)
            if packet.ACTION == CLIENT_REQUEST_EXIT:
                s_print(f'CLIENT @ {self.sock.getsockname()}: Exiting')
                self.isRunning = False
                break
            s_print(f'CLIENT @ {self.sock.getsockname()}: Client received packet from server at {self.addr}')
        self.sock.close()

    def send(self, ACTION, obj=None):
        packet = Packet(ACTION, obj)
        pickled_packet = pickle.dumps(packet)
        self.sock.send(pickled_packet)
        s_print(f'CLIENT @ {self.sock.getsockname()}:: Client sent packet to server at {self.addr}')

    def _receiver_handler(self, packet):
        if packet.ACTION == SERVER_UPDATE_DATABASE:
            # Team object requested
            self.database = packet.data

        elif packet.ACTION == SERVER_UPDATE_TEAMS:
            # Team objects requested
            self.team = packet.data[0]
            self.enemy_team = packet.data[1]

        elif packet.ACTION == SERVER_UPDATE_PLAYER_FOR_TEAM:
            # Database object requested
            None
        elif packet.ACTION == SERVER_UPDATE_MATCH:
            # Match object requested
            self.ongoing_match = packet.data
