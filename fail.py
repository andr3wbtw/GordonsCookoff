import pygame
pygame.font.init()
import variables
import random
import tutorial

# SOUND FILES
chickenSound = pygame.mixer.Sound("sounds/chickenSound.wav")
donkeySound = pygame.mixer.Sound("sounds/donkeySound.wav")
madSound = pygame.mixer.Sound("sounds/madSound.wav")

# IMAGE FILES
chickenImage = pygame.image.load('images/chickenImage.png')
donkeyImage = pygame.image.load('images/donkeyImage.png')
madImage = pygame.image.load('images/madImage.png')

# FONTS
clickToRestart = variables.crispyFoodFont.render("Click to Restart", True, variables.black)
clickToRestartRect = clickToRestart.get_rect(center=(variables.screenX/2, variables.screenY/2))

def initFail():
    ranNum = random.randint(1,3)
    if(ranNum == 1):
        variables.failSequence = "chicken"
        pygame.mixer.Sound.play(chickenSound)
    elif(ranNum == 2):
        variables.failSequence = "donkey"
        pygame.mixer.Sound.play(donkeySound)
    elif(ranNum == 3):
        variables.failSequence = "mad"
        pygame.mixer.Sound.play(madSound)

def fail():
    if variables.ev.type == pygame.MOUSEBUTTONUP:
                tutorial.initTutorial()
                variables.gameState = "tutorial"
                pygame.mixer.Sound.stop(chickenSound); pygame.mixer.Sound.stop(donkeySound); pygame.mixer.Sound.stop(madSound); # stop all sounds

    if(variables.failSequence == "chicken"):
        variables.screen.blit(chickenImage, (0,0))
    elif(variables.failSequence == "donkey"):
        variables.screen.blit(donkeyImage, (0,0))
    elif(variables.failSequence == "mad"):
        variables.screen.blit(madImage, (0,0))
    variables.screen.blit(clickToRestart, (clickToRestartRect[0], 600))