import math
import threading

import pygame

import bullet
import functions
import main
from networking import send

from bullet import bulletList

class Player:
    playerImg = pygame.image.load("res/gracz/graczHead.png")
    playerImg2 = pygame.image.load("res/gracz/graczBody.png")
    playerX = 12
    playerY = 400
    playerX_change = 0
    playerY_change = 0
    theta = 0
    timerBullet = 0
    currentBullets = 0
    running = True


def update_player():
    Player.timerBullet += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Player.running = False
            while True:
                if threading.active_count() < 2:
                    send("!DISCONNECT")
                    break

        # default 30
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] and Player.timerBullet > 18:
            for bullet1 in bulletList:
                if bullet1.player == 1:
                    Player.currentBullets += 1

            if Player.currentBullets < 3:
                bullet.bulletList.append(bullet.bullet(Player.playerX, Player.playerY, Player.theta, 1))
            Player.timerBullet = 0
            Player.currentBullets = 0
        # default 2
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a: Player.playerX_change -= 3.3
            if event.key == pygame.K_d: Player.playerX_change += 3.3
            if event.key == pygame.K_s: Player.playerY_change += 3.3
            if event.key == pygame.K_w: Player.playerY_change -= 3.3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a: Player.playerX_change += 3.3
            if event.key == pygame.K_d: Player.playerX_change -= 3.3
            if event.key == pygame.K_s: Player.playerY_change -= 3.3
            if event.key == pygame.K_w: Player.playerY_change += 3.3
    if functions.get_map(int((Player.playerY + Player.playerY_change) / 96), int((Player.playerX + 7) / 96)) != 1 and functions.get_map(
            int((Player.playerY + Player.playerY_change) / 96), int((Player.playerX + 90) / 96)) != 1 and functions.get_map(
            int((Player.playerY + 96 + Player.playerY_change) / 96), int((Player.playerX + 7) / 96)) != 1 and functions.get_map(
            int((Player.playerY + 96 + Player.playerY_change) / 96), int((Player.playerX + 90) / 96)) != 1:
        Player.playerY += Player.playerY_change

    if functions.get_map(int(Player.playerY / 96), int((Player.playerX + 7 + Player.playerX_change) / 96)) != 1 and functions.get_map(
            int(Player.playerY / 96), int((Player.playerX + 90 + Player.playerX_change) / 96)) != 1 and functions.get_map(
            int((Player.playerY + 96) / 96), int((Player.playerX + 7 + Player.playerX_change) / 96)) != 1 and functions.get_map(
            int((Player.playerY + 96) / 96), int((Player.playerX + 90 + Player.playerX_change) / 96)) != 1:
        Player.playerX += Player.playerX_change


def render_player(screen):  # render player
    x, y = pygame.mouse.get_pos()  # pozycjia kursora

    Player.theta = math.atan2(y - Player.playerY - 48, Player.playerX + 48 - x)
    Player.theta += 3.14159265358979323846 / 2.0

    rot_image = functions.rotate(Player.playerImg,Player.theta)

    screen.blit(Player.playerImg2, (Player.playerX, Player.playerY))

    screen.blit(rot_image, (Player.playerX, Player.playerY))

