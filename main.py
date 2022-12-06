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
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

timePerFrame = 1000000000.0 / 60  # FPS
timePerUpdate = 1000000000.0 / 60  # UPS
previousTime = time.time_ns()
deltaF = 0
deltaU = 0

map = functions.updatemap(screen, open("map1.txt", "r"))

mapimage = screen.copy()


def getmapimage():
    return mapimage


def render():
    # screen.fill((50, 0, 100))

    screen.blit(getmapimage(), (0, 0))

    for bullet in bulletList:
        screen.blit(bullet.rot_image, (bullet.bulletX, bullet.bulletY))


    # screen.blit(icon2, (networking.gracz2X+ networking.gracz2X_change, networking.gracz2Y+ networking.gracz2Y_change))

    screen.blit(player.Player.playerImg2, (networking.gracz2X, networking.gracz2Y))

    player2head = functions.rotate(player.Player.playerImg, networking.gracz2R)

    screen.blit(player2head, (networking.gracz2X, networking.gracz2Y))

    player.render_player(screen)


def update():
    if threading.active_count() < 2:
        thread2 = threading.Thread(target=networking.networkloop)
        thread2.start()

    for bullet in bulletList:
        bullet.update_bullet()

    player.update_player()

    if functions.get_map(int((networking.gracz2Y + networking.gracz2Y_change) / 96), int((networking.gracz2X + 7 + networking.gracz2X_change) / 96)) != 1 and functions.get_map(
        int((networking.gracz2Y + networking.gracz2Y_change) / 96), int((networking.gracz2X + 90 + networking.gracz2X_change) / 96)) != 1 and functions.get_map(
        int((networking.gracz2Y + 96 + networking.gracz2Y_change) / 96), int((networking.gracz2X + 7 + networking.gracz2X_change) / 96)) != 1 and functions.get_map(
        int((networking.gracz2Y + 96 + networking.gracz2Y_change) / 96), int((networking.gracz2X + 90 + networking.gracz2X_change) / 96)) != 1:
        networking.gracz2X = networking.gracz2X + networking.gracz2X_change
        networking.gracz2Y = networking.gracz2Y + networking.gracz2Y_change


while player.Player.running:

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
