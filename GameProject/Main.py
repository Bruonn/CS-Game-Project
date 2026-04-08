from Player import Player
import pygame as py
py.init
width, height = 600, 600
screen = py.display.set_mode((width, height))
py.display.set_caption("Movement")
clock = py.time.Clock()

run = True


player1 = Player(0, 0, 50, 50)

x, y = width/2, height/2
speedX, speedY = 5, 5

player2 = Player(x,  y, 50, 50)
c = "#a1b4d6"
while run:
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False
    clock.tick(60)
    screen.fill("#ffffff")
    r1 = player1.draw(screen)        #this will call the draw function from Player
    player1.move(screen)
    r2 = player2.draw(screen)
    # player1.collision(player2)
    print(r1.colliderect(r2))

    '''
    colliderect(rect) detects collision between 2 rect objects.
    it returns true or false
    '''

    py.display.flip()

py.quit()