import pickle
import socket
import threading
from collections import deque
from const import *
from game_classes import *
from helpers import s_print, setup_database
from networking_classes import *
from match import start_match

class Server:
    def __init__(self, port, debug):
        self.debug = debug
        if self.debug:
            s_print("SERVER: server Initialized")
        self.request_queue = deque()
        self.sock = socket.socket()
        self.addr = ('127.0.0.1', port)
        self.sock.bind(('', port))
        self.sock.listen(5)
        self.database: Database = setup_database()
        self.clients: [Connection] = []
        self.isRunning = True
        self.responderThread = threading.Thread(target=self.responder)
        self.responderThread.setName(f'server responder thread')
        self.responderThread.start()
        self.receiverThread = threading.Thread(target=self.receiver)
        self.receiverThread.setName(f'server connection-establisher thread')
        self.receiverThread.start()

    def send_packet(self,client, ACTION, obj=None):
        packet = pickle.dumps(Packet(ACTION, obj))
        if self.debug:
            s_print(f'Packet sent to {client.addr}')

        client.client_socket.send(packet)

    def receiver(self):
        while self.isRunning:
            if len(self.clients) < 2:
                c, addr = self.sock.accept()
                if self.debug:
                    s_print(f'SERVER: Connection received from {addr}')
                packet = pickle.loads(c.recv(50000))
                client = Connection(c, addr)
                if packet.ACTION == CLIENT_REQUEST_CONNECT and client not in self.clients:
                    # Client requested to connect
                    self.clients.append(client)
                    t = threading.Thread(target=self._on_new_client, args=(client,))
                    t.setName(f'Server receiver thread for client on {addr}')
                    t.start()
            else:
                break

    def responder(self):
        while self.isRunning:
            if self.request_queue:
                request, connection = self.request_queue.popleft()
                self._perform_action(request, connection)

    def _perform_action(self, packet, client):
        enemy_client = None
        for c in self.clients:
            if client.addr != c.addr:  # Find the enemy team
                enemy_client = c
        if packet.ACTION == CLIENT_REQUEST_DATABASE:
            # Team object requested
            if self.debug:
                s_print(f'SERVER: Client requested database')
            self.send_packet(c, SERVER_UPDATE_DATABASE, self.database)


        elif packet.ACTION == CLIENT_REQUEST_TEAM_NAME:
            if client.team is None:  # Cant request a team name if one is already there.
                client.team = Team(packet.data)
                self.send_packet(client, SERVER_UPDATE_TEAMS, (client.team, enemy_client.team))
                self.send_packet(enemy_client, SERVER_UPDATE_TEAMS, (enemy_client.team, client.team))
            else:
                self.send_packet(client, SERVER_REQUEST_DENIED, "Couldn't grant team name as team already has one")

        elif packet.ACTION == CLIENT_REQUEST_PLAYER_FOR_TEAM:
            if client.team is not None:
                drafted_player = self.database.draft_player(packet.data)
                if drafted_player is not None:
                    client.team.add_to_roster(drafted_player)
                    self.send_packet(client, SERVER_UPDATE_TEAMS, (client.team, enemy_client.team))
                    self.send_packet(enemy_client, SERVER_UPDATE_TEAMS, (enemy_client.team, client.team))
                else:
                    self.send_packet(client, SERVER_REQUEST_DENIED, "tried to draft an already drafted player")
                    if self.debug:
                        s_print(f'{client.team.teamname} tried to draft an already drafted player')
            else:
                self.send_packet(client, SERVER_REQUEST_DENIED, "Tried to draft without having a team")
                if self.debug:
                    s_print(f'{client.addr} tried to draft without having a team')
        elif packet.ACTION == CLIENT_REQUEST_MATCH:
            if client.team.is_ready() and enemy_client.team.is_ready():
                combat_log = start_match(client.team, enemy_client.team)
                self.send_packet(client, SERVER_UPDATE_MATCH, combat_log)
                self.send_packet(enemy_client, SERVER_UPDATE_MATCH, combat_log)
            else:
                self.send_packet(client, SERVER_REQUEST_DENIED, "A team is lacking players")

    def _on_new_client(self, connection):
        while self.isRunning:
            try:
                packet = connection.client_socket.recv(50000)
            except ConnectionAbortedError:
                break
            except ConnectionResetError:
                break
            unpickled_packet: Packet = pickle.loads(packet)
            if unpickled_packet.ACTION == CLIENT_REQUEST_EXIT:
                # Client requested to exit
                for c in self.clients:
                    self.send_packet(c, CLIENT_REQUEST_EXIT)
                    c.client_socket.close()
                self.isRunning = False
                break
            else:
                self.request_queue.append((unpickled_packet, connection))
        connection.client_socket.close()
