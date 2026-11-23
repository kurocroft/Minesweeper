import pygame
import random

#Initialise the pygame
pygame.init()
#Window preferences
wHeight = 500
wWidth = 500
#Ensure it doesn't quit immediately upon starting
open = True
sizex = 15
sizey = 15

# Background surface
display_surface = pygame.display.set_mode((wWidth, wHeight))
# Application title
pygame.display.set_caption("Minesweeper")

# making our grid
class Minezone:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # in this grid, 0 represents unknown/grass. 1 represents explored & no mine. 2 represents mine. 3 represents flagged.
        self.grid = [[0 for i in range(width)] for j in range(height)]

    # for all cells, finds mines within their vicinity
    def findCellValues(self):
        for i in range(self.width):
            for j in range(self.height):
                if self.grid[i][j].mine:
                    value = -1
                else:
                    value = 0
                    surround8 = [[i-1, j-1], [i-1, j], [i-1, j+1], [i, j-1], [i, j+1], [i+1, j-1], [i+1, j], [i+1, j+1]]
                    for x in range(len(surround8)):
                        try:
                            if surround8[x][0] == -1 or surround8[x][1] == -1:
                                continue
                            else:
                                if self.grid[surround8[x][0]][surround8[x][1]].mine:
                                    value += 1
                        except IndexError:
                            value += 0
                    
                self.grid[i][j].dangerValue = value
                        


    # Creates the initial cells in the Minezone grid
    def createCells(self):
        for i in range(self.width):
            for j in range(self.height):
                mineNum = random.randint(1, 20)
                mine = True if mineNum < 6 else False
                self.grid[i][j] = Cell(mine, (i*30+20), (j*30+20), 25)

    # Renders the Minezone
    def renderMinezone(self):
        for i in range(self.width):
            for j in range(self.height):
                self.grid[i][j].renderCell()

    #For later: a proper minezone should have a distinct percentage depending on grid size for difficulty.
    #           To do this I must take the array, find a random spot, and assign it a mine until a certain counter
    #           This is low priority right now.

    #For each cell, detects if its been clicked
    def leftClick(self):
        for i in range(self.width):
            for j in range(self.height):
                self.grid[i][j].checkLeftClick()

    def rightClick(self):
        for i in range(self.width):
            for j in range(self.height):
                self.grid[i][j].checkRightClick()

    def update(self):
        for i in range(self.width):
            for j in range(self.height):
                self.grid[i][j].updateClick()


#Defines each cell in the grid defined in Minezone
class Cell:
    def __init__(self, mine, x, y, l):
        #boolean value passed upon creation
        self.mine = mine
        self.flag = False
        self.mystery = True
        # How many mines in Vicinity
        self.dangerValue = 0
        self.neighbours = []

        #for mouse input
        self.leftClicked = False
        self.rightClicked = False

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
        self.font = pygame.font.SysFont('Arial', 18)
        

    # Changes attributes depending on clicks
    def updateClick(self):
        if self.leftClicked:
            self.mystery = False
            if self.mine:
                self.found = True
                print("GAME OVER")
            else:
                self.clear = True
        
        if self.rightClicked:
            if self.flag:
                self.flag = False
            else:
                self.flag = True

        self.updateColour()
        self.renderCell()
        self.leftClicked = False
        self.rightClicked = False

    # Checks if the cell has been left-clicked
    def checkLeftClick(self):
        mousePos = pygame.mouse.get_pos()
        if self.rectangle.collidepoint(mousePos):
            self.leftClicked = True
            self.updateClick()
    
    def checkRightClick(self):
        mousePos = pygame.mouse.get_pos()
        if self.rectangle.collidepoint(mousePos):
            self.rightClicked = True
            self.updateClick()

    # Updates colour depending on attribute
    def updateColour(self):
        if self.flag:
            self.colour = 'crimson'
        elif self.mystery:
            self.colour = 'chartreuse3'
        elif self.found:
            self.colour = 'purple'
        elif self.clear:
            self.colour = 'yellow'

    # Renders the Cell
    def renderCell(self):
        self.render = pygame.draw.rect(display_surface, self.colour, self.rectangle)
        if self.mystery == False:
            display_surface.blit(self.font.render(str(self.dangerValue), True, "crimson", None), (self.rectangle.centerx-5, self.rectangle.centery-10))





# Define new Minezone  
NewMine = Minezone(sizex, sizey)
# Initialise Cells
NewMine.createCells()
NewMine.findCellValues()

while open:
    # Watches for events 
    for event in pygame.event.get():
        # Checks if app closed
        if event.type == pygame.QUIT:
            open = False
        
        display_surface.fill('pink')

        # renders the minezone
        NewMine.renderMinezone()


        # Watches for mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            left = pygame.mouse.get_pressed()[0]
            right = pygame.mouse.get_pressed()[2]
            if left:
                NewMine.leftClick()
            if right == True:
                NewMine.rightClick()
        

    pygame.display.update()

pygame.quit()



