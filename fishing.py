import pygame
pygame.font.init()
import variables

grassImage = pygame.image.load('images/grass.png')
waterImage = pygame.image.load('images/water.png')

def fishing():
    variables.screen.fill(variables.blue)

    for y in range(0, variables.screenY, 16): # DRAW WATER AND GRASS
        if(y >= 480):
            for x in range(0, variables.screenX, 16):
                variables.screen.blit(grassImage, (x, y), (16, 16, 16, 16))
        else:
            for x in range(0, variables.screenX, 16):
                variables.screen.blit(waterImage, (x, y), (32, 0, 16, 16))