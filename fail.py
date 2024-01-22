import pygame
pygame.font.init()
import variables
import random
import tutorial

# SOUND FILES
chickenSound = pygame.mixer.Sound("sounds/chickenSound.wav")
donkeySound = pygame.mixer.Sound("sounds/donkeySound.wav")
madSound = pygame.mixer.Sound("sounds/madSound.wav")
lambSound = pygame.mixer.Sound("sounds/lambSound.wav")
sandwichSound = pygame.mixer.Sound("sounds/sandwichSound.wav")
yankieSound = pygame.mixer.Sound("sounds/yankieSound.wav") # <--- rare lose sound

# IMAGE FILES
chickenImage = pygame.image.load('images/chickenImage.png')
donkeyImage = pygame.image.load('images/donkeyImage.png')
madImage = pygame.image.load('images/madImage.png')
lambImage = pygame.image.load('images/lambImage.png')
sandwichImage = pygame.image.load('images/sandwichImage.png')
yankieImage = pygame.image.load('images/yankieImage.png') # <--- rare lose screen

# FONTS
clickToRestart = variables.crispyFoodFont.render("Click to Restart", True, variables.black)
clickToRestartRect = clickToRestart.get_rect(center=(variables.screenX/2, variables.screenY/2))

def initFail():
    rareRoll = random.randint(1,5)
    if(rareRoll != 5):
        ranNum = random.randint(1,5)
        if(ranNum == 1):
            variables.failSequence = "chicken"
            pygame.mixer.Sound.play(chickenSound)
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
    elif(rareRoll == 5):
         variables.failSequence = "yankie"
         pygame.mixer.Sound.play(yankieSound)

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
    elif(variables.failSequence == "lamb"):
        variables.screen.blit(lambImage, (0,0))
    elif(variables.failSequence == "sandwich"):
        variables.screen.blit(sandwichImage, (0,0))
    elif(variables.failSequence == "yankie"):
        variables.screen.blit(yankieImage, (0,0))
    variables.screen.blit(clickToRestart, (clickToRestartRect[0], 600))