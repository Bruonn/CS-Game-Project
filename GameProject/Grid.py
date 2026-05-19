from random import randint
import pygame as py
from Player import Player, Obstacle
from pygame import mixer
py.mixer.init()
dig_sound = py.mixer.Sound('Grass_dig1.ogg')
keypickup_sound = py.mixer.Sound('key-get.mp3')
keyopen_sound = py.mixer.Sound('key-twist-in-lock.mp3')
dooropen_sound = py.mixer.Sound('dooropen.wav')
drinksound = py.mixer.Sound('drinksound.mp3')
#background sounds







#to generalise our grid we use the followins variables
grid_r, grid_c, = 9, 9
grid1 = [[randint(0,6) for i in range(grid_c)]for j in range(grid_r)]

grid2 = [[randint(20,21) for i in range(grid_c)]for j in range(grid_r)]

grid3 = [[randint(30,31) for i in range(grid_c)]for j in range(grid_r)]

grid4 = [[randint(40,41) for i in range(grid_c)]for j in range(grid_r)]

grid5 = [[randint(50,51) for i in range(grid_c)]for j in range(grid_r)]
#ensure starting area is always open
grid1[0][0] = 1
grid1[1][0] = 1 #right neighbour
grid1[0][1] = 1 #bottom neighbour
grid1[4][8] = 12
grid1[4][7] = 1
grid1[7][2] = 14
grid2[8][4] = 9
grid2[randint(0,7)][randint(0,8)] = 10
grid2[randint(0,7)][randint(0,8)] = 10
grid2[randint(0,7)][randint(0,8)] = 10
grid2[randint(0,7)][randint(0,8)] = 10
grid3[0][8] = 32
grid4[0][0] = 39
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

for k in grid3:
    print(k)

for o in grid4:
    print(o)

for l in grid5:
    print(l)

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

shovelcount = 0
for s in grid4:
    for n in s:
        if n == 39:
            shovelcount += 1

cell_size = 60 #cell size in which the player will reside
#width and height of the game layout depends on the grid and cell size
width, height = cell_size * grid_c, cell_size * grid_r
panel = 150
coins = 0
notes = 0
key = 0
hole = py.image.load('hole.jpg')
hole = py.transform.scale(hole, (60,60))
funkymonkey = py.image.load('smiler.png')
funkymonkey = py.transform.scale(funkymonkey, (60,60))
bgimg3 = py.image.load('concrete.jpeg')
bgimg3= py.transform.scale(bgimg3, (width, height))
bgimg4 = py.image.load('sand.jpg')
bgimg4= py.transform.scale(bgimg4, (width, height))
thanksforbeingmyteacher = py.image.load('Untitled.png')
thanksforbeingmyteacher = py.transform.scale(thanksforbeingmyteacher, (width, height))
cash = py.image.load('almond water.png')
cash = py.transform.scale(cash, (60,60))
lockimg = py.image.load('exitdoor.png')
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
empty = py.image.load('empty.png')
empty = py.transform.scale(empty, (60,60))
funkykongList = [Player(j*cell_size, j*cell_size, funkymonkey) for j in range(0, grid_c - 1)]
exitimg = py.image.load('door.png')
exitimg = py.transform.scale(exitimg, (60,60))
key = py.image.load('key.jpg.pdf.jfif.jpeg.webp.heif')
key = py.transform.scale(key,(55,55))
shovel = py.image.load('shovel.png')
shovel = py.transform.scale(shovel, (55,55))
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
        elif grid[row][col] == 32:
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
            screen.blit(cash,(col*cell_size, row*cell_size))
        elif grid[row][col] == 43:
            screen.blit(exitimg, (col*cell_size, row*cell_size))
        elif grid[row][col] == 39:
            screen.blit(shovel, (col*cell_size, row*cell_size))
        elif grid[row][col] == 42:
            screen.blit(breakimg, (col*cell_size, row*cell_size))
            #py.draw.rect(screen, "#000000", (row*cell_size, col*cell_size, cell_size, cell_size))
        col += 1 #then go to the next cell
        if col == grid_c:   #if you reach the last column
            row += 1 #then we go to the next row
            col = 0 #and we reset the column to zero
        

def draw_panel(screen, info):
    font = py.font.SysFont(None, 30)
    py.draw.rect(screen, "#000000", (width, 0, panel, height))
    textSurface = font.render(f" : {player1.coins}", True, "#ffffff")
    textSurface2 = font.render(f"r = reset", True, "#ffffff")
    screen.blit(textSurface, (width + 19, 38))
    screen.blit(textSurface2, (width + 19, 500))
    screen.blit(coinTextimg,(width + 7, 32))
    if grid == grid1:
        textKey = font.render(f"keys: {player1.key}", True, "#ffffff")
        screen.blit(textKey, (width + 19, 60))
    elif grid == grid5:
        textKey = font.render(f"you won :)", True, "#ffffff")
        screen.blit(textKey, (width + 19, 60))
    elif grid == grid2:
        textSurface = font.render(f"take a rest", True, "#ffffff")
        screen.blit(textSurface, (width + 19, 150))
        textSurface = font.render(f":)", True, "#ffffff")
        screen.blit(textSurface, (width + 19, 180))
        # textSurface = font.render(f"notes : {player1.notes}", True, "#ffffff")
        # screen.blit(textSurface, (width + 19, 60))
        # if player1.notes == 1:
        #     textCode1 = font.render(f"code : {player1.code1}", True, "#ffffff")
        #     screen.blit(textCode1, (width + 19, 80))    
        # if player1.notes == 2:
        #     textCode2 = font.render(f"code : {player1.code1}{player1.code2}", True, "#ffffff")
        #     screen.blit(textCode2, (width + 19, 80))
        # if player1.notes == 3:
        #     textCode3 = font.render(f"code : {player1.code1}{player1.code2}{player1.code3}", True, "#ffffff")
        #     screen.blit(textCode3, (width + 19, 80))    
        # if player1.notes == 4:
        #     textCode4 = font.render(f"code : {player1.code1}{player1.code2}{player1.code3}{player1.code4}", True, "#ffffff")
        #     screen.blit(textCode4, (width + 19, 80))
    elif grid == grid4:
        textSurface = font.render(f"the exit is", True, "#ffffff")
        screen.blit(textSurface, (width + 19, 150))
        textSurface = font.render(f"not what it", True, "#ffffff")
        screen.blit(textSurface, (width + 19, 180))
        textSurface = font.render(f"seems", True, "#ffffff")
        screen.blit(textSurface, (width + 19, 210))


