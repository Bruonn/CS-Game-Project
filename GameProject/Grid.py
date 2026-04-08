from random import randint
import pygame as py
from Player import Player, Obstacle
py.mixer.init()
dig_sound = py.mixer.Sound('Grass_dig1.ogg')
#to generalise our grid we use the followins variables
grid_r, grid_c, = 9, 9
grid = [[randint(0,4) for i in range(grid_c)]for j in range(grid_r)]
#print(grid)

#ensure starting area is always open
grid[0][0] = 1
grid[0][1] = 1 #right neighbour
grid[1][0] = 1 #bottom neighbour

for g in grid:
    print(g)



cell_size = 60 #cell size in which the player will reside
#width and height of the game layout depends on the grid and cell size
width, height = cell_size * grid_c, cell_size * grid_r
panel = 150
coins = 0
obimg = py.image.load('bark2.png')
obimg = py.transform.scale(obimg, (60,60))
bgimg = py.image.load('grass3.jpg')
bgimg = py.transform.scale(bgimg, (width, height))
img = py.image.load('unoriginal4.jpg')
img = py.transform.scale(img, (50,50))
coinimg = py.image.load('coin.png')
coinimg = py.transform.scale(coinimg, (55,55))
breakimg = py.image.load('breakblank.png')
breakimg = py.transform.scale(breakimg, (55,55))
player1 = Player(5, 5, img)
obstacleList = []
for r in range(grid_r):
    for c in range(grid_c):
        if grid[r][c] == 0:
            obstacleList.append(Obstacle(c*cell_size, r*cell_size, obimg))
# [Obstacle(r, c) if grid [r][c] for i in range(grid_r*grid_c)]

py.init()
screen = py.display.set_mode((width + panel, height))
py.display.set_caption("Creating Grid")
clock = py.time.Clock()

def draw_grid(grid:list):
    row = 0 #row of grid
    col = 0 #column of grid
    index = 0
    for i in range(grid_r*grid_c): #looping through the entire grid
        if grid[row][col] == 0: #check if the grid list has 1
            #if yes then draw the obstacle
            obstacleList[index].draw(screen)
            index += 1
        elif grid[row][col] == 5:
            screen.blit(coinimg, (col*cell_size, row*cell_size))
        elif grid[row][col] == 7:
            screen.blit(breakimg, (col*cell_size, row*cell_size))
            #py.draw.rect(screen, "#000000", (row*cell_size, col*cell_size, cell_size, cell_size))
        col += 1 #then go to the next cell
        if col == grid_c:   #if you reach the last column
            row += 1 #then we go to the next row
            col = 0 #and we reset the column to zero
        

def draw_panel(screen, coins):
    font = py.font.SysFont(None, 30)
    py.draw.rect(screen, "#000000", (width, 0, panel, height))
    textSurface = font.render(f"Coins: {player1.coins}", True, "#ffffff")
    screen.blit(textSurface, (width + 20, 40))

def dig():
    if event.type == py.KEYDOWN:
        if event.key == py.K_SPACE:
            if(grid[player1.y//60][player1.x//60] == 3):
                dig_sound.play()
                player1.coins += 1
                grid[player1.y//60][player1.x//60] = 5
            if 1<= grid[player1.y//60][player1.x//60] <= 4:
                dig_sound.play()
                grid[player1.y//60][player1.x//60] = 7
                
                

                


# r= img.get_rect()

run = True
while run:
    clock.tick(10)
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False
        player1.move(screen, grid, event)
        dig()
    screen.blit(bgimg, (0,0))
    draw_panel(screen, coins)
    
    '''
    how to draw on the screen using our grid?
    '''
    draw_grid(grid)
    player1.draw(screen)
    
    
    #r.center = (player1.x, player1.y)
    #screen.blit(img,p)
    
    py.display.flip()#update the screen

py.quit()
#make the game a rhythm game  