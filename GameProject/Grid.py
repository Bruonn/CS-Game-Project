from random import randint
import pygame as py
from Player import Player, Obstacle
py.mixer.init()
dig_sound = py.mixer.Sound('Grass_dig1.ogg')
#to generalise our grid we use the followins variables
grid_r, grid_c, = 9, 9
grid1 = [[randint(0,6) for i in range(grid_c)]for j in range(grid_r)]

grid2 = [[randint(20,26) for i in range(grid_c)]for j in range(grid_r)]
#print(grid)

#ensure starting area is always open
grid1[0][0] = 1
grid1[1][0] = 1 #right neighbour
grid1[0][1] = 1 #bottom neighbour
grid1[0][4] = 12
grid1[1][4] = 1
grid1[7][2] = 14
grid2[4][4] = 9
grid2[randint(0,8)][randint(0,8)] = 10
grid2[randint(0,8)][randint(0,8)] = 10
grid2[randint(0,8)][randint(0,8)] = 10
grid2[randint(0,8)][randint(0,8)] = 10
'''
create a loop which runs exactly n times
go through each row randomly pick run another loop 3 times
generate a randomnumber between 0-8
check if the index generated doesnt already contain the vaue that you want
if not then change the value otherwise restart the loop

'''

for g in grid1:
    print(g)

for h in grid2:
    print(h)


notecount = 0
for i in grid2:
    for j in i:
        if j == 10:
            notecount += 1

keycount = 0
for t in grid1:
    for n in t:
        if n == 14:
            keycount += 1




cell_size = 60 #cell size in which the player will reside
#width and height of the game layout depends on the grid and cell size
width, height = cell_size * grid_c, cell_size * grid_r
panel = 150
coins = 0
notes = 0
code = 0
key = 0
hole = py.image.load('hole.jpg')
hole = py.transform.scale(hole, (60,60))
noteimg = py.image.load('noteplaceholder.jfif')
noteimg = py.transform.scale(noteimg, (60,60))
lockimg = py.image.load('lockplaceholder.jfif')
lockimg = py.transform.scale(lockimg, (60,60))
obimg = py.image.load('backwall.jfif')
obimg = py.transform.scale(obimg, (60,60))
bgimg = py.image.load('carpet-yellow.jpg')
bgimg = py.transform.scale(bgimg, (width, height))
bgimg2 = py.image.load('grass.jpg')
bgimg2 = py.transform.scale(bgimg2, (width, height))
img = py.image.load('unoriginal4.jpg')
img = py.transform.scale(img, (50,50))
coinimg = py.image.load('notZeldaRupee.png')
coinTextimg = py.transform.scale(coinimg, (30,30))
coinimg = py.transform.scale(coinimg, (55,55))
openimg = py.image.load('dooropen.png')
openimg = py.transform.scale(openimg, (60,60))
breakimg = py.image.load('breakblank.png')
breakimg = py.transform.scale(breakimg, (55,55))
player1 = Player(5, 5, img)
# player2 = Player(5, 5, hidecoinimg)
exitimg = py.image.load('door.png')
exitimg = py.transform.scale(exitimg, (60,60))
key = py.image.load('key.jpg.pdf.jfif.jpeg.webp.heif')
key = py.transform.scale(key,(55,55))
obstacleList = []
for r in range(grid_r):
    for c in range(grid_c):
        if grid1[r][c] == 0 or grid1[r][c] == 2:
            obstacleList.append(Obstacle(c*cell_size, r*cell_size, obimg))
# [Obstacle(r, c) if grid [r][c] for i in range(grid_r*grid_c)]

py.init()
screen = py.display.set_mode((width + panel, height))
py.display.set_caption("game")
clock = py.time.Clock()

