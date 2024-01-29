import pygame
pygame.font.init()
import variables
import fail
import steakCooking
import math
import random

# # # # # # # # # # # # # # # # # # # # # # # # #
# Images #
grassImage = pygame.image.load('images/grass.png')
waterImage = pygame.image.load('images/water.png')

ammoImage = pygame.image.load('images/ammo.png')
tableImage = pygame.image.load('images/table.png')

gordonPixelImage = pygame.image.load('images/gordPixels.png')
# # # # # # # # # # # # # # # # # # # # # # # # #
# Sound #
shootSound = pygame.mixer.Sound("sounds/shootSound.wav")
chopSound = pygame.mixer.Sound("sounds/chopSound.wav")
powerupSound = pygame.mixer.Sound("sounds/powerupSound.wav")
# # # # # # # # # # # # # # # # # # # # # # # # #
# Text #
tutorialText1 = variables.talkingFont.render("Your first challenge is to make fish and chips..", True, variables.black) # generate all tutorial text fonts
tutorialText2 = variables.talkingFont.render("I want you to catch a fresh fish from the ocean..", True, variables.black)
tutorialText3 = variables.talkingFont.render("Left click to shoot your gun..", True, variables.black)
tutorialText4 = variables.talkingFont.render("Be careful, you have limited bullets.", True, variables.black)

tutorialText5 = variables.talkingFont.render("Great job catching the fish..", True, variables.black) # generate all tutorial text fonts (pt 2)
tutorialText6 = variables.talkingFont.render("Now you have to cut the potatoes..", True, variables.black)
tutorialText7 = variables.talkingFont.render("Click to cut the potatoes.", True, variables.black)

tutorialText8 = variables.talkingFont.render("Amazing! Collect the fish and chips to continue.", True, variables.black) # generate all tutorial text fonts (pt 3)
tutorialText9 = variables.talkingFont.render("Click to cut the potatoes.", True, variables.black)

timer5 = variables.tastyBoldFont.render("5", True, variables.black)
timer5Rect = timer5.get_rect(center=(variables.screenX/2, variables.screenY/2))
timer4 = variables.tastyBoldFont.render("4", True, variables.black)
timer4Rect = timer4.get_rect(center=(variables.screenX/2, variables.screenY/2))
timer3 = variables.tastyBoldFont.render("3", True, variables.black)
timer3Rect = timer3.get_rect(center=(variables.screenX/2, variables.screenY/2))
timer2 = variables.tastyBoldFont.render("2", True, variables.black)
timer2Rect = timer2.get_rect(center=(variables.screenX/2, variables.screenY/2))
timer1 = variables.tastyBoldFont.render("1", True, variables.black)
timer1Rect = timer1.get_rect(center=(variables.screenX/2, variables.screenY/2))
timer0 = variables.tastyBoldFont.render("0", True, variables.black)
timer0Rect = timer0.get_rect(center=(variables.screenX/2, variables.screenY/2))
# # # # # # # # # # # # # # # # # # # # # # # # #

# Player Class: blueprint to create player as an object
class Player(pygame.sprite.Sprite):
    def __init__(self, dx, dy, filename): # called to initialize player class
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = dx
        self.rect.y = dy
        self.left = pygame.image.load('images/character/idle/1L.png').convert_alpha()
        self.right = pygame.image.load('images/character/idle/1R.png').convert_alpha()
    def draw(self, screen): # when called, draw self on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))
    def moveUp(self): # when called, move self up
        if(self.rect.y >= 418):
            self.rect.y = self.rect.y - variables.speed
    def moveDown(self): # when called, move self down
        if(self.rect.y <= 625):
            self.rect.y = self.rect.y + variables.speed
    def moveRight(self): # when called, move self right
        if(self.rect.x <= 1233):
            self.rect.x = self.rect.x + variables.speed
        self.image = self.right
    def moveLeft(self): # when called, move self left
        if(self.rect.x >= -34):
            self.rect.x = self.rect.x - variables.speed
        self.image = self.left

# Fish Class: blueprint to create fish objects which randomly move around the screen
class Fish(pygame.sprite.Sprite):
    def __init__(self, dx, dy, filename): # called to initialize fish class
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = dx
        self.rect.y = dy
    def draw(self, screen): # when called, draw self on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))
    def moveUp(self): # when called, move self up
        if(self.rect.y >= 0):
            self.rect.y = self.rect.y - variables.fishSpeed
    def moveDown(self): # when called, move self down
        if(self.rect.y <= 418):
            self.rect.y = self.rect.y + variables.fishSpeed
    def moveRight(self): # when called, move self right
        if(self.rect.x <= 1233):
            self.rect.x = self.rect.x + variables.fishSpeed
    def moveLeft(self): # when called, move self left
        if(self.rect.x >= -34):
            self.rect.x = self.rect.x - variables.fishSpeed 

