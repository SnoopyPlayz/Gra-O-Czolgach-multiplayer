import socket

import bullet
import networking
import player

HEADER = 64
PORT = 5555
FORMAT = 'utf-8'
SERVER = "127.0.1.1"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

test = client.connect(ADDR)

clientreceve = ""
gracz2X = 0
gracz2Y = 0
gracz2R = 0
gracz2Y_change = 0
gracz2X_change = 0
gracz2Y_bullets = [[], [], [], [], [], [], [], [], []]


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    networking.clientreceve = client.recv(2048).decode(FORMAT)


send("jaki_Gracz")
Tplayer = clientreceve  # Tplayer = jaki to jest gracz


def networkloop():
    # for bullet in bulletList:


    if player.Player.running:
        send(str(Tplayer) + "," + str(player.Player.playerX) + "," + str(player.Player.playerY) + "," + str(
            player.Player.theta) + "," + str(player.Player.playerX_change) + "," + str(
            player.Player.playerY_change) + "/" + str(bullet.get_bullets()))

        print(networking.clientreceve)

        # split player and bullets
        #                player|bullets
        networking.clientreceve, networking.gracz2Y_bullets = tuple(map(str, networking.clientreceve.split('/')))

        # split player
        g, networking.gracz2X, networking.gracz2Y, networking.gracz2R, networking.gracz2X_change, networking.gracz2Y_change = tuple(map(float, networking.clientreceve.split(',')))
