import socket
from threading import Thread

IP_ADDRESS = '127.0.0.1'
PORT = 8050
SERVER = NoneBUFFER_SIZE = 4096
Clients = {}

def setup():
    print('\n\n\n\n\n\n IP Messenger\n')

    global PORT
    global IP_ADDRESS
    global SERVER

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))

    SERVER.listen(100)

    print('Server is Waiting for Incoming Connections..')
    print('\n')

    acceptConnections()

def acceptConnections():
    global SERVER
    global clients 

    while True:
        client, addr = SERVER.accept()
        print(client.addr)

setup_thread = Thread(target = setup)
setup_thread.start()
