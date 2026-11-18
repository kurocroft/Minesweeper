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

    #hover detection - must be done using event watcher
    def click(self):
        for i in range(self.width):
            for j in range(self.height):
                self.grid[i][j].checkClick()




class Cell:
    def __init__(self, mine, x, y, l):
        #boolean value passed upon creation
        self.mine = mine
        self.flag = False
        self.mystery = True
        self.clicked = False

        #a revealed MINE cell
        self.found = False
        #a revealed CLEAR cell
        self.clear = False

        #parameters for rect
        self.colour = "chartreuse3"
        self.x = x
        self.y = y
        self.l = l
        #rect object
        self.rectangle = pygame.Rect(self.x, self.y, self.l, self.l)
        
    def updateColour(self):
            if self.mystery:
                self.colour = 'chartreuse3'
            elif self.flag:
                self.colour = 'red'
            elif self.found:
                self.colour = 'purple'
            elif self.clear:
                self.colour = 'yellow'


    def clicked(self):
        self.clicked = True
        if self.mine:
            self.found = True
            print("GAME OVER")
        else:
            self.clear = True

        self.updateColour()
        self.renderCell()

    def checkClick(self):
        mousePos = pygame.mouse.get_pos()
        if self.rectangle.collidepoint(mousePos):
            self.colour = 'aqua'
            self.renderCell()



    def renderCell(self):
        pygame.draw.rect(display_surface, self.colour, self.rectangle)




display_surface = pygame.display.set_mode((wWidth, wHeight))
pygame.display.set_caption("Minesweeper")

cellColour = (255, 255, 203)  

while open:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open = False
        
        display_surface.fill('pink')
        
        NewMine = Minezone(10, 10)
        NewMine.renderMinezone()
        if event.type == pygame.MOUSEBUTTONUP:
            NewMine.click()
   

    


    pygame.display.update()

pygame.quit()