# Potato Class: blueprint to create potato objects which move randomly from right to left or left to right
class Potato(pygame.sprite.Sprite):
    def __init__(self, dx, dy, speed, filename): # called to initialize potato class
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = dx
        self.rect.y = dy
        self.speed = speed
    def draw(self, screen): # when called, draw self on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))
    def move(self): # when called, move self to whichever direction moving in
        self.rect.x = self.rect.x - self.speed

# FishAndChips Class: blueprint to create the fish and chip object to go to next level
class FishAndChips(pygame.sprite.Sprite):
    def __init__(self, dx, dy, filename): # called to initialize fish and chips class
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = dx
        self.rect.y = dy
    def draw(self, screen): # when called, draw self on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

player = Player(200, 490, 'images/character/idle/1R.png') # create singular objects that are used within the level
caughtFish = Fish(variables.screenX-100, 500, 'images/fish.png')
caughtPotato = Potato(variables.screenX-115, 525, 0, 'images/potato.png')
fishAndChips = FishAndChips(variables.screenX-220, 500, 'images/fishandchips.png')

bulletList = [] # lists to track information about created objects
fishList = []
potatoList = []

# initFishing Function: function to reset fishing variables in order to allow for replayability
def initFishing():
    pygame.display.set_caption("Gordon's Cookoff - Game") # change window title
    variables.gordonTalking = True # reset variables
    variables.tutorialText = 1
    variables.ammo = 5
    variables.fishShot = False; variables.potatoCollected = False
    variables.talkStatus = "intro"
    variables.potatoTimerBegin = 0; variables.potatoTimerEnd = 0
    player.rect.x = 200; player.rect.y = 490
    fishList.clear(); potatoList.clear() # clear object lists
    for i in range (0, 5, 1): # generate 5 fish
        randX = random.randint(0,variables.screenX) # generate a random x
        randY = random.randint(0, 460) # generate a random y
        fishList.append(Fish(randX, randY, 'images/fish.png')) # make a new fish object and put it into fish list
    print("initialized fishing")

# spawnPotato Function: function to generate (amount) number of potatoes via the Potato class
def spawnPotato(amount):
    for i in range (0, amount, 1): # for number of potatoes needed to spawn
        leftRightRandom = random.randint(1,2) # generate random left or right
        randomY = random.randint(-20, 400)
        if(leftRightRandom == 1): # if left chosen
            potatoList.append(Potato(-70, randomY, -2, 'images/potato.png')) # spawn a new chicken on the left side of screen
        elif(leftRightRandom == 2): # if right chosen
            potatoList.append(Potato(variables.screenX-10, randomY, 2, 'images/potato.png')) # spawn a new chicken on the right side of screen

