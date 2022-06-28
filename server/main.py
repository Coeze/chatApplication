import socket
from threading import Thread
import sys
import time

## end of imports ###

### init ###

s = socket.socket()
host = socket.gethostname()
print(" server will start on host : ", host)
port = 8080
s.bind((host, port))
print("")
print(" Server done binding to host and port successfully")
print("")
print("Server is waiting for incoming connections")
print("")
s.listen(3)  # this is the number of connections the server will accept.


# print(addr, " Has connected to the server and is now online ...")
# print("")


clients_sockets = []

def handle_multiple_clients(client):
    while True:
        incoming_message = client.recv(1024)  # the number of bytes of the message to receive
        broadcast_message(incoming_message)


def receive():
    while True:
        conn, addr = s.accept()

        print(f"{addr} has joined the chat.")

        clients_sockets.append(conn)

        new_thread = Thread(target=handle_multiple_clients, args=(conn, ))
        new_thread.start()



def broadcast_message(msg):
    for client in clients_sockets:
        client.send(msg)


thread = Thread(target=receive)
thread.start()
