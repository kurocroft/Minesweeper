import pygame

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

    #def renderMinezone(self):
     #   tiles = []
      #  posx = 0
       # poxy = 0
        #for i in range(self.width):
         #   for j in range(self.height):
               # tile = self.grid[i, j]
                #match tile:
                 #   case 0:
                  #  case 1:
                   # case 2:
                    #case 3:
                #for every j, increase row
            # for every i, go down





display_surface = pygame.display.set_mode((wWidth, wHeight))
pygame.display.set_caption("Minesweeper")

cellColour = (255, 255, 203)  

def renderGrid(colour):
    for i in range(5):
        for j in range(5):
            pygame.draw.rect(display_surface, colour, pygame.Rect(i*25+20, j*25+20, 20, 20))



while open:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open = False;
   

    display_surface.fill('pink')
    renderGrid(cellColour)
    pygame.display.update()

pygame.quit()



