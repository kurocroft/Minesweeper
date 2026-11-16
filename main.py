import pygame
import random

pygame.init()
wHeight = 400
wWidth = 600
open = True

# making our grid
class Minezone:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # in this grid, 0 represents unknown/grass. 1 represents explored & no mine. 2 represents mine. 3 represents flagged.
        self.grid = [[0 for i in range(width)] for j in range(height)]
    
    def renderMinezone(self):
        for i in range(self.width):
            for j in range(self.height):
                mineNum = random.randint(1, 10)
                mine = True if mineNum == 5 else False
                self.grid[i][j] = Cell(mine, (i*30+20), (j*30+20), 25)
                self.grid[i][j].renderCell()



class Cell:
    def __init__(self, mine, x, y, l):
        #boolean value passed upon creation
        self.mine = mine
        self.flag = False
        #a revealed MINE cell
        self.revealed = False
        self.mystery = True
        self.clicked = False

        #parameters for rect
        self.colour = "chartreuse2"
        self.x = x
        self.y = y
        self.l = l



    def updateColour(self):
            if self.mystery:
                self.colour = green
            elif self.flag:
                self.colour = red
            elif self.revealed:
                self.colour = purple

    def renderCell(self):
        pygame.draw.rect(display_surface, self.colour, pygame.Rect(self.x, self.y, self.l, self.l))




display_surface = pygame.display.set_mode((wWidth, wHeight))
pygame.display.set_caption("Minesweeper")

cellColour = (255, 255, 203)  

#def renderGrid(colour):
#    for i in range(5):
#        for j in range(5):
#            pygame.draw.rect(display_surface, colour, pygame.Rect(i*25+20, j*25+20, 20, 20))






while open:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open = False;
   

    display_surface.fill('pink')
   
    NewMine = Minezone(10, 10)
    NewMine.renderMinezone()

    pygame.display.update()

pygame.quit()



