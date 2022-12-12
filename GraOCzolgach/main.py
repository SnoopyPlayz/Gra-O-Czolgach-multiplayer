import math
import threading
import time
import pygame
import main

import functions

import player
import networking
from bullet import bulletList

pygame.init()
screen = pygame.display.set_mode((1920, 1010))

pygame.display.set_caption("Gra O Czolgach")
icon = pygame.image.load("res/icon.png")

pygame.display.set_icon(icon)

timePerFrame = 1000000000.0 / 60  # FPS
timePerUpdate = 1000000000.0 / 60  # UPS
previousTime = time.time_ns()
deltaF = 0
deltaU = 0

functions.updatemap(screen, open("map1.txt", "r"))

mapimage = screen.copy()


def getmapimage():
    return mapimage


def render():
    # screen.fill((50, 0, 100))

    screen.blit(getmapimage(), (0, 0))

    for bullet in bulletList:
        screen.blit(bullet.rot_image, (bullet.bulletX, bullet.bulletY))

    i = 5
    while len(networking.gracze) > i:
        x = float(networking.gracze[i - 4])
        y = float(networking.gracze[i - 3])
        rot = float(networking.gracze[i - 2])

        if rot >= 50:
            screen.blit(functions.explosion5, (x, y))
        elif rot >= 40:
            screen.blit(functions.explosion4, (x, y))
        elif rot >= 30:
            screen.blit(functions.explosion3, (x, y))
        elif rot >= 20:
            screen.blit(functions.explosion2, (x, y))
        elif rot >= 10:
            screen.blit(functions.explosion1, (x, y))

        else:
            screen.blit(functions.RedPlayerBody, (x, y))

            player2head = functions.rotate(functions.RedPlayerHead, rot)

            screen.blit(player2head, (x, y))
        i += 6

    i = 3
    while len(networking.bullets) > i:  # wyświetlanie naboje innych graczy
        # i-3 = x   i-2 = y   i-1 = rot
        # ToDO

        rot = float(networking.bullets[i - 1])
        x = float(networking.bullets[i - 3])
        y = float(networking.bullets[i - 2])
        flip = float(networking.bullets[i])

        screen.blit(pygame.transform.flip(functions.rotate(functions.bulletimage,
                                                           rot),  # rotation
                                          flip == -1, flip == 1),  # image flip
                    (x, y))  # image position

        i += 4

    player.render_player(screen)


def update():
    if threading.active_count() < 2:
        thread2 = threading.Thread(target=networking.networkloop)
        thread2.start()

    for bullet in bulletList:
        bullet.update_bullet()

    i = 3
    while len(networking.bullets) > i:  # przeczówa gdzie dalej będzie nabuj innych graczy
        # ToDO
        rot = float(networking.bullets[i - 1])
        x = float(networking.bullets[i - 3])
        y = float(networking.bullets[i - 2])
        flip = float(networking.bullets[i])

        if player.Player.playerX+90 > x > player.Player.playerX and player.Player.playerY + 90 > y > player.Player.playerY:
            player.Player.Zyje = False

        for bullet in bulletList:
            if bullet.bulletX+25 > x > bullet.bulletX and bullet.bulletY+25 > y > bullet.bulletY:
                bulletList.remove(bullet)

        if flip == -1:  # Jeśli się odbiło od prawej lub levej ściany
            networking.bullets[i - 3] = str(x + math.sin(rot) * 9)
        else:
            networking.bullets[i - 3] = str(x - math.sin(rot) * 9)

        if flip == 1:  # Jeśli się odbiło od górnej lub dolnej ściany
            networking.bullets[i - 2] = str(y + math.cos(rot) * 9)
        else:
            networking.bullets[i - 2] = str(y - math.cos(rot) * 9)

        i += 4

    player.update_player()

    # przeczówa gdzie dalej będą inni Gracze
    if functions.get_map(int((networking.gracz2Y + networking.gracz2Y_change) / 96),
                         int((networking.gracz2X + 7 + networking.gracz2X_change) / 96)) != 1 and functions.get_map(
        int((networking.gracz2Y + networking.gracz2Y_change) / 96),
        int((networking.gracz2X + 90 + networking.gracz2X_change) / 96)) != 1 and functions.get_map(
        int((networking.gracz2Y + 96 + networking.gracz2Y_change) / 96),
        int((networking.gracz2X + 7 + networking.gracz2X_change) / 96)) != 1 and functions.get_map(
        int((networking.gracz2Y + 96 + networking.gracz2Y_change) / 96),
        int((networking.gracz2X + 90 + networking.gracz2X_change) / 96)) != 1:
        networking.gracz2X = networking.gracz2X + networking.gracz2X_change
        networking.gracz2Y = networking.gracz2Y + networking.gracz2Y_change


while player.Player.running:  # loop

    currentTime = time.time_ns()
    deltaU += (currentTime - previousTime) / timePerUpdate
    deltaF += (currentTime - previousTime) / timePerFrame
    previousTime = currentTime

    if deltaU >= 1:
        deltaU -= 1
        update()

    if deltaF >= 1:
        deltaF -= 1
        render()
        pygame.display.update()
