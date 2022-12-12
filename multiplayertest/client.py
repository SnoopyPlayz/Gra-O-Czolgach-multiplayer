import socket

HEADER = 64
PORT = 5050
FORMAT = int
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "127.0.1.1"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
print(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = int(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send(67)
input()
send(67)
input()
send("Hello Tim!")

send(DISCONNECT_MESSAGE)
