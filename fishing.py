import pygame
pygame.font.init()
import variables
import fail
import steakCooking
import math
import random

class Player(pygame.sprite.Sprite):
    def __init__(self, dx, dy, filename):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = dx
        self.rect.y = dy
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
    def moveUp(self):
        if(self.rect.y >= 418):
            self.rect.y = self.rect.y - variables.speed
    def moveDown(self):
        if(self.rect.y <= 625):
            self.rect.y = self.rect.y + variables.speed
    def moveRight(self):
        if(self.rect.x <= 1233):
            self.rect.x = self.rect.x + variables.speed
    def moveLeft(self):
        if(self.rect.x >= -34):
            self.rect.x = self.rect.x - variables.speed

class Fish(pygame.sprite.Sprite):
    def __init__(self, dx, dy, filename):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = dx
        self.rect.y = dy
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
    def moveUp(self):
        if(self.rect.y >= 0):
            self.rect.y = self.rect.y - variables.fishSpeed
    def moveDown(self):
        if(self.rect.y <= 418):
            self.rect.y = self.rect.y + variables.fishSpeed
    def moveRight(self):
        if(self.rect.x <= 1233):
            self.rect.x = self.rect.x + variables.fishSpeed
    def moveLeft(self):
        if(self.rect.x >= -34):
            self.rect.x = self.rect.x - variables.fishSpeed 

class Potato(pygame.sprite.Sprite):
    def __init__(self, dx, dy, speed, filename):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = dx
        self.rect.y = dy
        self.speed = speed
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
    def move(self):
        self.rect.x = self.rect.x - self.speed

class FishAndChips(pygame.sprite.Sprite):
    def __init__(self, dx, dy, filename):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = dx
        self.rect.y = dy
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))


grassImage = pygame.image.load('images/grass.png')
waterImage = pygame.image.load('images/water.png')

ammoImage = pygame.image.load('images/ammo.png')
tableImage = pygame.image.load('images/table.png')

gordonPixelImage = pygame.image.load('images/gordPixels.png')

tutorialText1 = variables.talkingFont.render("Your first challenge is to make fish and chips..", True, variables.black)
tutorialText2 = variables.talkingFont.render("I want you to catch a fresh fish from the ocean..", True, variables.black)
tutorialText3 = variables.talkingFont.render("Left click to shoot your gun..", True, variables.black)
tutorialText4 = variables.talkingFont.render("Be careful, you have limited bullets.", True, variables.black)

tutorialText5 = variables.talkingFont.render("Great job catching the fish..", True, variables.black)
tutorialText6 = variables.talkingFont.render("Now you have to cut the potatoes..", True, variables.black)
tutorialText7 = variables.talkingFont.render("Click to cut the potatoes.", True, variables.black)

tutorialText8 = variables.talkingFont.render("Amazing! Collect the fish and chips to continue.", True, variables.black)
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

player = Player(200, 490, 'images/character/idle/1.png')
caughtFish = Fish(variables.screenX-100, 500, 'images/fish.png')
caughtPotato = Potato(variables.screenX-115, 525, 0, 'images/potato.png')
fishAndChips = FishAndChips(variables.screenX-220, 500, 'images/fishandchips.png')

shootSound = pygame.mixer.Sound("sounds/shootSound.wav")
chopSound = pygame.mixer.Sound("sounds/chopSound.wav")
powerupSound = pygame.mixer.Sound("sounds/powerupSound.wav")

# SHOOTING VARIABLES
bulletList = []
fishList = []
potatoList = []

def initFishing():
    variables.gordonTalking = True
    variables.tutorialText = 1
    variables.ammo = 5
    variables.fishShot = False; variables.potatoCollected = False
    variables.talkStatus = "intro"
    variables.potatoTimerBegin = 0; variables.potatoTimerEnd = 0
    player.rect.x = 200; player.rect.y = 490
    fishList.clear(); potatoList.clear()
    for i in range (0, 5, 1):
        randX = random.randint(0,variables.screenX)
        randY = random.randint(0, 460)
        fishList.append(Fish(randX, randY, 'images/fish.png'))
    print("initialized fishing")

def spawnPotato(amount):
    for i in range (0, amount, 1):
        leftRightRandom = random.randint(1,2)
        randomY = random.randint(-20, 400)
        if(leftRightRandom == 1):
            potatoList.append(Potato(-70, randomY, -2, 'images/potato.png'))
        elif(leftRightRandom == 2):
            potatoList.append(Potato(variables.screenX-10, randomY, 2, 'images/potato.png'))

