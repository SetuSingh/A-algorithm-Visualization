#----------------------------#           #----- importing and initializing ----------#
import pygame
import math
from queue import PriorityQueue
import time
import random


from pygame.constants import KEYDOWN, K_LSHIFT, K_SPACE,K_RSHIFT       

pygame.init()
#----------------------------#        #------- setting up display -------- #
WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption('A* PATH FINDING ALGO')
#---------------------------#
#---------------------------# #------COLOR CONSTANTs----#
WALL = (64,64,64)
GREEN = (51,255,153)
BLUE = (0,0,255)
YELLOW = (255,255,0)
ORANGE = (255,165,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
PURPLE = (255,0,255)
TEAL = (153,255,204)
GRAY = (128,128,128)
LIGHT_BLUE= (153,204,255)
PINK = (229,204,255)
#---------------------------#

#---------------------------#    #-----defining rows, col , total_rows, then defining colors for blocks----#
class Node:
    def __init__(self,row,col,width,total_rows):
        self.row = row
        self.col = col
        self.x = row*width
        self.y = col*width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row ,self.col
    
    def is_closed(self):
        return self.color == TEAL
    def is_open(self):
        return self.color == GREEN
    def is_barrier(self):
        return self.color == WALL
    def is_start(self):
        return self.color == YELLOW
    def is_end(self):
        return self.color == BLUE
    def reset(self):
        self.color = WHITE
    
    def make_is_closed(self):
        self.color = TEAL 
    def make_is_open(self):
        self.color = GREEN
    def make_is_barrier(self):
        self.color = WALL
    def make_is_start(self):
        self.color = YELLOW
    def make_is_end(self):
        self.color = BLUE
    def make_is_path(self):
        self.color = ORANGE
        #self.numb += 1
    def draw(self,win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))
#---------------------------# 
#---------------------------#  #----definining neighbour traversal----#
    def update_neighbors(self, grid):
        self.neighbors = []
        if self.row > 0 and not grid[self.row-1][self.col].is_barrier():     #UP
            self.neighbors.append(grid[self.row-1][self.col])

        if self.row < self.total_rows - 1  and not grid[self.row+1][self.col].is_barrier():     #DOWN
            self.neighbors.append(grid[self.row+1][self.col])

        if self.col > 0 and not grid[self.row][self.col-1].is_barrier():     #left
            self.neighbors.append(grid[self.row][self.col-1])

        if self.col < self.total_rows - 1  and not grid[self.row][self.col+1].is_barrier():     #right
            self.neighbors.append(grid[self.row][self.col+1])
        


        

#---------------------------#  #------edge_case----#
    def __lt__(self,other):
        return False
#---------------------------#
#---------------------------# #------text to show on screen---#
def text_object(text,font):
    textsurface = font.render(text, True, (0,0,0))
    return textsurface, textsurface.get_rect()
#---------------------------#
#---------------------------# #-----text properties--#
def message(text):
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    tSurf,tRect = text_object(text,myfont)
    tRect =  (100,700)
    WIN.blit(tSurf,tRect )

    pygame.display.update()
    time.sleep(3)
#---------------------------#
#---------------------------#  #--another text object-----#
def text_object2(text,font):
    textsurface2 = font.render(text, True, BLUE)
    return textsurface2, textsurface2.get_rect()
#---------------------------#
#---------------------------# #------another text property------#
def message2(text2):                                    
    myfont2 = pygame.font.Font("AstroSpace-eZ2Bg.ttf", 50)
    tSurf2,tRect2 = text_object2(text2,myfont2)
    tRect2 =  (160,700)
    WIN.blit(tSurf2,tRect2 )

    pygame.display.update()
    time.sleep(.5)
#---------------------------#
#---------------------------#   #------defining H score, (asssumed shortest distance)-----#
def h(p1,p2):                                         #h_score
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1-x2) + abs(y1-y2)
#---------------------------#
#---------------------------#  #-----reconstructing the path---#
def counter(num):
    num += 1
    
def reconstruct_path(came_from,current,draw,end,start,num=0):
    while current in came_from:
        current = came_from[current]
        current.make_is_path()
        num += 1
        end.make_is_end()
        start.make_is_start()
        draw()
    num = num -1
    message(f'A* ALGO took  {num} blocks to reach the destination')
#---------------------------#

#---------------------------# #------main algo----#
def algorithm(draw,grid,start,end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}
    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0
    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = h(start.get_pos(),end.get_pos())

    open_set_hash = {start}
    
    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        current = open_set.get()[2]
        open_set_hash.remove(current)
        
        if current == end:
            reconstruct_path(came_from, end, draw,end,start)
            end.make_is_end()
            start.make_is_start()
            l = f_score[start] - 1
            #message(f'It took us {a} blocks')
            end.make_is_end()
            start.make_is_start()
            


            return True
            
        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1
            
            if temp_g_score < g_score[neighbor]:
                
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
                
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_is_open()
        draw()
        
        if current != start:
            current.make_is_closed()
            
    return False

def make_grid(rows,width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i,j,gap,rows)
            grid[i].append(node)

    return grid
def draw_grid(win,rows,width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GRAY,(0,i * gap),(width, i* gap))
        for j in range(rows):
            pygame.draw.line(win, GRAY,(j * gap,0),(j* gap,width))
            
def draw(win , grid, rows, width):
    win.fill(WHITE)
    
    for row in grid:
        for node in row:
            node.draw(win)
    
    draw_grid(win, rows, width)
    pygame.display.update()

def click_pos(pos,rows,width):
    gap = width // rows
    y, x = pos
    
    row = y // gap
    col = x // gap
    return row, col


random1 = 0
list_c = []
def main(win,width):
    global random1,list_c
    ROWS = 50
    grid = make_grid(ROWS,width)

    start = None
    end = None
    
    run = True
    started = False
     
    while run:
        draw(win,grid,ROWS,width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if started == True:
                continue
            
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = click_pos(pos, ROWS, width)
                spot = grid[row][col]
                
                if not start and spot != end:
                    start = spot
                    spot.make_is_start()
                    
                elif not end and spot != start :
                    end = spot
                    spot.make_is_end()
                    
                elif spot != start and spot != end:
                    spot.make_is_barrier()

            if pygame.mouse.get_pressed()[1]:         ## ---- NOT WORKING :((( ##---- 
                pos = pygame.mouse.get_pos()
                row, col = click_pos(pos, ROWS, width)
                spot = grid[row][col]
                WIN.blit(textsurface,(WIDTH //2,WIDTH//2))

                
            if pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = click_pos(pos, ROWS, width)
                spot = grid[row][col]
                spot.reset()
                if spot == start:
                    start = None
                elif spot == end:
                    end = None

            


            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE and not started:
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)

                    algorithm(lambda: draw(win,grid,ROWS, width), grid,start,end)
            
            if event.type == pygame.KEYDOWN:
                if event.key == K_LSHIFT:
                    message2('RESETTING - SCENE')
                    main(win,width)
            
            if event.type == pygame.KEYDOWN:
                if event.key == K_RSHIFT:
                    message2('Chosing Random')
                    time.sleep(2)
                    
                    for i in range(0,50):
                        for j in range(0,50):
                            list_c.append((i,j))
                    for i in range(1000):
                        random1 = random.choice(list_c)
                        random_row , random_col = random1
                        aa = random_row
                        bb = random_col
                        print(aa,bb)
                        spot = grid[aa][bb]
                        if spot != start and spot != end:
                            spot.make_is_barrier()
    
    
    pygame.quit()
    
    
main(WIN, WIDTH)