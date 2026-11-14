import pygame

pygame.init()
wHeight = 1000
wWidth = 1500
open = True

display_surface = pygame.display.set_mode((wWidth, wHeight))


while open:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open = false;



