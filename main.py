import pygame
import random

#Initialise the pygame
pygame.init()
#Window preferences
wHeight = 400
wWidth = 600
#Ensure it doesn't quit immediately upon starting
open = True

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
                value = 0
                surround8 = [self.grid[i-1][j-1], self.grid[i-1][j], self.grid[i-1][j+1], self.grid[i][j-1], self.grid[i][j+1], self.grid[i+1][j-1], self.grid[i+1][j], self.grid[i+1][j-1]]
                surroundTL = [self.grid[i+1][j], self.grid[i+1][j+1], self.grid[i][j+1]]
                surroundTR = [self.grid[i][j-1], self.grid[i+1][j-1], self.grid[i+1][j]]
                surroundBL = [self.grid[i-1][j], self.grid[i-1][j+1], self.grid[i][j+1]]
                surroundBR = [self.grid[i][j-1], self.grid[i-1][j], self.grid[i-1][j-1]]
                if i < 1:
                    if j < 1:
                        # if the cell is in position (0,0) (TL)
                        for x in range(len(surroundTL)):
                            if surroundTL[x].mine:
                                value += 1
                    elif j == self.height-1:
                        for x in range(len(surroundTR)):
                            if surroundTR[x].mine:
                                value += 1
                    else:
                        # top row will never have above positions

                        # if the cell is in position (0,max) (TR)
                elif i == self.width-1:
                    if j<1:
                        # if cell is in position (max, 0) (BL)

                        for x in range(len(surroundBL)):
                            if surroundBL[x].mine:
                                value += 1
                    elif j == self.height-1:
                        # if cell is in position (max, max) (BR)

                        for x in range(len(surroundBR)):
                            if surroundBR[x].mine:
                                value += 1
                    else:
                        #bbottom row will never have below positions
                else:
                    #if cell is in any other positon
                    for x in range(len(surround8)):
                        if surround8[x].mine:
                            value += 1
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


#Defines each cell in the grid defined in Minezone
class Cell:
    def __init__(self, mine, x, y, l):
        #boolean value passed upon creation
        self.mine = mine
        self.flag = False
        self.mystery = True
        # How many mines in Vicinity
        self.dangerValue = 0

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
        pygame.draw.rect(display_surface, self.colour, self.rectangle)



# Background surface
display_surface = pygame.display.set_mode((wWidth, wHeight))
# Application title
pygame.display.set_caption("Minesweeper")

# Define new Minezone  
NewMine = Minezone(10, 10)
# Initialise Cells
NewMine.createCells()
#NewMine.findCellValues()

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



