import socket

HOST = '127.0.0.1'  # IP SERVER
PORT = 8000         # PORT SERVER

class SocketServer:
	def start_server(self):
		self.commands = self.set_commands()

		self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket_server.bind(
			(
				HOST, PORT
			)
		)
		print(f'SERVER STARTING IN HOST {HOST} PORT {PORT}')

		self.socket_server.listen(1)
		self.listen_server()

		print(f'SERVER OFF')

	def listen_server(self):
		print('STARTING THE LISTENING SERVER')

		while True:
			conn, client = self.socket_server.accept()
			print ('CONNECTED BY', client)

			while True:
				bytes_message = conn.recv(1024)
				string_message = bytes_message.decode('utf-8')

				if string_message in self.commands:
					callback_message ='{} SEND COMMAND {} - {}'.format(
						client,
						string_message,
						self.commands[string_message]
					)
				elif string_message == '/quit':
					callback_message = 'CONNECTION TERMINATED BY {}'.format(client)
	
					print(callback_message)
					conn.sendall(bytes(callback_message.encode('utf-8')))
					break
				else:
					callback_message = '{} INVALID COMMAND {}'.format(client, string_message)

				print(callback_message)
				conn.sendall(bytes(callback_message.encode('utf-8')))

			conn.close()
			break

	def set_commands(self):
		return {
			'ligar' : 'Ligando Computador',
			'desligar' : 'Desligando Computador',
			'acender' : 'Acendendo Luz',
			'apagar' : 'Apagando Luz',
			'abrir' : 'Abrindo Janela',
			'fechar' : 'Fechando Janela'
		}

SocketServer().start_server()