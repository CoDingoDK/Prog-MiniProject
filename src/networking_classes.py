class Packet:
    def __init__(self, ACTION, data):
        self.ACTION = ACTION
        self.data = data


class Connection:
    def __init__(self, client_socket, addr):
        self.client_socket = client_socket
        self.addr = addr
        self.team = None

    def __eq__(self, other):
        return other.addr == self.addr

