import math
import threading
import pygame
import bullet
import functions
import networking
from networking import send

from bullet import bulletList

class Player:
    Zyje = True
    Tplayer = networking.Tplayer
    playerImg = pygame.image.load("res/gracz/graczHead.png")
    playerImg2 = pygame.image.load("res/gracz/graczBody.png")
    playerX = 120
    playerY = 400
    playerX_change = 0
    playerY_change = 0
    smoke = 9
    theta = 0
    timerBullet = 0
    currentBullets = 0
    running = True


def update_player():
    if Player.Zyje:
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
    else:
        Player.smoke += 1

        Player.theta = Player.smoke

        if Player.smoke >= 60:
            Player.Zyje = True
            Player.smoke = 9



def render_player(screen):  # render player
    if Player.Zyje:
        x, y = pygame.mouse.get_pos()  # pozycjia kursora

        Player.theta = math.atan2(y - Player.playerY - 48, Player.playerX + 48 - x)
        Player.theta += 3.14159265358979323846 / 2.0

        rot_image = functions.rotate(Player.playerImg,Player.theta)

        screen.blit(Player.playerImg2, (Player.playerX, Player.playerY))

        screen.blit(rot_image, (Player.playerX, Player.playerY))
    else:
        if Player.smoke >= 50:
            screen.blit(functions.explosion5, (Player.playerX, Player.playerY))
        elif Player.smoke >= 40:
            screen.blit(functions.explosion4, (Player.playerX, Player.playerY))
        elif Player.smoke >= 30:
            screen.blit(functions.explosion3, (Player.playerX, Player.playerY))
        elif Player.smoke >= 20:
            screen.blit(functions.explosion2, (Player.playerX, Player.playerY))
        elif Player.smoke >= 10:
            screen.blit(functions.explosion1, (Player.playerX, Player.playerY))