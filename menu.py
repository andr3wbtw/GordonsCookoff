import pygame
pygame.font.init()
import variables
import tutorial

titleText = variables.tastyBoldFont.render("Gordon's Cookoff", True, variables.white)
titleTextRect = titleText.get_rect(center=(variables.screenX/2, variables.screenY/2))

gordonImage = pygame.image.load('images/gordon.jpg')
gordonImageRect = gordonImage.get_rect(center=(variables.screenX/2, variables.screenY/2))

clickToPlayText = variables.crispyFoodFont.render("Click to Play", True, variables.white)
clickToPlayTextRect = clickToPlayText.get_rect(center=(variables.screenX/2, variables.screenY/2))

def menu():
    if variables.ev.type == pygame.MOUSEBUTTONUP:
                tutorial.initTutorial()
                variables.gameState = "tutorial"

    variables.screen.fill(variables.brown)
    variables.screen.blit(titleText, (titleTextRect[0], 120))
    variables.screen.blit(clickToPlayText, (clickToPlayTextRect[0], 550))
    variables.screen.blit(gordonImage, (gordonImageRect[0], 280))