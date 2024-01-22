import pygame
pygame.font.init()
import variables
import fail
import random
import win

gordonPixelImage = pygame.image.load('images/gordPixels.png')
tutorialText1 = variables.talkingFont.render("Finally, it's time to make some chicken..", True, variables.black)
tutorialText2 = variables.talkingFont.render("Catch five chickens into your bucket..", True, variables.black)
tutorialText3 = variables.talkingFont.render("Use A/D to move your bucket..", True, variables.black)
tutorialText4 = variables.talkingFont.render("Beware of impostor bomb chickens!!", True, variables.black)

chickenBackgroundImage = pygame.image.load('images/chickenbkg.png')

bucketImage = pygame.image.load('images/bucket.png')
bucketImageRect = bucketImage.get_rect(center=(variables.screenX/2, variables.screenY/2))

chickenImage = pygame.image.load('images/chickenFall.png')
chickenEvilImage = pygame.image.load('images/chickenFallEvil.png')

chickenFallSound = pygame.mixer.Sound("sounds/chickenFallSound.wav")
creeperSound = pygame.mixer.Sound("sounds/creeperSound.wav")

chickenList = []

class Chicken(pygame.sprite.Sprite):
    def __init__(self, dx, dy, speed, status, filename):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = dx
        self.rect.y = dy
        self.speed = speed
        self.status = status
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
    def move(self):
        self.rect.y = self.rect.y + self.speed

def initChicken():
    variables.gordonTalking = True; variables.talkStatus = "intro"; variables.tutorialText = 1
    variables.bucketX = bucketImageRect[0]
    variables.bucketDirection = "none"
    variables.chickensCaught = 0; chickenList.clear()
    print("initialized chicken")

def spawnChicken(amount):
    for i in range (0, amount, 1):
        evilNiceRandom = random.randint(1,2)
        randomX = random.randint(0, variables.screenX-80)
        randomSpeed = random.randint(2, 3)
        if(evilNiceRandom == 1):
            chickenList.append(Chicken(randomX, -40, randomSpeed, "nice", 'images/chickenFall.png')) # NICE SPAWN
            chickenFallSound.play()
        elif(evilNiceRandom == 2):
            chickenList.append(Chicken(randomX, -40, randomSpeed, "evil", 'images/chickenFallEvil.png')) # EVIL SPAWN
            creeperSound.play()

def chicken():
    variables.screen.blit(chickenBackgroundImage, (0,0))

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

    # SPACE DETECTION
    if variables.ev.type == pygame.KEYUP:
            if variables.ev.key == pygame.K_SPACE:
                if(variables.talkStatus == "intro"):
                    if(variables.tutorialText < 4):
                        variables.tutorialText += 1
                    elif(variables.tutorialText == 4):
                        variables.gordonTalking = False; variables.talkStatus = "chickensFalling"; spawnChicken(3)

    # DRAW CHICKENS & UPDATE CHICKEN POSITION
    if(variables.talkStatus == "chickensFalling"):
        for chicken in chickenList:
            chicken.move()
            chicken.draw(variables.screen)

            if(chicken.rect.y > variables.screenY-120): # remove chicken if touches ground
                spawnChicken(1)
                chickenList.remove(chicken)

            if pygame.Rect.collidepoint(chicken.rect, variables.bucketX+60, 540): # bucket-chicken collision
                chickenList.remove(chicken)
                spawnChicken(1)
                if(chicken.status == "nice"):
                    print("NICE CHICKEN")
                    variables.chickensCaught += 1
                elif(chicken.status == "evil"):
                    print("BAD CHICKEN")
                    fail.initFail()
                    variables.gameState = "fail"

    # 5 CHICKEN WIN DETECTION
    if(variables.chickensCaught == 5):
        win.initWin()
        variables.gameState = "win"

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

    variables.screen.blit(bucketImage, (variables.bucketX, 520))