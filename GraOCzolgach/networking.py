import socket

import bullet
import networking
import player

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

test = client.connect(ADDR)

clientreceve = "1,-100,-100,4,0,0/1"
gracz2X = -100
gracz2Y = -100
gracz2R = 0
gracz2Y_change = 0
gracz2X_change = 0

gracze = []
bullets = []


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    networking.clientreceve = client.recv(2048).decode(FORMAT)


send("jaki_Gracz")
Tplayer = clientreceve  # jaki to jest gracz


def networkloop():

    if player.Player.running:
        # wysyła wszystko o tym graczu serverowi
        send(str(Tplayer) + "," + str(player.Player.playerX) + "," + str(player.Player.playerY) + "," + str(
            player.Player.theta) + "," + str(player.Player.playerX_change) + "," + str(
            player.Player.playerY_change) + "/" + str(bullet.get_bullets() + "%"))
        #print(networking.clientreceve)

        graczeINaboje = list(map(str,networking.clientreceve.split('%')))

        # sortuje to co server prześle na naboje i na graczy
        #                player|bullets
        i = 1
        networking.bullets = []
        networking.gracze = []
        while len(graczeINaboje) > i:
            if graczeINaboje != '':

                graczetemp, bullettemp = tuple(map(str, graczeINaboje[i - 1].split('/')))
                bullettemp = list(map(str, bullettemp.split(',')))
                graczetemp = list(map(str, graczetemp.split(',')))

                e = 0
                while len(bullettemp) > e:
                    if bullettemp[e] != '':
                        networking.bullets.append(bullettemp[e])
                    e += 1

                e = 0
                while len(graczetemp) > e:
                    if graczetemp[e] != '':
                        networking.gracze.append(graczetemp[e])
                    e += 1

            i+=1


        #networking.bullets = list(map(float, networking.bullets[i - 1].split(',')))