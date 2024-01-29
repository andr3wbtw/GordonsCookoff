import pygame
pygame.font.init()
import variables
import tutorial

winImage = pygame.image.load('images/winbkg.png')
winSound = pygame.mixer.Sound("sounds/winSound.wav")

clickToPlayAgain = variables.crispyFoodFont.render("Click to Play Again", True, variables.gold)
clickToPlayAgainRect = clickToPlayAgain.get_rect(center=(variables.screenX/2, variables.screenY/2))

# initChicken Function: function to reset win variables in order to allow for replayability
def initWin():
    pygame.display.set_caption("Gordon's Cookoff - Win")
    pygame.mixer.Sound.play(winSound)
    print("initialized win state")

# MAIN WIN LOOP
def win():
    if variables.ev.type == pygame.MOUSEBUTTONUP: # if mouse button is released
        tutorial.initTutorial() 
        variables.gameState = "tutorial" # restart game, go back to tutorial

    variables.screen.blit(winImage, (0,0)) # display win bkg image
    variables.screen.blit(clickToPlayAgain, (clickToPlayAgainRect[0], 600)) # display click to play text