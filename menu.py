import pygame
pygame.font.init()
import variables
import tutorial

# # # # # # # # # # # # # # # # # # # # # # # # #
# Images #
scrollingBkg1 = pygame.image.load('images/scrollingbkg1.png') # load all scrolling bkg images
scrollingBkg2 = pygame.image.load('images/scrollingbkg2.png')
scrollingBkg3 = pygame.image.load('images/scrollingbkg3.png')
scrollingBkg4 = pygame.image.load('images/scrollingbkg4.png')
scrollingBkg5 = pygame.image.load('images/scrollingbkg5.png')
scrollingBkg6 = pygame.image.load('images/scrollingbkg6.png')

gordonImage = pygame.image.load('images/gordon.jpg')
gordonImageRect = gordonImage.get_rect(center=(variables.screenX/2, variables.screenY/2))
# # # # # # # # # # # # # # # # # # # # # # # # #
# Text #
titleText = variables.tastyBoldFont.render("Gordon's Cookoff", True, variables.black)
titleTextRect = titleText.get_rect(center=(variables.screenX/2, variables.screenY/2))

clickToPlayText = variables.crispyFoodFont.render("Click to Play", True, variables.black)
clickToPlayTextRect = clickToPlayText.get_rect(center=(variables.screenX/2, variables.screenY/2))
# # # # # # # # # # # # # # # # # # # # # # # # #
# Sound #
tutorialSound = pygame.mixer.Sound("sounds/tutorialSound.wav")
# # # # # # # # # # # # # # # # # # # # # # # # #

# MAIN MENU LOOP
def menu():
    # MOUSE CLICK START GAME LOGIC
    if variables.ev.type == pygame.MOUSEBUTTONUP: # if mouse button is released
        tutorial.initTutorial()
        variables.gameState = "tutorial" # go to tutorial
        tutorialSound.play()

    # SCROLLING BKG DISPLAY LOGIC
    if(variables.currentScrolling == 1): # if on frame 1
        variables.screen.blit(scrollingBkg1, (0,0)) # display bkg frame 1
    elif(variables.currentScrolling == 2):
        variables.screen.blit(scrollingBkg2, (0,0))
    elif(variables.currentScrolling == 3):
        variables.screen.blit(scrollingBkg3, (0,0))
    elif(variables.currentScrolling == 4):
        variables.screen.blit(scrollingBkg4, (0,0))
    elif(variables.currentScrolling == 5):
        variables.screen.blit(scrollingBkg5, (0,0))
    elif(variables.currentScrolling == 6):
        variables.screen.blit(scrollingBkg6, (0,0))

    # SCROLLING LOGIC
    variables.scrollingTimer+=1 # increase scrolling timer by 1 tick
    if(variables.scrollingTimer % 100 == 0): # if timer is at 100
        if(variables.currentScrolling < 6):
            variables.currentScrolling += 1 # change bkg frame
        elif(variables.currentScrolling == 6):
            variables.currentScrolling = 1

    variables.screen.blit(titleText, (titleTextRect[0], 120)) # display images to screen
    variables.screen.blit(clickToPlayText, (clickToPlayTextRect[0], 550))
    variables.screen.blit(gordonImage, (gordonImageRect[0], 280))