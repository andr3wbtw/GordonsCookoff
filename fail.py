import pygame
pygame.font.init()
import variables
import random

# SOUND FILES
chickenSound = pygame.mixer.Sound("sounds/chickenSound.wav")
donkeySound = pygame.mixer.Sound("sounds/donkeySound.wav")
madSound = pygame.mixer.Sound("sounds/madSound.wav")

# IMAGE FILES
chickenImage = pygame.image.load('images/chickenImage.png')
donkeyImage = pygame.image.load('images/donkeyImage.png')
madImage = pygame.image.load('images/madImage.png')

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
    if(variables.failSequence == "chicken"):
        variables.screen.blit(chickenImage, (0,0))
    elif(variables.failSequence == "donkey"):
        variables.screen.blit(donkeyImage, (0,0))
    elif(variables.failSequence == "mad"):
        variables.screen.blit(madImage, (0,0))