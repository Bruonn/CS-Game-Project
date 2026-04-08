import pygame as py
from random import randint
'''
here we will learn how to move a pygame object or shape
1. move it and bounce off the wall
2.control movement with keyboard
'''
py.init
width, height = 600, 600
screen = py.display.set_mode((width, height))
py.display.set_caption("Movement")
clock = py.time.Clock()

run = True
#setting up the background colour

x, y = width/2, height/2
speedX, speedY = 5, 5
c = "#a1b4d6"
while run:
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False
    clock.tick(60)
    screen.fill("#ffffff")
    py.draw.rect(screen, c, (x, y, 50, 50))
    #the following code makes the shape move autonomusly
    # if x > width - 50 or x < 0:
    #     speedX = -speedX
    #     c = (randint(0,255), randint(0, 255), randint(0, 255))
    # if y > width - 50 or y < 0:
    #     speedY = -speedY
    #     c = (randint(0,255), randint(0, 255), randint(0, 255))
    # x += speedX
    # y += speedY

    #keymovement
    keys = py.key.get_pressed() #this wil create a dictionary called keys
    if keys[py.K_a] and x > 0:
        x -= speedX
    if keys[py.K_d] and x < width - 50:
        x += speedX
    if keys[py.K_w] and y > 0:
        y -= speedY
    if keys[py.K_s] and y < height - 50:
        y += speedY

    py.display.flip()
py.quit