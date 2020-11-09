import csv
import socket, pickle, threading
from collections import deque
from uuid import getnode as get_mac
from const import *
from game_classes import *
from networking_classes import *


def _setup_database():
    with open('res/data.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        array = []
        for row in csv_reader:
            # print(\nf'Column names are {", ".join(row)}')
            array.append(
                Player(row["Player"], row["Position"], row["Games"], row["Win rate"], row["KDA"], row["CSM"],
                       row["GPM"],
                       row["KP%"], row["DMG%"]))
            # print(\narray[line_count])
        # print(\nf'Processed {line_count} lines.')
        return Database(array)


def send_packet(client, ACTION, obj=None):
    packet = pickle.dumps(Packet(ACTION, obj))
    print(f'\nPacket sent to {client.addr}')

    client.client_socket.send(packet)


class Server:
    def __init__(self, port):
        print("\nSERVER: server Initialized")
        self.request_queue = deque()
        self.sock = socket.socket()
        self.addr = ('127.0.0.1', port)
        self.sock.bind(('', port))
        self.sock.listen(5)
        self.database: Database = _setup_database()
        self.clients: [Connection] = []
        self.isRunning = True
        self.responseThread = threading.Thread(target=self.responder)
        self.responseThread.start()
        self.receiverThread = threading.Thread(target=self.receiver)
        self.receiverThread.setName(f'server receiver on port {port}')
        self.receiverThread.start()

    def receiver(self):
        while self.isRunning:
            if len(self.clients) < 2:
                c, addr = self.sock.accept()
                print(f'\nSERVER: Connection received from {addr}')
                packet = pickle.loads(c.recv(50000))
                client = Connection(c, addr)
                if packet.ACTION == CLIENT_REQUEST_CONNECT and client not in self.clients:
                    # Client requested to connect
                    self.clients.append(client)
                    t = threading.Thread(target=self._on_new_client, args=(client,))
                    t.setName(f'Server connection receiver thread for client on {addr}')
                    t.start()
                    print(f'\nSERVER: Client added, total amount of clients is now {len(self.clients)}')

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
            print(f'\nSERVER: Client requested database')
            for c in self.clients:
                send_packet(c, SERVER_UPDATE_DATABASE, self.database)

        elif packet.ACTION == CLIENT_REQUEST_TEAM_NAME:
            if client.team is None:  # Cant request a team name if one is already there.
                client.team = Team(packet.data)
                send_packet(client, SERVER_UPDATE_TEAMS, (client.team, enemy_client.team))
                send_packet(enemy_client, SERVER_UPDATE_TEAMS, (enemy_client.team, client.team))
            else:
                send_packet(client, SERVER_REQUEST_DENIED, "Couldn't grant team name as team already has one")

        elif packet.ACTION == CLIENT_REQUEST_PLAYER_FOR_TEAM:
            if client.team is not None:
                drafted_player = self.database.draft_player(packet.data)
                if drafted_player is not None:
                    client.team.add_to_roster(drafted_player)
                    send_packet(client, SERVER_UPDATE_TEAMS, (client.team, enemy_client.team))
                    send_packet(enemy_client, SERVER_UPDATE_TEAMS, (enemy_client.team, client.team))
                else:
                    print(f'{client.team.teamname} tried to draft an already drafted player')
            else:
                print(f'{client.addr} tried to draft without having a team')
        elif packet.ACTION == CLIENT_REQUEST_MATCH:
            # Match object requested
            None

    def _on_new_client(self, connection):
        while self.isRunning:
            try:
                packet = connection.client_socket.recv(50000)
            except ConnectionAbortedError:
                print("\nsocket closed")
                break
            unpickled_packet: Packet = pickle.loads(packet)
            if unpickled_packet.ACTION == CLIENT_REQUEST_EXIT:
                # Client requested to exit
                for c in self.clients:
                    send_packet(c, CLIENT_REQUEST_EXIT)
                    c.client_socket.close()
                self.isRunning = False
                break
            else:
                self.request_queue.append((unpickled_packet, connection))
        connection.client_socket.close()
