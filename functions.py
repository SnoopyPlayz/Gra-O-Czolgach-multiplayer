import math

import pygame

grass = pygame.image.load("res/map/L1.png")
stone = pygame.image.load("res/map/L2.png")
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
            e += 1
        i += 1

    return map

def get_map(x, y):
    return int(map[x][y])