based = False
def open():
    if event.type == py.KEYDOWN:
            if event.key == py.K_e:
            # if player1.coins == counter:
                if player1.key == keycount:
                    if (grid1[player1.y//60][player1.x//60] == 12):
                        grid1[player1.y//60][player1.x//60] = 13
                        print("testing open")
                        keyopen_sound.play()
                        return True
    return False

further = False
def input():
    if event.type == py.KEYDOWN:
        if event.key == py.K_e:
            if player1.notes == notecount:
                if (grid2[player1.y//60][player1.x//60] == 9):
                        grid2[player1.y//60][player1.x//60] = 18
                        print("testing input")
                        dooropen_sound.play()
                        return True
    return False

lastlevel = False
def last_levelgo():
    if event.type == py.KEYDOWN:
        if event.key == py.K_e:
            if (grid3[player1.y//60][player1.x//60] == 32):
                grid3[player1.y//60][player1.x//60] = 13
                dooropen_sound.play()
                return True
    return False


idk = False
def leave():
    if event.type == py.KEYDOWN:
        if event.key == py.K_e:
            if (grid4[player1.y//60][player1.x//60] == 43):
                grid4[player1.y//60][player1.x//60] = 63
                dooropen_sound.play()
                return True
    return False



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
        keypickup_sound.play()
        grid1[player1.y//60][player1.x//60] = 15

def shovelpickup():
    if (grid4[player1.y//60][player1.x//60] == 39):
        player1.shovel = 1
        grid4[player1.y//60][player1.x//60] = 40

def pickup():
    if (grid1[player1.y//60][player1.x//60] == 3):
        player1.coins += 1
        grid1[player1.y//60][player1.x//60] = 11
      
def dig():
    if event.type == py.KEYDOWN:
        if event.key == py.K_e:
            if player1.shovel == 1:
                if (grid4[player1.y//60][player1.x//60] == 40) or (grid4[player1.y//60][player1.x//60] == 41):
                    if randint(1,10) == 1:
                        grid4[player1.y//60][player1.x//60] = 42
                    elif randint(1,10) == 2:
                        grid4[player1.y//60][player1.x//60] = 43
                    dig_sound.play()



def check_enemy_collision():
    for enemy in funkykongList:
        if (abs(player1.x - enemy.x) < 60 and abs(player1.y - enemy.y) < 60):
            player1.x = 4*60
            player1.y = 8*60
            print("system")
            

# r= img.get_rect()


run = True
while run:
    if idk == False:
        if lastlevel == False:
            if further == False:

                if based == False:
                    grid = grid1
                    background = bgimg
                    info = coins
                    funk = pickup()
                    funkykong = 0
                    bgmusic = mixer.music.load('humbuzz.mp3')
    #----------------------------------------------------
                elif based == True:
                    print("Testing")
                    grid = grid2
                    background = bgimg2
                    info = cash
                    funk= noteget()
                    funkykong = 0
                    bgmusic = 0

            elif further == True:
                grid = grid3
                background = bgimg3
                info = 0
                funk = 0
                bgmusic = 0
                for k in funkykongList:
                    k.movebad(screen, grid3)
                    k.movebad2electricboogalooremastered4keditionwithSHREK(screen, grid3)
                check_enemy_collision()

        elif lastlevel == True:
            grid = grid4
            background = bgimg4
            funk = shovelpickup()
            funkykong = 0
            info = 0
            bgmusic = 0
            if grid == grid4:
                funkykongList = [Player(j*cell_size, j*cell_size, empty) for j in range(0, grid_c - 1)]
            

    elif idk == True:
        grid = grid5
        background = thanksforbeingmyteacher
        funk = 0
        funkykong = 0
        info = 0
        bgmusic = 0

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
        funkykong
        dig()
        if based == False:
            based = open()
        elif further == False:
            further = input()
        elif lastlevel == False:
            lastlevel = last_levelgo()
        elif idk == False:
            idk = leave()
        print(based)
    screen.blit(background, (0,0))
    draw_panel(screen, info)
    draw_grid(grid)



    '''
    how to draw on the screen using our grid?
    '''
    #player2.movebad(screen, grid)
    
    player1.draw(screen)
    if further == True:
        for k in funkykongList:
            k.draw(screen)
        
    
    #r.center = (player1.x, player1.y)
    #screen.blit(img,p)
    
    py.display.flip()#update the screen

py.quit()
#make the game a rhythm game  