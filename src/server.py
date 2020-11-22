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
        self.connections: [Connection] = []
        self.isRunning = True
        # Create a new thread responsible for responding to requests from clients
        self.request_responder_thread = threading.Thread(target=self.request_responder)
        self.request_responder_thread.setName(f'server request responder')
        self.request_responder_thread.start()
        # Create a thread responsible for receiving incoming connections
        self.connection_receiver_thread = threading.Thread(target=self.connection_receiver)
        self.connection_receiver_thread.setName(f'server connection-receiver')
        self.connection_receiver_thread.start()

    def send_packet(self, client, ACTION, obj=None):
        packet = pickle.dumps(Packet(ACTION, obj))
        if self.debug:
            s_print(f'Packet sent to {client.addr}')
        client.client_socket.send(packet)

    def connection_receiver(self):
        while self.isRunning:
            # Only accept two connections, then end this loop, which then ends the thread.
            if len(self.connections) < 2:
                # Accept a connection
                c, addr = self.sock.accept()
                if self.debug:
                    s_print(f'SERVER: Connection received from {addr}')
                # Receive the first packet
                packet = pickle.loads(c.recv(50000))
                # Create a connection object
                connection = Connection(c, addr)
                # Check if it actually is a request to connect, and if the same connection doens't already exist.
                if packet.ACTION == CLIENT_REQUEST_CONNECT and connection not in self.connections:
                    self.connections.append(connection)
                    # Start a thread for this new connection, responsible for receiving data from that client.
                    t = threading.Thread(target=self.on_new_client, args=(connection,))
                    t.setName(f'Server receiver thread for client on {addr}')
                    t.start()
            else:
                break

    def request_responder(self):
        while self.isRunning:
            # if the request queue has items in it
            if self.request_queue:
                # Pop the leftmost item from the double ended queue, atomic poplefts and appends
                # ensure chronological order as well as thread-safety.
                request, connection = self.request_queue.popleft()
                # Process the request
                self.perform_action(request, connection)

    def perform_action(self, packet, connection):
        enemy_connection = None
        for c in self.connections:
            if connection.addr != c.addr:  # Find the enemy team
                enemy_connection = c
        if packet.ACTION == CLIENT_REQUEST_DATABASE:
            # Team object requested
            if self.debug:
                s_print(f'SERVER: Client requested database')
            self.send_packet(connection, SERVER_UPDATE_DATABASE, self.database)
        elif packet.ACTION == CLIENT_REQUEST_TEAM_NAME:
            if connection.team is None:  # Cant request a team name if one is already there.
                connection.team = Team(packet.data)
                self.send_packet(connection, SERVER_UPDATE_TEAMS, (connection.team, enemy_connection.team))
                self.send_packet(enemy_connection, SERVER_UPDATE_TEAMS, (enemy_connection.team, connection.team))
            else:
                self.send_packet(connection, SERVER_REQUEST_DENIED, "Couldn't grant team name as team already has one")

        elif packet.ACTION == CLIENT_REQUEST_PLAYER_FOR_TEAM:
            if connection.team is not None:
                drafted_player = self.database.draft_player(packet.data)
                if drafted_player is not None:
                    connection.team.add_to_roster(drafted_player)
                    self.send_packet(connection, SERVER_UPDATE_TEAMS, (connection.team, enemy_connection.team))
                    self.send_packet(enemy_connection, SERVER_UPDATE_TEAMS, (enemy_connection.team, connection.team))
                else:
                    self.send_packet(connection, SERVER_REQUEST_DENIED, "tried to draft an already drafted player")
                    if self.debug:
                        s_print(f'{connection.team.teamname} tried to draft an already drafted player')
            else:
                self.send_packet(connection, SERVER_REQUEST_DENIED, "Tried to draft without having a team")
                if self.debug:
                    s_print(f'{connection.addr} tried to draft without having a team')
        elif packet.ACTION == CLIENT_REQUEST_MATCH:
            if connection.team.is_ready() and enemy_connection.team.is_ready():
                combat_log = start_match(connection.team, enemy_connection.team)
                self.send_packet(connection, SERVER_UPDATE_MATCH, combat_log)
                self.send_packet(enemy_connection, SERVER_UPDATE_MATCH, combat_log)
            else:
                self.send_packet(connection, SERVER_REQUEST_DENIED, "A team is lacking players")

    def on_new_client(self, connection):
        while self.isRunning:
            try:
                # Receive data from this client
                packet = connection.client_socket.recv(50000)
            except ConnectionAbortedError:
                break
            except ConnectionResetError:
                break
            try:
                unpickled_packet: Packet = pickle.loads(packet)
            except EOFError:
                break
            # Check if its a request for an exit, before appending it to the request queue.
            if unpickled_packet.ACTION == CLIENT_REQUEST_EXIT:
                # Client requested to exit
                for c in self.connections:
                    self.send_packet(c, CLIENT_REQUEST_EXIT)
                    c.client_socket.close()
                self.isRunning = False
                break
            else:
                # it isn't, so append it.
                self.request_queue.append((unpickled_packet, connection))
        connection.client_socket.close()
