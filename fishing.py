import pygame
pygame.font.init()
import variables
import math

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
        if(self.rect.x <= 1216):
            self.rect.x = self.rect.x + variables.speed
    def moveLeft(self):
        if(self.rect.x >= -17):
            self.rect.x = self.rect.x - variables.speed

grassImage = pygame.image.load('images/grass.png')
waterImage = pygame.image.load('images/water.png')

ammoImage = pygame.image.load('images/ammo.png')

gordonPixelImage = pygame.image.load('images/gordPixels.png')
gordonPixelImageRect = gordonPixelImage.get_rect(center=(variables.screenX/2, variables.screenY/2))

tutorialText1 = variables.talkingFont.render("Your first challenge is to make fish and chips..", True, variables.black)
tutorialText2 = variables.talkingFont.render("I want you to catch a fresh fish from the ocean..", True, variables.black)
tutorialText3 = variables.talkingFont.render("Use space to shoot your gun..", True, variables.black)
tutorialText4 = variables.talkingFont.render("Be careful, you have limited bullets.", True, variables.black)

player = Player(200, 490, 'images/character/idle/1.png')

# SHOOTING VARIABLES
variables.start = pygame.math.Vector2((player.rect.x, player.rect.y))
variables.end = variables.start
variables.bulletSpeed = variables.bulletSpeed
bulletList = []

def initFishing():
    variables.gordonTalking = True
    variables.tutorialText = 1
    variables.ammo = 5

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
                if(variables.tutorialText < 4):
                    variables.tutorialText += 1
                elif(variables.tutorialText == 4):
                    variables.gordonTalking = False

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

    # MOUSE SHOOT 
    if variables.ev.type == pygame.MOUSEBUTTONDOWN:
        if(variables.ammo > 0):
            variables.ammo -= 1

            mouse_x, mouse_y = pygame.mouse.get_pos()
            
            distance_x = mouse_x - player.rect.x - 40
            distance_y = mouse_y - player.rect.y - 30
            
            angle = math.atan2(distance_y, distance_x)
            
            speed_x = variables.bulletSpeed * math.cos(angle)
            speed_y = variables.bulletSpeed * math.sin(angle)
            
            bulletList.append([player.rect.x + 40, player.rect.y + 30, speed_x, speed_y])

    # UPDATE BULLETS
    for bullet in bulletList:
        # speed_x, speed_y can be `float` but I don't convert to `int` to get better position
        bullet[0] += bullet[2]  # posX - speed
        bullet[1] += bullet[3]  # posY - speed
        if((bullet[0] < 0) or (bullet[0] > variables.screenX) or (bullet[1] < 0) or (bullet[1] > variables.screenY)):
            bulletList.remove(bullet)

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
        if(variables.tutorialText == 1):
            variables.screen.blit(tutorialText1, (160, 600))
        elif(variables.tutorialText == 2):
            variables.screen.blit(tutorialText2, (160, 600))
        elif(variables.tutorialText == 3):
            variables.screen.blit(tutorialText3, (160, 600))
        elif(variables.tutorialText == 4):
            variables.screen.blit(tutorialText4, (160, 600))
    
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

    player.draw(variables.screen)

    print(bulletList)