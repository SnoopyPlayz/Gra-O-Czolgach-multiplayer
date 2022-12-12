import math

import pygame
import player
# textury
grass = pygame.image.load("res/map/L1.png")
stone = pygame.image.load("res/map/L2.png")
bulletimage = pygame.image.load("res/bullet.png")
RedPlayerBody = pygame.image.load("res/gracz/RedPlayerBody.png")
RedPlayerHead = pygame.image.load("res/gracz/RedPlayerHead.png")
explosion1 = pygame.image.load("res/explosion/1.png")
explosion2 = pygame.image.load("res/explosion/2.png")
explosion3 = pygame.image.load("res/explosion/3.png")
explosion4 = pygame.image.load("res/explosion/4.png")
explosion5 = pygame.image.load("res/explosion/5.png")

map = [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]]

def rotate(img, rot):
    orig_rect = img.get_rect()
    rot_image = pygame.transform.rotate(img, math.degrees(rot))
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    return rot_image.subsurface(rot_rect).copy()


def updatemap(screen, mapRaw):

    i = 0
    while i < 11:
        map[i] = [c for c in mapRaw.readline()]
        e = 0
        while e < 20:
            if map[i][e] == "0":
                screen.blit(grass, (e * 96, i * 96))
            elif map[i][e] == "1":
                screen.blit(stone, (e * 96, i * 96))

            elif map[i][e] == "2":
                if player.Player.Tplayer == "1":
                    player.Player.playerX = e * 96
                    player.Player.playerY = i * 96
                screen.blit(grass, (e * 96, i * 96))

            elif map[i][e] == "3":
                if player.Player.Tplayer == "2":
                    player.Player.playerX = e * 96
                    player.Player.playerY = i * 96
                screen.blit(grass, (e * 96, i * 96))

            elif map[i][e] == "4":
                if player.Player.Tplayer == "3":
                    player.Player.playerX = e * 96
                    player.Player.playerY = i * 96
                screen.blit(grass, (e * 96, i * 96))

            elif map[i][e] == "5":
                if player.Player.Tplayer == "4":
                    player.Player.playerX = e * 96
                    player.Player.playerY = i * 96
                screen.blit(grass, (e * 96, i * 96))

            e += 1
        i += 1

    return map

def get_map(x, y):
    return int(map[x][y])

