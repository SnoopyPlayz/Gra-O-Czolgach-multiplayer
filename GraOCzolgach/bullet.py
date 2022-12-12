import math

import pygame

import functions

bulletList = []


def get_bullets():  # Daje wszystkie naboje tego gracza w string

    allBullets = ""

    # x,y,rot,odbicie naboju od ściany + odbicie naboju od sufitu
    for bullet in bulletList:
        allBullets = allBullets + "," + str(bullet.bulletX) + "," + str(bullet.bulletY) + "," + str(
            bullet.rot) + "," + str(int(bullet.Lbounced + bullet.Rbounced))

    allBullets = allBullets.replace(",", "", 1)

    return allBullets


class bullet:

    def __init__(self, X, Y, rot, player):
        self.rot = rot  # rotacjia
        self.bulletX = (X - math.sin(rot) * 49) + 35
        self.bulletY = (Y - math.cos(rot) * 49) + 36
        self.player = player

        self.bulletX_change = math.sin(self.rot) * 9
        self.bulletY_change = math.cos(self.rot) * 9

        self.bounced = False
        self.Lbounced = 0
        self.Rbounced = 0

        self.rot_image = functions.rotate(functions.bulletimage, rot)

    def update_bullet(self):
        self.bulletX -= self.bulletX_change
        self.bulletY -= self.bulletY_change

        for bullet in bulletList:
            if bullet.bulletX+25 > self.bulletX > bullet.bulletX and bullet.bulletY+25 > self.bulletY > bullet.bulletY:
                bulletList.remove(self)
                bulletList.remove(bullet)

        # odbijanie od ścian
        if functions.get_map(int((self.bulletY + 10) / 96), int(self.bulletX / 96)) == 1 or functions.get_map(
                int((self.bulletY + 10) / 96), int((self.bulletX + 25) / 96)) == 1:
            if self.bounced:
                bulletList.remove(self)

            # zmienia rotacjie zdjęcia jeśli nabuj jest odbity
            self.rot_image = pygame.transform.flip(self.rot_image, True, False)

            self.Lbounced = -1
            self.bulletX_change = -self.bulletX_change
            self.bounced = True

        # odbijanie od sufitu i podłogi
        elif functions.get_map(int(self.bulletY / 96), int((self.bulletX + 10) / 96)) == 1 or functions.get_map(
                int((self.bulletY + 25) / 96), int((self.bulletX + 10) / 96)) == 1:

            if self.bounced:
                bulletList.remove(self)

            # zmienia rotacjie zdjęcia jeśli nabuj jest odbity
            self.rot_image = pygame.transform.flip(self.rot_image, False, True)

            self.Rbounced = 1
            self.bulletY_change = -self.bulletY_change
            self.bounced = True

        # usuwanie naboji jeśli poza mapą
        elif self.bulletY >= 1000 or self.bulletY <= 0 or self.bulletX <= 0 or self.bulletX >= 1880:
            bulletList.remove(self)