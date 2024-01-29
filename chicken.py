import pygame
pygame.font.init()
import variables
import fail
import random
import win

# # # # # # # # # # # # # # # # # # # # # # # # #
# Images #
gordonPixelImage = pygame.image.load('images/gordPixels.png') # import gordon face image
chickenBackgroundImage = pygame.image.load('images/chickenbkg.png')
bucketImage = pygame.image.load('images/bucket.png')
bucketImageRect = bucketImage.get_rect(center=(variables.screenX/2, variables.screenY/2))
chickenImage = pygame.image.load('images/chickenFall.png')
chickenEvilImage = pygame.image.load('images/chickenFallEvil.png')
# # # # # # # # # # # # # # # # # # # # # # # # #
# Text #
tutorialText1 = variables.talkingFont.render("Finally, it's time to make some chicken..", True, variables.black) # generate all tutorial text fonts
tutorialText2 = variables.talkingFont.render("Catch five chickens into your bucket..", True, variables.black)
tutorialText3 = variables.talkingFont.render("Use A/D to move your bucket..", True, variables.black)
tutorialText4 = variables.talkingFont.render("Beware of impostor bomb chickens!!", True, variables.black)
# # # # # # # # # # # # # # # # # # # # # # # # #
# Sounds #
chickenFallSound = pygame.mixer.Sound("sounds/chickenFallSound.wav")
creeperSound = pygame.mixer.Sound("sounds/creeperSound.wav")
# # # # # # # # # # # # # # # # # # # # # # # # #

chickenList = [] # list to track all chicken objects

# Chicken Class: blueprint to create chicken objects which fall from the top border to the ground
class Chicken(pygame.sprite.Sprite):
    def __init__(self, dx, dy, speed, status, filename): # called to initialize chicken class
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = dx
        self.rect.y = dy
        self.speed = speed
        self.status = status
    def draw(self, screen): # when called, draw self on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))
    def move(self): # when called, move down based on self speed
        self.rect.y = self.rect.y + self.speed

# initChicken Function: function to reset chicken variables in order to allow for replayability
def initChicken():
    variables.gordonTalking = True; variables.talkStatus = "intro"; variables.tutorialText = 1
    variables.bucketX = bucketImageRect[0]
    variables.bucketDirection = "none"
    variables.chickensCaught = 0; chickenList.clear()
    print("initialized chicken")

# spawnChicken Function: function to generate (amount) number of chickens via the Chicken class
def spawnChicken(amount):
    for i in range (0, amount, 1): # amount of times to generate a chicken
        evilNiceRandom = random.randint(1,2) # choose whether or not to make good or evil chicken (50/50 chance)
        randomX = random.randint(0, variables.screenX-80) # random X value between 0 and screen size
        randomSpeed = random.randint(2, 3) # random speed value (2 or 3)
        if(evilNiceRandom == 1): # if nice spawn chosen
            chickenList.append(Chicken(randomX, -40, randomSpeed, "nice", 'images/chickenFall.png')) # NICE SPAWN
            chickenFallSound.play() # play nice sound
        elif(evilNiceRandom == 2): # if evil spawn chosen
            chickenList.append(Chicken(randomX, -40, randomSpeed, "evil", 'images/chickenFallEvil.png')) # EVIL SPAWN
            creeperSound.play() # play evil sound

# MAIN CHICKEN LOOP
def chicken():
    variables.screen.blit(chickenBackgroundImage, (0,0))

    # BUCKET MOVEMENT AND BORDER LOGIC
    if(variables.bucketDirection) == "right" and (variables.bucketX < variables.screenX-80): # if bucket direction is right and not at screen border
            variables.bucketX -= variables.bucketSpeed # move bucket right
    elif(variables.bucketDirection) == "left" and (variables.bucketX > -50): # if bucket direction is left and not at screen border
        variables.bucketX += variables.bucketSpeed # move bucket left

    # BUCKET MOVEMENT KEY DETECTION
    if variables.ev.type == pygame.KEYDOWN: # if player presses a key
        if variables.ev.key == pygame.K_d: # if key is d
            variables.bucketDirection = "right" # bucket direction is right
        elif (variables.ev.key == pygame.K_a): # if key is a
            variables.bucketDirection = "left" # bucket direction is left

    # SPACE DETECTION
    if variables.ev.type == pygame.KEYUP: # if player releases a key
            if variables.ev.key == pygame.K_SPACE: # if key is space
                if(variables.talkStatus == "intro"): # navigate through tutorial dialogue
                    if(variables.tutorialText < 4):
                        variables.tutorialText += 1
                    elif(variables.tutorialText == 4): # if at end of tutorial dialogue
                        variables.gordonTalking = False; variables.talkStatus = "chickensFalling"; spawnChicken(3) # start spawning chickens

    # DRAW CHICKENS & UPDATE CHICKEN POSITION
    if(variables.talkStatus == "chickensFalling"):
        for chicken in chickenList: # for each chicken that exists
            chicken.move() # update chicken info
            chicken.draw(variables.screen) # draw chicken on screen

            if(chicken.rect.y > variables.screenY-120): # remove chicken if touches ground
                spawnChicken(1) # spawn new chicken
                chickenList.remove(chicken) # remove old chicken from chicken list

            if pygame.Rect.collidepoint(chicken.rect, variables.bucketX+60, 540): # bucket-chicken collision
                chickenList.remove(chicken) # remove chicken if touching bucket
                spawnChicken(1) # spawn new chicken
                if(chicken.status == "nice"): # if caught nice chicken
                    print("NICE CHICKEN")
                    variables.chickensCaught += 1 # +1 for caught chicken counter
                elif(chicken.status == "evil"): # if caught bad chicken
                    print("BAD CHICKEN")
                    fail.initFail() # fail game
                    variables.gameState = "fail"

    # 5 CHICKEN WIN DETECTION
    if(variables.chickensCaught == 5): # if chicken counter is 5
        win.initWin() # win game
        variables.gameState = "win"

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

    variables.screen.blit(bucketImage, (variables.bucketX, 520)) # display bucket image