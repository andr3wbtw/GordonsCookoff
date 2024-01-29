import pygame
pygame.font.init()
import variables
import fail
import chicken

# # # # # # # # # # # # # # # # # # # # # # # # #
# Images #
kitchenImage = pygame.image.load('images/kitchen.png')
gordonPixelImage = pygame.image.load('images/gordPixels.png')

steakImage = pygame.image.load('images/steak.png')
steakTransparentImage = pygame.image.load('images/steakTransparent.png')
steakImageRect = steakImage.get_rect(center=(variables.screenX/2, variables.screenY/2))

fireImage = pygame.image.load('images/fire.png')
fireImageRect = fireImage.get_rect(center=(variables.screenX/2, variables.screenY/2))
# # # # # # # # # # # # # # # # # # # # # # # # #
# Text #
tutorialText1 = variables.talkingFont.render("Your next challenge is to cook some steak..", True, variables.black) # generate all tutorial text fonts
tutorialText2 = variables.talkingFont.render("Press space bar when the temperature is in the middle!", True, variables.black)
tutorialText3 = variables.talkingFont.render("Impressive.. onto my last challenge.", True, variables.black)
# # # # # # # # # # # # # # # # # # # # # # # # #
# Sound #
igniteSound = pygame.mixer.Sound("sounds/igniteSound.wav")
powerupSound = pygame.mixer.Sound("sounds/powerupSound.wav")
# # # # # # # # # # # # # # # # # # # # # # # # #

# initSteakCooking Function: function to reset steak variables in order to allow for replayability
def initSteakCooking():
    variables.gordonTalking = True; variables.tutorialText = 1; variables.talkStatus = "intro"; variables.steakDetection = False # reset variables
    variables.steaksCooked = 0; variables.fireX = fireImageRect[0]
    variables.fireSpeed = -8; variables.fireX = 0
    print("initialized steak cooking")

# MAIN STEAK LOOP
def steakCooking():
    middleRect = pygame.draw.rect(variables.screen, variables.red, (variables.screenX/2-60, 265, 120, 120)) # INVISIBLE RECTANGLE FOR COLLISION DETECTION
    variables.screen.blit(kitchenImage, (0,0)) # display kitchen bkg image

# STEAK ICON DRAW & LOGIC
    variables.screen.blit(steakTransparentImage, (steakImageRect[0]-150, 20)) # display transparent steak images
    variables.screen.blit(steakTransparentImage, (steakImageRect[0], 20))
    variables.screen.blit(steakTransparentImage, (steakImageRect[0]+150, 20))
    if(variables.steakDetection == True):
        if(variables.steaksCooked >=1): # if above 1 steak cooked
            variables.screen.blit(steakImage, (steakImageRect[0]+150, 20)) # display opaque steak image
            if(variables.steaksCooked >=2):
                variables.screen.blit(steakImage, (steakImageRect[0], 20))
                if(variables.steaksCooked >= 3): # if 3 steaks cooked
                    variables.screen.blit(steakImage, (steakImageRect[0]-150, 20)) # display all opaque steak images
                    variables.fireSpeed = 0 # stop moving fire
                    variables.gordonTalking = True; variables.talkStatus = "done" # update variables

    # SPACE DETECTION
    if variables.ev.type == pygame.KEYUP: # if key released
            if variables.ev.key == pygame.K_SPACE: # if key is space
                if(variables.steakDetection == True):
                    fireImageRect = fireImage.get_rect() # track fire rectangle
                    fireImageRect.x = variables.fireX # update fire rectangle x value to current x position
                    fireImageRect.y = 245 # update fire rectangle y value (static value)
                    if fireImageRect.colliderect(middleRect) and (variables.steaksCooked <= 3) and (variables.talkStatus == "intro"): # if invisible middle rectangle collides with fire rectangle
                        variables.steaksCooked += 1 # update steak counter
                        variables.fireSpeed -= 6 # increase speed
                        print("STEAK CORRECTLY COOKED")
                        igniteSound.play()
                    else: # if fire rectangle isn't in middle
                        if(variables.talkStatus == "intro"):
                            fail.initFail() # fail sequence
                            variables.gameState = "fail"
                            print("STEAK IS NOT COOKED PROPERLY")
                            igniteSound.play()
                if(variables.talkStatus == "intro"): # if in tutorial dialogue
                    if(variables.tutorialText < 2):
                        variables.tutorialText += 1 # go to next tutorial dialogue line
                    elif(variables.tutorialText == 2):
                        variables.gordonTalking = False
                        variables.steakDetection = True
                        variables.tutorialText+= 1
                elif(variables.talkStatus == "done"):
                    if(variables.tutorialText < 4):
                        variables.tutorialText += 1
                    if(variables.tutorialText == 4): # if at end of dialogue at end of steak cooking level
                        variables.gordonTalking = False
                        chicken.initChicken()
                        variables.gameState = "chicken" # go to chicken level
                        powerupSound.play()

    # FIRE MOVEMENT & EDGE DETECTION
    if variables.talkStatus == "intro":
        if(variables.fireDirection) == "right": # if fire direction is right
            variables.fireX -= variables.fireSpeed # move fire to right
        elif(variables.fireDirection) == "left":
            variables.fireX += variables.fireSpeed
        if(variables.fireX < -20): # if fire is at left screen border
            variables.fireDirection = "right" # start moving right
        if(variables.fireX > variables.screenX-80): # if fire is at right screen border
            variables.fireDirection = "left" # start moving left

    # GORDON TALKING SEQUENCE
    if(variables.gordonTalking == True): # if tutorial text is active
        variables.screen.blit(gordonPixelImage, (-20, 490)) # display gordon pixel image
        if(variables.talkStatus == "intro"):
            if(variables.tutorialText == 1): # depending on current dialogue, display text
                variables.screen.blit(tutorialText1, (160, 600))
            elif(variables.tutorialText == 2):
                variables.screen.blit(tutorialText2, (160, 600))
        elif(variables.talkStatus == "done"):
            if(variables.tutorialText == 3):
                variables.screen.blit(tutorialText3, (160, 600))

    pygame.draw.rect(variables.screen, (variables.black), pygame.Rect(0, 280, variables.screenX, 100),  10, 30) # draw invisible rectangle
    pygame.draw.circle(variables.screen, variables.black, (variables.screenX/2, 325), 60) # draw middle circle
    variables.screen.blit(fireImage, (variables.fireX, 245)) # draw fire image