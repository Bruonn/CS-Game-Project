import pygame as py
py.init()
width , height = 600, 600

#the below statement creates a screen of a given size
screen = py.display.set_mode((width,height))
#changing caption of the screen
py.display.set_caption("Intro to Pygame")

screen.fill("#cddee1")
run = True
#we need clock object to write efficient and resource conserving program
clock = py.time.Clock()
while run:
    #this needed to identify when quit is pressed
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False
    clock.tick(60)
    py.draw.line(screen, "#000000", (0,0), (width/2, height/2))
    py.draw.line(screen, "#ff0000", (0,600), (width/2, height/2))
    py.draw.line(screen, "#00ff00", (600,600), (width/2, height/2))
    py.draw.line(screen, "#0000ff", (600, 0), (width/2, height/2))

    py.draw.rect(screen, "#674141", ( 250, 250, 100, 100))
                                 #( x-pos, y-pos, width, height)
    py.draw.circle(screen, "#827F7F",(300,500), 75 )
    py.draw.ellipse(screen, "#ffff00",( 125, 250, 50, 100))
                    #(x0pos of top left, y-pos of top left, width, height)
    py.draw.ellipse(screen, "#ffff00",( 425, 250, 50, 100))
    py.draw.ellipse(screen, "#4b4b07",( 200, 50, 200, 100))
    py.draw.circle(screen, "#000000",(150,300),25,5)
    py.draw.circle(screen, "#000000",(450,300),25,5)
    py.display.flip()
py.quit()