def fishing():
    variables.screen.fill(variables.blue)

    # MOVEMENT UPDATING
    if(variables.goingUp == True):
        player.moveUp()
    if(variables.goingDown == True):
        player.moveDown()
    if(variables.goingRight == True):
        player.moveRight()
    if(variables.goingLeft == True):
        player.moveLeft()

    # SPACE DETECTION
    if variables.ev.type == pygame.KEYUP:
            if variables.ev.key == pygame.K_SPACE:
                if(variables.talkStatus == "intro"):
                    if(variables.tutorialText < 4):
                        variables.tutorialText += 1
                    elif(variables.tutorialText == 4):
                        variables.gordonTalking = False
                elif(variables.talkStatus == "prepotato"):
                    if(variables.tutorialText < 7):
                        variables.tutorialText += 1
                    elif(variables.tutorialText == 7):
                        variables.talkStatus = "potato"
                        variables.gordonTalking = False
                        variables.potatoTimerBegin = pygame.time.get_ticks()
                        spawnPotato(3)

    # MOVEMENT DETECTION (START)
    if variables.ev.type == pygame.KEYDOWN:
        if variables.ev.key == pygame.K_w:
            variables.goingUp = True
        elif variables.ev.key == pygame.K_s:
            variables.goingDown = True
        elif variables.ev.key == pygame.K_d:
            variables.goingRight = True
        elif (variables.ev.key == pygame.K_a):
            variables.goingLeft = True
    # MOVEMENT DETECTION (STOP)
    if variables.ev.type == pygame.KEYUP: 
        if variables.ev.key == pygame.K_w:
            variables.goingUp = False; 
        elif variables.ev.key == pygame.K_s: 
            variables.goingDown = False; 
        elif variables.ev.key == pygame.K_d:
            variables.goingRight = False; 
        elif variables.ev.key == pygame.K_a:
            variables.goingLeft = False; 

    # MOUSE LEFT CLICK DETECTION 
    if (variables.ev.type == pygame.MOUSEBUTTONDOWN) and (variables.ev.button == 1):
        if(variables.talkStatus == "intro"):
            variables.gordonTalking = False
            if(variables.ammo > 0) and (pygame.mouse.get_pressed()[0]):
                shootSound.play()
                variables.ammo -= 1

                mouse_x, mouse_y = pygame.mouse.get_pos()
                
                distance_x = mouse_x - player.rect.x - 40
                distance_y = mouse_y - player.rect.y - 30
                
                angle = math.atan2(distance_y, distance_x)
                
                speed_x = variables.bulletSpeed * math.cos(angle)
                speed_y = variables.bulletSpeed * math.sin(angle)
                
                bulletList.append([player.rect.x + 40, player.rect.y + 30, speed_x, speed_y])
        elif(variables.talkStatus == "potato"):
            chopSound.play()
            variables.gordonTalking = False
            mouseX, mouseY = pygame.mouse.get_pos()
            for potato in potatoList:
                if pygame.Rect.collidepoint(potato.rect, mouseX, mouseY):
                    potatoList.remove(potato)

    # UPDATE BULLETS
    for bullet in bulletList:
        # speed_x, speed_y can be `float` but I don't convert to `int` to get better position
        bullet[0] += bullet[2]  # posX - speed
        bullet[1] += bullet[3]  # posY - speed
        if((bullet[0] < 0) or (bullet[0] > variables.screenX) or (bullet[1] < 0) or (bullet[1] > variables.screenY)):
            bulletList.remove(bullet)
        # FISH-BULLET COLLISION DETECTION
        for fish in fishList:
            if pygame.Rect.collidepoint(fish.rect, bullet[0], bullet[1]):
                bulletList.remove(bullet)
                fishList.clear()
                variables.fishShot = True
                variables.gordonTalking = True
                variables.talkStatus = "prepotato"
                variables.tutorialText = 5
                variables.ammo = 0

    # UPDATE GAME STATUS AFTER ALL POTATOES COLLECTED
    if(variables.talkStatus == "potato") and (len(potatoList) == 0):
        variables.potatoCollected = True; variables.talkStatus = "done"; variables.gordonTalking = True

    # DRAW WATER AND GRASS
    for y in range(0, variables.screenY, 16):
        if(y >= 480):
            for x in range(0, variables.screenX, 16):
                variables.screen.blit(grassImage, (x, y), (16, 16, 16, 16))
        else:
            for x in range(0, variables.screenX, 16):
                variables.screen.blit(waterImage, (x, y), (32, 0, 16, 16))

    # GORDON TALKING SEQUENCE
    if(variables.gordonTalking == True):
        variables.screen.blit(gordonPixelImage, (-20, 490))
        if(variables.talkStatus == "intro"):
            if(variables.tutorialText == 1):
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
    for pos_x, pos_y, speed_x, speed_y in bulletList:
        pos_x = int(pos_x) # screen only uses int values
        pos_y = int(pos_y)
        pygame.draw.circle(variables.screen, (variables.red), (pos_x, pos_y), 5)

    # DRAW AMMO DISPLAY
    if(variables.ammo > 0):
        variables.screen.blit(ammoImage, (10, 10))
        if(variables.ammo > 1):
            variables.screen.blit(ammoImage, (40, 10))
            if(variables.ammo > 2):
                variables.screen.blit(ammoImage, (70, 10))
                if(variables.ammo > 3):
                    variables.screen.blit(ammoImage, (100, 10))
                    if(variables.ammo > 4):
                        variables.screen.blit(ammoImage, (130, 10))
    elif(variables.ammo == 0) and (variables.fishShot == False) and (variables.talkStatus == "intro") and (len(bulletList) == 0):
        variables.gameState = "fail"; fail.initFail()

    # DRAW FISH & UPDATE FISH POSITION
    for fish in fishList:
        fish.draw(variables.screen)
        randNum = random.randint(0,4)
        if randNum == 1:
            fish.moveUp()
        elif randNum == 2:
            fish.moveDown()
        elif randNum == 3:
            fish.moveRight()
        elif randNum == 4:
            fish.moveLeft()

    # DRAW POTATOES & UPDATE POTATO POSITION
    if(variables.talkStatus == "potato"):
        for potato in potatoList:
            potato.move()
            potato.draw(variables.screen)

            if((potato.rect.x < -80) or (potato.rect.x > (variables.screenX+20))):
                spawnPotato(1)
                potatoList.remove(potato)

    # DRAW POTATO TIMER & UPDATE
    if(variables.talkStatus == "potato"):
        variables.potatoTimerEnd = pygame.time.get_ticks()
        if((variables.potatoTimerEnd - variables.potatoTimerBegin) >= 0) and ((variables.potatoTimerEnd - variables.potatoTimerBegin) <= 1000): # 5
            variables.screen.blit(timer5, (timer5Rect[0], 20))
        if((variables.potatoTimerEnd - variables.potatoTimerBegin) >= 1000) and ((variables.potatoTimerEnd - variables.potatoTimerBegin) <= 2000): # 4
            variables.screen.blit(timer4, (timer4Rect[0], 20))
        if((variables.potatoTimerEnd - variables.potatoTimerBegin) >= 2000) and ((variables.potatoTimerEnd - variables.potatoTimerBegin) <= 3000): # 3
            variables.screen.blit(timer3, (timer3Rect[0], 20))
        if((variables.potatoTimerEnd - variables.potatoTimerBegin) >= 3000) and ((variables.potatoTimerEnd - variables.potatoTimerBegin) <= 4000): # 2
            variables.screen.blit(timer2, (timer2Rect[0], 20))
        if((variables.potatoTimerEnd - variables.potatoTimerBegin) >= 4000) and ((variables.potatoTimerEnd - variables.potatoTimerBegin) <= 5000): # 1
            variables.screen.blit(timer1, (timer1Rect[0], 20))
        if((variables.potatoTimerEnd - variables.potatoTimerBegin) >= 5000): # 0
            variables.screen.blit(timer0, (timer0Rect[0], 20))
        if((variables.potatoTimerEnd - variables.potatoTimerBegin) >= 6000): # lose
            variables.gameState = "fail"; fail.initFail()

    # DRAW FISH ON TABLE WHEN CAUGHT
    if(variables.fishShot == True):
        variables.screen.blit(tableImage, (variables.screenX-100, 495))
        caughtFish.draw(variables.screen)
    if(variables.potatoCollected == True):
        variables.screen.blit(tableImage, (variables.screenX-100, 560))
        caughtPotato.draw(variables.screen)

    # DRAW FISH AND CHIPS AND COLLISION DETECTION
    if(variables.talkStatus == "done"):
        fishAndChips.draw(variables.screen)
        if pygame.sprite.collide_rect(player, fishAndChips):
            steakCooking.initSteakCooking()
            variables.gameState = "steak"
            powerupSound.play()

    player.draw(variables.screen)