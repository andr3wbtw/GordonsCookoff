import pygame
pygame.font.init()
import variables
import fail
import math
import random

kitchenImage = pygame.image.load('images/kitchen.png')
gordonPixelImage = pygame.image.load('images/gordPixels.png')

fireImage = pygame.image.load('images/fire.png')
fireImageRect = fireImage.get_rect(center=(variables.screenX/2, variables.screenY/2))

tutorialText1 = variables.talkingFont.render("Your next challenge is to cook some steak..", True, variables.black)
tutorialText2 = variables.talkingFont.render("Press space bar when the temperature is in the middle!", True, variables.black)

def initSteakCooking():
    variables.gordonTalking = True; variables.tutorialText = 1; variables.talkStatus = "intro"
    variables.fireX = fireImageRect[0]
    print("initialized steak cooking")

def steakCooking():
    middleRect = pygame.draw.rect(variables.screen, variables.red, (variables.screenX/2-60, 265, 120, 120)) # INVISIBLE RECTANGLE FOR COLLISION DETECTION # INVISIBLE RECTANGLE FOR COLLISION DETECTION
    variables.screen.blit(kitchenImage, (0,0))

    # SPACE DETECTION
    if variables.ev.type == pygame.KEYUP:
            if variables.ev.key == pygame.K_SPACE:
                if(variables.talkStatus == "intro"):
                    if(variables.tutorialText < 2):
                        variables.tutorialText += 1
                    elif(variables.tutorialText == 2):
                        variables.gordonTalking = False

    # FIRE MOVEMENT & EDGE DETECTION
    if variables.talkStatus == "intro":
        if(variables.fireDirection) == "right":
            variables.fireX -= variables.fireSpeed
        elif(variables.fireDirection) == "left":
            variables.fireX += variables.fireSpeed
        if(variables.fireX < -20):
            variables.fireDirection = "right"
        if(variables.fireX > variables.screenX-80):
            variables.fireDirection = "left"

    # GORDON TALKING SEQUENCE
    if(variables.gordonTalking == True):
        variables.screen.blit(gordonPixelImage, (-20, 490))
        if(variables.talkStatus == "intro"):
            if(variables.tutorialText == 1):
                variables.screen.blit(tutorialText1, (160, 600))
            elif(variables.tutorialText == 2):
                variables.screen.blit(tutorialText2, (160, 600))

    pygame.draw.rect(variables.screen, (variables.black), pygame.Rect(0, 280, variables.screenX, 100),  10, 30)
    pygame.draw.circle(variables.screen, variables.black, (variables.screenX/2, 325), 60)
    variables.screen.blit(fireImage, (variables.fireX, 245))