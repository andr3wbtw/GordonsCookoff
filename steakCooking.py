import pygame
pygame.font.init()
import variables
import fail
import math
import random

kitchenImage = pygame.image.load('images/kitchen.png')
gordonPixelImage = pygame.image.load('images/gordPixels.png')

steakImage = pygame.image.load('images/steak.png')
steakTransparentImage = pygame.image.load('images/steakTransparent.png')
steakImageRect = steakImage.get_rect(center=(variables.screenX/2, variables.screenY/2))

fireImage = pygame.image.load('images/fire.png')
fireImageRect = fireImage.get_rect(center=(variables.screenX/2, variables.screenY/2))

tutorialText1 = variables.talkingFont.render("Your next challenge is to cook some steak..", True, variables.black)
tutorialText2 = variables.talkingFont.render("Press space bar when the temperature is in the middle!", True, variables.black)
tutorialText3 = variables.talkingFont.render("Impressive.. onto my last challenge.", True, variables.black)

def initSteakCooking():
    variables.gordonTalking = True; variables.tutorialText = 1; variables.talkStatus = "intro"; variables.steakDetection = False
    variables.steaksCooked = 0; variables.fireX = fireImageRect[0]
    print("initialized steak cooking")

def steakCooking():
    middleRect = pygame.draw.rect(variables.screen, variables.red, (variables.screenX/2-60, 265, 120, 120)) # INVISIBLE RECTANGLE FOR COLLISION DETECTION # INVISIBLE RECTANGLE FOR COLLISION DETECTION
    variables.screen.blit(kitchenImage, (0,0))

    # SPACE DETECTION
    if variables.ev.type == pygame.KEYUP:
            if variables.ev.key == pygame.K_SPACE:
                if(variables.steakDetection == True):
                    fireImageRect = fireImage.get_rect()
                    fireImageRect.x = variables.fireX
                    fireImageRect.y = 245
                    if fireImageRect.colliderect(middleRect) and (variables.steaksCooked <= 3):
                        variables.steaksCooked += 1
                        variables.fireSpeed -= 6
                        print("STEAK CORRECTLY COOKED")
                if(variables.talkStatus == "intro"):
                    if(variables.tutorialText < 2):
                        variables.tutorialText += 1
                    elif(variables.tutorialText == 2):
                        variables.gordonTalking = False
                        variables.steakDetection = True
                        variables.tutorialText+= 1
                elif(variables.talkStatus == "done"):
                    if(variables.tutorialText < 4):
                        variables.tutorialText += 1
                    if(variables.tutorialText == 4):
                        variables.gordonTalking = False
                        variables.gameState = "chicken"
    
    # ENABLE STEAK RECTANGLE TRACKING

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
        elif(variables.talkStatus == "done"):
            if(variables.tutorialText == 3):
                variables.screen.blit(tutorialText3, (160, 600))

    # STEAK ICON DRAW & LOGIC
    variables.screen.blit(steakTransparentImage, (steakImageRect[0]-150, 20))
    variables.screen.blit(steakTransparentImage, (steakImageRect[0], 20))
    variables.screen.blit(steakTransparentImage, (steakImageRect[0]+150, 20))
    if(variables.steakDetection == True):
        if(variables.steaksCooked >=1):
            variables.screen.blit(steakImage, (steakImageRect[0]+150, 20))
            if(variables.steaksCooked >=2):
                variables.screen.blit(steakImage, (steakImageRect[0], 20))
                if(variables.steaksCooked >= 3):
                    variables.screen.blit(steakImage, (steakImageRect[0]-150, 20))
                    variables.fireSpeed = 0
                    variables.gordonTalking = True; variables.talkStatus = "done"

    pygame.draw.rect(variables.screen, (variables.black), pygame.Rect(0, 280, variables.screenX, 100),  10, 30)
    pygame.draw.circle(variables.screen, variables.black, (variables.screenX/2, 325), 60)
    variables.screen.blit(fireImage, (variables.fireX, 245))