def draw_grid(grid:list):
    row = 0 #row of grid
    col = 0 #column of grid
    index = 0
    for i in range(grid_r*grid_c): #looping through the entire grid
        if grid[row][col] == 0 or grid[row][col] == 2: #check if the grid list has 1
            #if yes then draw the obstacle
            obstacleList[index].draw(screen)
            index += 1
        elif grid[row][col] == 3:
            screen.blit(coinimg, (col*cell_size, row*cell_size))
        elif grid[row][col] == 12:
            screen.blit(exitimg, (col*cell_size, row*cell_size))
        elif grid[row][col] == 13:
            screen.blit(openimg, (col*cell_size, row*cell_size))
        elif grid[row][col] == 6:
             screen.blit(obimg,(col*cell_size, row*cell_size))
        elif grid[row][col] == 14:
             screen.blit(key,(col*cell_size, row*cell_size))
        elif grid[row][col] == 9:
             screen.blit(lockimg,(col*cell_size, row*cell_size))
        elif grid[row][col] == 10:
             screen.blit(noteimg,(col*cell_size, row*cell_size))
        elif grid[row][col] == 2137:
             screen.blit(hole,(col*cell_size, row*cell_size))
            #py.draw.rect(screen, "#000000", (row*cell_size, col*cell_size, cell_size, cell_size))
        col += 1 #then go to the next cell
        if col == grid_c:   #if you reach the last column
            row += 1 #then we go to the next row
            col = 0 #and we reset the column to zero
        

def draw_panel(screen, info, extra):
    font = py.font.SysFont(None, 30)
    py.draw.rect(screen, "#000000", (width, 0, panel, height))
    textSurface = font.render(f" : {player1.coins}", True, "#ffffff")
    screen.blit(textSurface, (width + 19, 38))
    screen.blit(coinTextimg,(width + 7, 32))
    if grid == grid1:
        textKey = font.render(f"keys: {player1.key}", True, "#ffffff")
        screen.blit(textKey, (width + 19, 60))
    elif grid == grid2:
        textSurface = font.render(f"notes : {player1.notes}", True, "#ffffff")
        screen.blit(textSurface, (width + 19, 60))
    if player1.notes == 1:
        textCode1 = font.render(f"code : {player1.code1}", True, "#ffffff")
        screen.blit(textCode1, (width + 19, 80))    
    if player1.notes == 2:
        textCode2 = font.render(f"code : {player1.code1}{player1.code2}", True, "#ffffff")
        screen.blit(textCode2, (width + 19, 80))
    if player1.notes == 3:
        textCode3 = font.render(f"code : {player1.code1}{player1.code2}{player1.code3}", True, "#ffffff")
        screen.blit(textCode3, (width + 19, 80))    
    if player1.notes == 4:
        textCode4 = font.render(f"code : {player1.code1}{player1.code2}{player1.code3}{player1.code4}", True, "#ffffff")
        screen.blit(textCode4, (width + 19, 80))    

based = False
def open():
    if event.type == py.KEYDOWN:
            if event.key == py.K_e:
            # if player1.coins == counter:
                if player1.key == keycount:
                    if (grid1[player1.y//60][player1.x//60] == 12):
                        grid1[player1.y//60][player1.x//60] = 13
                        print("testing open")
                        return True
    return False

def input():
    if event.type == py.KEYDOWN:
        if event.key == py.K_e:
            if player1.notes == notecount:
                if (grid1[player1.y//60][player1.x//60] == 9):
                    grid1[player1.y//60][player1.x//60] = 2137
                
def pickup():
    if (grid1[player1.y//60][player1.x//60] == 3):
        player1.coins += 1
        grid1[player1.y//60][player1.x//60] = 11

def noteget():
    if (grid2[player1.y//60][player1.x//60] == 10):
        player1.notes += 1
        grid2[player1.y//60][player1.x//60] = 16
        
def keypickup():
    if (grid1[player1.y//60][player1.x//60] == 14):
        player1.key += 1
        grid1[player1.y//60][player1.x//60] = 15

                


# r= img.get_rect()

run = True
while run:           
    if based == False:
        grid = grid1
        background = bgimg
        info = coins
        extra = 0
        funk = pickup()
    elif based == True:
        print("Testing")
        grid = grid2
        background = bgimg2
        info = notes
        extra = code
        funk = noteget()

    clock.tick(10)
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False
        if event.type == py.KEYDOWN:
            if event.key == py.K_r:
                run = False
        player1.move(screen, grid, event)
        keypickup()
        funk
        if based == False:
            based = open()
        input()
        print(based)
    screen.blit(background, (0,0))
    draw_panel(screen, info, extra)
    draw_grid(grid)



    '''
    how to draw on the screen using our grid?
    '''
    #player2.movebad(screen, grid)
    
    player1.draw(screen)
    # player2.draw(screen)
    
    
    #r.center = (player1.x, player1.y)
    #screen.blit(img,p)
    
    py.display.flip()#update the screen

py.quit()
#make the game a rhythm game  