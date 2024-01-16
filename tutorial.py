import pygame
pygame.font.init()
import variables

gordonPixelImage = pygame.image.load('images/gordPixels.png')
gordonPixelImageRect = gordonPixelImage.get_rect(center=(variables.screenX/2, variables.screenY/2))

characterImage = pygame.image.load('images/character/idle/1.png')

grassImage = pygame.image.load('images/grass.png')

tutorialText = ["Welcome to my cookoff!", "Use WASD to move" "Good luck!"]
tutorialText1 = variables.talkingFont.render("(Press space to continue..)", True, variables.white)
tutorialText2 = variables.talkingFont.render("Welcome to my cookoff!", True, variables.white)
tutorialText3 = variables.talkingFont.render("Use WASD to move.", True, variables.white)
tutorialText4 = variables.talkingFont.render("I have three cooking challenges for you.", True, variables.white)
tutorialText5 = variables.talkingFont.render("Don't disappoint me.", True, variables.white)

def initTutorial():
    variables.gordonTalking = True
    variables.tutorialText = 1

def tutorial():
    variables.screen.fill(variables.blue)

    if variables.ev.type == pygame.KEYUP:
            if variables.ev.key == pygame.K_SPACE:
                if(variables.tutorialText < 5):
                    variables.tutorialText += 1
                elif(variables.tutorialText == 5):
                    variables.gordonTalking = False

    for y in range(0, variables.screenY, 16):
        for x in range(0, variables.screenX, 16):
            variables.screen.blit(grassImage, (x, y), (0, 128, 16, 16))

    if(variables.gordonTalking == True):
        variables.screen.blit(gordonPixelImage, (-20, 490))
        if(variables.tutorialText == 1):
            variables.screen.blit(tutorialText1, (160, 600))
        elif(variables.tutorialText == 2):
            variables.screen.blit(tutorialText2, (160, 600))
        elif(variables.tutorialText == 3):
            variables.screen.blit(tutorialText3, (160, 600))
        elif(variables.tutorialText == 4):
            variables.screen.blit(tutorialText4, (160, 600))
        elif(variables.tutorialText == 5):
            variables.screen.blit(tutorialText5, (160, 600))

    variables.screen.blit(characterImage, (variables.xPos, variables.yPos))