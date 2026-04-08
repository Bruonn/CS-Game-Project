import pygame as py
from dataclasses import dataclass

class Player:
    '''
    creates a player with xy coordinates
    and w, h as it's width and height
    '''

    speedX, speedY = 5, 5
    collide = False
    #contructor
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.w = 50
        self.h = 50
        self.img = img
        self.coins = 0
        self.rect = (self.x, self.y, self.w, self.h)

    def draw(self, screen):
        #blit draws surface on a surface. here image surface is drawn on the screen
        screen.blit(self.img, (self.x, self.y))
        #py.draw.rect(screen, "#9e0c0c", self.rect)

    def move(self, screen, grid, event):
        r = self.y//60
        c = self.x//60
        if event.type == py.KEYDOWN:
        #keys = py.key.get_pressed() #this wil create a dictionary called keys
            if event.key == py.K_a and c - 1 >= 0 and grid[r][c-1] != 0:
                self.x -= 60
            if event.key == py.K_d and c + 1 < len(grid[0]) and grid[r][c+1] != 0:
                self.x += 60
            if event.key == py.K_w and r - 1 >= 0 and grid[r-1][c] != 0:
                self.y -= 60
            if event.key == py.K_s and r + 1 < len(grid) and grid[r+1][c] != 0:
                self.y += 60
            # if(grid[self.y//60][self.x//60] == 3):
            #     self.coins += 1
            #     grid[self.y//60][self.x//60] = 2137 #change value after collect coin so no coin farming
            self.rect = (self.x, self.y, self.w, self.h)

    def collision(self, obstacle):
        if abs(self.x - obstacle.x) < self.w:
            if abs(self.y - obstacle.y) < self.y:
                if (not Player.collide):
                    print("Collision")
                    Player.collide = True
            else:
                Player.collide = False
        else:
            Player.collide = False

#using dataclass is a standard for when the attributes/instance variables
#are staight forward
@dataclass
class Obstacle:
    x: int
    y: int
    img:any
    #to be checked how to create static variable with dataclass

    def draw(self, screen):
        screen.blit(self.img,(self.x, self.y))