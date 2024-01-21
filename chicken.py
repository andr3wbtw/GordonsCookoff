import pygame
pygame.font.init()
import variables
import fail
import math
import random

tutorialText1 = variables.talkingFont.render("Finally, it's time to make some chicken..", True, variables.black)
tutorialText2 = variables.talkingFont.render("Catch 5 chickens into your bucket..", True, variables.black)
tutorialText3 = variables.talkingFont.render("Use A/D to move your bucket..", True, variables.black)
tutorialText4 = variables.talkingFont.render("Beware of impostor bomb chickens!!", True, variables.black)

chickenBackgroundImage = pygame.image.load('images/chickenbkg.png')

bucketImage = pygame.image.load('images/bucket.png')
bucketImageRect = bucketImage.get_rect(center=(variables.screenX/2, variables.screenY/2))

def initChicken():
    print("initialized chicken")
    variables.bucketX = bucketImageRect[0]
    variables.bucketDirection = "none"

def chicken():
    # BUCKET MOVEMENT AND BORDER LOGIC
    if(variables.bucketDirection) == "right" and (variables.bucketX < variables.screenX-80):
            variables.bucketX -= variables.bucketSpeed
    elif(variables.bucketDirection) == "left" and (variables.bucketX > -50):
        variables.bucketX += variables.bucketSpeed

    # BUCKET MOVEMENT KEY DETECTION
    if variables.ev.type == pygame.KEYDOWN:
        if variables.ev.key == pygame.K_d:
            variables.bucketDirection = "right"
        elif (variables.ev.key == pygame.K_a):
            variables.bucketDirection = "left"

    variables.screen.blit(chickenBackgroundImage, (0,0))
    variables.screen.blit(bucketImage, (variables.bucketX, 520))