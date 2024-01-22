import pygame
pygame.font.init()
import variables
import tutorial

winImage = pygame.image.load('images/winbkg.png')
winSound = pygame.mixer.Sound("sounds/winSound.wav")

clickToPlayAgain = variables.crispyFoodFont.render("Click to Play Again", True, variables.gold)
clickToPlayAgainRect = clickToPlayAgain.get_rect(center=(variables.screenX/2, variables.screenY/2))

def initWin():
    pygame.display.set_caption("Gordon's Cookoff - Win")
    pygame.mixer.Sound.play(winSound)
    print("initialized win state")

def win():
    if variables.ev.type == pygame.MOUSEBUTTONUP:
                tutorial.initTutorial()
                variables.gameState = "tutorial"

    variables.screen.blit(winImage, (0,0))
    variables.screen.blit(clickToPlayAgain, (clickToPlayAgainRect[0], 600))