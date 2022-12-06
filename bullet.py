import math

import pygame

import functions

bulletList = []
icon2 = pygame.image.load("bullet.png")

def get_bullets():
    allBullets = ""

    for bullet in bulletList:
        x = bullet.bulletX
        y = bullet.bulletY
        r = bullet.rot
        allBullets = allBullets + "," + str(x) + "," + str(y) + "," + str(r)

    allBullets = allBullets.replace(",", "", 1)

    return allBullets

class bullet:

    def __init__(self, X, Y, rot, player):
        self.rot = rot
        self.bulletX = (X - math.sin(rot) * 49) + 35
        self.bulletY = (Y - math.cos(rot) * 49) + 36
        self.player = player

        self.bulletX_change = math.sin(self.rot) * 9
        self.bulletY_change = math.cos(self.rot) * 9

        self.bounced = False

        orig_rect = icon2.get_rect()
        self.rot_image = pygame.transform.rotate(icon2, math.degrees(rot))
        rot_rect = orig_rect.copy()
        rot_rect.center = self.rot_image.get_rect().center
        self.rot_image = self.rot_image.subsurface(rot_rect).copy()

    def update_bullet(self):
        self.bulletX -= self.bulletX_change
        self.bulletY -= self.bulletY_change

        # delete bullet if out of map

        if functions.get_map(int((self.bulletY + 10) / 96), int(self.bulletX / 96)) == 1 or functions.get_map(
                int((self.bulletY + 10) / 96), int((self.bulletX + 25) / 96)) == 1:
            if self.bounced:
                bulletList.remove(self)
            self.rot_image = pygame.transform.flip(self.rot_image,True,False)

            self.bulletX_change = -self.bulletX_change
            self.bounced = True

        elif functions.get_map(int(self.bulletY / 96), int((self.bulletX + 10) / 96)) == 1 or functions.get_map(
                int((self.bulletY + 25) / 96), int((self.bulletX + 10) / 96)) == 1:
            if self.bounced:
                bulletList.remove(self)

            self.rot_image = pygame.transform.flip(self.rot_image, False, True)
            self.bulletY_change = -self.bulletY_change
            self.bounced = True

        if self.bulletY >= 1000 or self.bulletY <= 0 or self.bulletX <= 0 or self.bulletX >= 1880:
            bulletList.remove(self)

#    def render_bullet(self):

