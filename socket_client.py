import socket

HOST = '127.0.0.1'  # IP SERVER
PORT = 8000         # PORT SERVER

class SocketClient:
    def start_client(self):
        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_server.connect(
            (
                HOST, PORT
            )
        )

        print(f'CLIENT CONNECT IN SERVER HOST {HOST} PORT {PORT}')

        self.connect_server()
        
        print(f'SERVER OFF')

    def connect_server(self, message = ''):
        while message != '/quit':
            message = input("SEND MESSAGE OR /quit TO EXIT: ")
            self.socket_server.send(message.encode('utf-8'))

            bytes_received_message = self.socket_server.recv(1024)
            string_received_message = bytes_received_message.decode('utf-8')

            print(f'SERVER MESSAGE: {string_received_message}')

        self.socket_server.close()

SocketClient().start_client()