# MAIN FISHING LOOP
def fishing():
    variables.screen.fill(variables.blue)

    # MOVEMENT UPDATING
    if(variables.goingUp == True): # if player is moving up
        player.moveUp() # update position
    if(variables.goingDown == True): # if player is moving down
        player.moveDown() # update position
    if(variables.goingRight == True): # if player is moving right
        player.moveRight() # update position
    if(variables.goingLeft == True): # if player is moving left
        player.moveLeft() # update position

    # SPACE DETECTION
    if variables.ev.type == pygame.KEYUP: # if key released
            if variables.ev.key == pygame.K_SPACE: # if key is space
                if(variables.talkStatus == "intro"):
                    if(variables.tutorialText < 4): # update tutorial dialogue
                        variables.tutorialText += 1
                    elif(variables.tutorialText == 4):
                        variables.gordonTalking = False
                elif(variables.talkStatus == "prepotato"):
                    if(variables.tutorialText < 7):
                        variables.tutorialText += 1
                    elif(variables.tutorialText == 7): # if reached end of dialogue
                        variables.talkStatus = "potato"
                        variables.gordonTalking = False # stop dialogue
                        variables.potatoTimerBegin = pygame.time.get_ticks() # begin potato spawning timer
                        spawnPotato(3) # spawn 3 potatoes

    # MOVEMENT DETECTION (START)
    if variables.ev.type == pygame.KEYDOWN: # if key pressed
        if variables.ev.key == pygame.K_w: # if key is w
            variables.goingUp = True
        elif variables.ev.key == pygame.K_s: # if key is s
            variables.goingDown = True
        elif variables.ev.key == pygame.K_d: # if key is d
            variables.goingRight = True
        elif variables.ev.key == pygame.K_a: # if key is a
            variables.goingLeft = True
    # MOVEMENT DETECTION (STOP)
    if variables.ev.type == pygame.KEYUP: # if key released
        if variables.ev.key == pygame.K_w: # if key is w
            variables.goingUp = False; 
        elif variables.ev.key == pygame.K_s: # if key is s
            variables.goingDown = False; 
        elif variables.ev.key == pygame.K_d: # if key is d
            variables.goingRight = False; 
        elif variables.ev.key == pygame.K_a: # if key is a
            variables.goingLeft = False; 

    # MOUSE LEFT CLICK DETECTION 
    if (variables.ev.type == pygame.MOUSEBUTTONDOWN) and (variables.ev.button == 1): # if left mouse button is clicked
        if(variables.talkStatus == "intro"): # if in fish shooting minigame
            variables.gordonTalking = False
            if(variables.ammo > 0) and (pygame.mouse.get_pressed()[0]): # if player still has ammo
                shootSound.play() # play shoot sound
                variables.ammo -= 1 # remove 1 ammo

                mouse_x, mouse_y = pygame.mouse.get_pos() # track mouse position
                
                distance_x = mouse_x - player.rect.x - 40 # math to track distance between click and player position
                distance_y = mouse_y - player.rect.y - 30
                
                angle = math.atan2(distance_y, distance_x) # track angle for speed
                
                speed_x = variables.bulletSpeed * math.cos(angle) # generate bullet x and y speed based on angle
                speed_y = variables.bulletSpeed * math.sin(angle)
                
                bulletList.append([player.rect.x + 40, player.rect.y + 30, speed_x, speed_y]) # create bullet in bullet list to track info
        elif(variables.talkStatus == "potato"): # if in potato minigame
            chopSound.play()
            variables.gordonTalking = False
            mouseX, mouseY = pygame.mouse.get_pos() # track mouse position
            for potato in potatoList: # for # of potatoes in potatolist
                if pygame.Rect.collidepoint(potato.rect, mouseX, mouseY): # if mouse is colliding inside of potato rectangle
                    potatoList.remove(potato) # remove potato from list

    # UPDATE BULLETS
    for bullet in bulletList:
        bullet[0] += bullet[2]  # posX - speed
        bullet[1] += bullet[3]  # posY - speed
        if((bullet[0] < 0) or (bullet[0] > variables.screenX) or (bullet[1] < 0) or (bullet[1] > variables.screenY)): # if bullet is out of border
            bulletList.remove(bullet) # remove bullet
        # FISH-BULLET COLLISION DETECTION
        for fish in fishList: # for # of fish in fishlist
            if pygame.Rect.collidepoint(fish.rect, bullet[0], bullet[1]): # if bullet is colliding inside of fish rectangle
                bulletList.remove(bullet) # remove bullet
                fishList.clear() # remove all remaining fish
                variables.fishShot = True # update variables
                variables.gordonTalking = True
                variables.talkStatus = "prepotato"
                variables.tutorialText = 5
                variables.ammo = 0

    # UPDATE GAME STATUS AFTER ALL POTATOES COLLECTED
    if(variables.talkStatus == "potato") and (len(potatoList) == 0):
        variables.potatoCollected = True; variables.talkStatus = "done"; variables.gordonTalking = True

    # DRAW WATER AND GRASS
    for y in range(0, variables.screenY, 16): # for # of rows on screen (Y value), increase by 16 each loop
        if(y >= 480): # if on lower screen
            for x in range(0, variables.screenX, 16): # draw grass tiles
                variables.screen.blit(grassImage, (x, y), (16, 16, 16, 16))
        else: # if on higher screen
            for x in range(0, variables.screenX, 16): # draw water tiles
                variables.screen.blit(waterImage, (x, y), (32, 0, 16, 16))

    # GORDON TALKING SEQUENCE
    if(variables.gordonTalking == True): # if tutorial text is active
        variables.screen.blit(gordonPixelImage, (-20, 490)) # display gordon pixel image
        if(variables.talkStatus == "intro"):
            if(variables.tutorialText == 1): # depending on current dialogue, display text
                variables.screen.blit(tutorialText1, (160, 600))
            elif(variables.tutorialText == 2):
                variables.screen.blit(tutorialText2, (160, 600))
            elif(variables.tutorialText == 3):
                variables.screen.blit(tutorialText3, (160, 600))
            elif(variables.tutorialText == 4):
                variables.screen.blit(tutorialText4, (160, 600))
        elif(variables.talkStatus == "prepotato"):
            if(variables.tutorialText == 5):
                variables.screen.blit(tutorialText5, (160, 600))
            elif(variables.tutorialText == 6):
                variables.screen.blit(tutorialText6, (160, 600))
            elif(variables.tutorialText == 7):
                variables.screen.blit(tutorialText7, (160, 600))
        elif(variables.talkStatus == "done"):
            variables.screen.blit(tutorialText8, (160, 600))
    
    # DRAW BULLETS
    for pos_x, pos_y, speed_x, speed_y in bulletList: # for every data value listed in bulletlist
        pos_x = int(pos_x) # screen only uses int values
        pos_y = int(pos_y)
        pygame.draw.circle(variables.screen, (variables.red), (pos_x, pos_y), 5) # draw bullet based on position

    # DRAW AMMO DISPLAY
    if(variables.ammo > 0): # if ammo is at least 1
        variables.screen.blit(ammoImage, (10, 10)) # draw 1st ammo image
        if(variables.ammo > 1): # if ammo is at least 2
            variables.screen.blit(ammoImage, (40, 10)) # draw 2nd ammo image
            if(variables.ammo > 2):
                variables.screen.blit(ammoImage, (70, 10))
                if(variables.ammo > 3):
                    variables.screen.blit(ammoImage, (100, 10))
                    if(variables.ammo > 4):
                        variables.screen.blit(ammoImage, (130, 10))
    elif(variables.ammo == 0) and (variables.fishShot == False) and (variables.talkStatus == "intro") and (len(bulletList) == 0): # if out of ammo
        variables.gameState = "fail"; fail.initFail() # fail game

    # DRAW FISH & UPDATE FISH POSITION
    for fish in fishList: # for # of fish in fishlist
        fish.draw(variables.screen) # draw fish on screen
        randNum = random.randint(0,4) 
        if randNum == 1: # randomly move each fish up/down/left/right
            fish.moveUp()
        elif randNum == 2:
            fish.moveDown()
        elif randNum == 3:
            fish.moveRight()
        elif randNum == 4:
            fish.moveLeft()

    # DRAW POTATOES & UPDATE POTATO POSITION
    if(variables.talkStatus == "potato"):
        for potato in potatoList: # for # of potatoes in potatolist
            potato.move() # move potatoes right/left
            potato.draw(variables.screen) # draw potatoes on screen

            if((potato.rect.x < -80) or (potato.rect.x > (variables.screenX+20))): # if potato is out of screen border
                spawnPotato(1) # create new potato 
                potatoList.remove(potato) # remove old potato

    # DRAW POTATO TIMER & UPDATE
    if(variables.talkStatus == "potato"):
        variables.potatoTimerEnd = pygame.time.get_ticks() # get end timer ticks
        if((variables.potatoTimerEnd - variables.potatoTimerBegin) >= 0) and ((variables.potatoTimerEnd - variables.potatoTimerBegin) <= 1000): # if timer at 5
            variables.screen.blit(timer5, (timer5Rect[0], 20)) # display "5" text
        if((variables.potatoTimerEnd - variables.potatoTimerBegin) >= 1000) and ((variables.potatoTimerEnd - variables.potatoTimerBegin) <= 2000): # if timer at 4
            variables.screen.blit(timer4, (timer4Rect[0], 20)) # display "4" text
        if((variables.potatoTimerEnd - variables.potatoTimerBegin) >= 2000) and ((variables.potatoTimerEnd - variables.potatoTimerBegin) <= 3000): # if timer at 3
            variables.screen.blit(timer3, (timer3Rect[0], 20)) # display "3" text
        if((variables.potatoTimerEnd - variables.potatoTimerBegin) >= 3000) and ((variables.potatoTimerEnd - variables.potatoTimerBegin) <= 4000): # if timer at 2
            variables.screen.blit(timer2, (timer2Rect[0], 20)) # display "2" text
        if((variables.potatoTimerEnd - variables.potatoTimerBegin) >= 4000) and ((variables.potatoTimerEnd - variables.potatoTimerBegin) <= 5000): # if timer at 1
            variables.screen.blit(timer1, (timer1Rect[0], 20)) # display "1" text
        if((variables.potatoTimerEnd - variables.potatoTimerBegin) >= 5000): # if timer at 0
            variables.screen.blit(timer0, (timer0Rect[0], 20)) # display "0" text
        if((variables.potatoTimerEnd - variables.potatoTimerBegin) >= 6000): # if timer below 0
            variables.gameState = "fail"; fail.initFail() # lose game

    # DRAW FISH ON TABLE WHEN CAUGHT
    if(variables.fishShot == True): # if fish was shot
        variables.screen.blit(tableImage, (variables.screenX-100, 495)) # display fish on table
        caughtFish.draw(variables.screen)
    if(variables.potatoCollected == True): # if potatoes were collected
        variables.screen.blit(tableImage, (variables.screenX-100, 560)) # display potato on table
        caughtPotato.draw(variables.screen)

    # DRAW FISH AND CHIPS AND COLLISION DETECTION
    if(variables.talkStatus == "done"):
        fishAndChips.draw(variables.screen)
        if pygame.sprite.collide_rect(player, fishAndChips): # if player rect colliding with fishandchips rect
            steakCooking.initSteakCooking()
            variables.gameState = "steak" # go to steak cooking level
            powerupSound.play()

    player.draw(variables.screen)