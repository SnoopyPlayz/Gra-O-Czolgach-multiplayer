import socket
import threading

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv.bind((socket.gethostbyname(socket.gethostname()), 5050))
FORMAT = 'utf-8'
print("server się włancza")


class server:
    current_players = 0
    #        |gracz            |bullet
    gracz1 = "1,-100,-100,4,0,0/1"
    gracz2 = "1,-100,-100,4,0,0/1"
    gracz3 = "1,-100,-100,4,0,0/1"
    gracz4 = "1,-100,-100,4,0,0/1"


def handle_client(conn,addr):

    server.current_players += 1
    Tplayer = server.current_players


    while True:
        msg_length = conn.recv(64).decode(FORMAT)
        if msg_length:
            msg = conn.recv(int(msg_length)).decode(FORMAT)
            if msg == "!DISCONNECT":
                server.current_players -= 1
                #print("player left:"+str(server.current_players))
                break
            print(msg)

            if msg == "jaki_Gracz":
                conn.send(str(Tplayer).encode(FORMAT))
            else:

                if Tplayer == 1:
                    server.gracz1 = msg#.lstrip(msg[0])
                    conn.send((server.gracz2+server.gracz3+server.gracz4).encode(FORMAT))

                elif Tplayer == 2:
                    server.gracz2 = msg#.lstrip(msg[0])
                    conn.send((server.gracz1+server.gracz3+server.gracz4).encode(FORMAT))

                elif Tplayer == 3:
                    server.gracz3 = msg#.lstrip(msg[0])
                    conn.send((server.gracz1+server.gracz2+server.gracz4).encode(FORMAT))

                elif Tplayer == 4:
                    server.gracz4 = msg#.lstrip(msg[0])
                    conn.send((server.gracz1+server.gracz2+server.gracz3).encode(FORMAT))

                else:
                    conn.send("1,-100,-100,4,0,0/1".encode(FORMAT))

    conn.close()


serv.listen()
print("Server jusz czeka")

while True:
    conn, addr = serv.accept()
    print(conn)
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
    print(addr + " dołączył się")
    print("ile ludzi:  " + str(threading.active_count() - 1))
