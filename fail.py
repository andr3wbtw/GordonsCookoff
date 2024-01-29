import pygame
pygame.font.init()
import variables
import random
import tutorial

# # # # # # # # # # # # # # # # # # # # # # # # #
# Images #
chickenImage = pygame.image.load('images/chickenImage.png')
donkeyImage = pygame.image.load('images/donkeyImage.png')
madImage = pygame.image.load('images/madImage.png')
lambImage = pygame.image.load('images/lambImage.png')
sandwichImage = pygame.image.load('images/sandwichImage.png')
yankieImage = pygame.image.load('images/yankieImage.png') # <--- rare lose screen
# # # # # # # # # # # # # # # # # # # # # # # # #
# Sound #
chickenSound = pygame.mixer.Sound("sounds/chickenSound.wav")
donkeySound = pygame.mixer.Sound("sounds/donkeySound.wav")
madSound = pygame.mixer.Sound("sounds/madSound.wav")
lambSound = pygame.mixer.Sound("sounds/lambSound.wav")
sandwichSound = pygame.mixer.Sound("sounds/sandwichSound.wav")
yankieSound = pygame.mixer.Sound("sounds/yankieSound.wav") # <--- rare lose sound
# # # # # # # # # # # # # # # # # # # # # # # # #
# Text #
clickToRestart = variables.crispyFoodFont.render("Click to Restart", True, variables.black)
clickToRestartRect = clickToRestart.get_rect(center=(variables.screenX/2, variables.screenY/2))
# # # # # # # # # # # # # # # # # # # # # # # # #

# initFail Function: function to reset fail variables in order to allow for replayability
def initFail():
    pygame.display.set_caption("Gordon's Cookoff - Lose") # update window title
    rareRoll = random.randint(1,5) # common/rare fail screen roll
    if(rareRoll != 5): # if common rolled (1-4)
        ranNum = random.randint(1,5) # pick a random fail screen
        if(ranNum == 1):
            variables.failSequence = "chicken" # update variable to chosen fail screen
            pygame.mixer.Sound.play(chickenSound) # play fail screen sound
        elif(ranNum == 2):
            variables.failSequence = "donkey"
            pygame.mixer.Sound.play(donkeySound)
        elif(ranNum == 3):
            variables.failSequence = "mad"
            pygame.mixer.Sound.play(madSound)
        elif(ranNum == 4):
            variables.failSequence = "lamb"
            pygame.mixer.Sound.play(lambSound)
        elif(ranNum == 5):
            variables.failSequence = "sandwich"
            pygame.mixer.Sound.play(sandwichSound)
    elif(rareRoll == 5): # if rare rolled (5)
         variables.failSequence = "yankie" # update variable to chosen fail screen
         pygame.mixer.Sound.play(yankieSound) # play fail screen sound

# MAIN FAIL LOOP
def fail():
    if variables.ev.type == pygame.MOUSEBUTTONUP: # if released click button
        tutorial.initTutorial() # go back to tutorial state
        variables.gameState = "tutorial"
        pygame.mixer.Sound.stop(chickenSound); pygame.mixer.Sound.stop(donkeySound); pygame.mixer.Sound.stop(madSound); pygame.mixer.Sound.stop(lambSound); pygame.mixer.Sound.stop(sandwichSound); pygame.mixer.Sound.stop(yankieSound) # stop all sounds
        # stop any current sounds

    if(variables.failSequence == "chicken"): # display fail screen based on randomly chosen
        variables.screen.blit(chickenImage, (0,0))
    elif(variables.failSequence == "donkey"):
        variables.screen.blit(donkeyImage, (0,0))
    elif(variables.failSequence == "mad"):
        variables.screen.blit(madImage, (0,0))
    elif(variables.failSequence == "lamb"):
        variables.screen.blit(lambImage, (0,0))
    elif(variables.failSequence == "sandwich"):
        variables.screen.blit(sandwichImage, (0,0))
    elif(variables.failSequence == "yankie"):
        variables.screen.blit(yankieImage, (0,0))
    variables.screen.blit(clickToRestart, (clickToRestartRect[0], 600)) # display click to restart text