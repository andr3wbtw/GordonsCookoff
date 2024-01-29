import pygame
pygame.font.init()
import variables
import fishing

# # # # # # # # # # # # # # # # # # # # # # # # #
# Images #
gordonPixelImage = pygame.image.load('images/gordPixels.png')
gordonPixelImageRect = gordonPixelImage.get_rect(center=(variables.screenX/2, variables.screenY/2))

characterImage = pygame.image.load('images/character/idle/1R.png')

grassImage = pygame.image.load('images/grass.png')

tree1 = pygame.image.load('images/Tree1.png')
tree2 = pygame.image.load('images/Tree2.png')
# # # # # # # # # # # # # # # # # # # # # # # # #
# Text #
tutorialText1 = variables.talkingFont.render("(Press space to continue conversation)", True, variables.white) # generate all tutorial text fonts
tutorialText2 = variables.talkingFont.render("Welcome to my cookoff..", True, variables.white)
tutorialText3 = variables.talkingFont.render("Use WASD to move..", True, variables.white)
tutorialText4 = variables.talkingFont.render("I have three cooking challenges for you..", True, variables.white)
tutorialText5 = variables.talkingFont.render("Collect my Beef Wellington to begin..", True, variables.white)
tutorialText6 = variables.talkingFont.render("Don't disappoint me.", True, variables.white)
# # # # # # # # # # # # # # # # # # # # # # # # #
# Sound #
powerupSound = pygame.mixer.Sound("sounds/powerupSound.wav")
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
        if(self.rect.y >= -50):
            self.rect.y = self.rect.y - variables.speed
    def moveDown(self): # when called, move self down
        if(self.rect.y <= 625):
            self.rect.y = self.rect.y + variables.speed
    def moveRight(self): # when called, move self right
        if(self.rect.x <= 1216):
            self.rect.x = self.rect.x + variables.speed
        self.image = self.right
    def moveLeft(self): # when called, move self left
        if(self.rect.x >= -17):
            self.rect.x = self.rect.x - variables.speed
        self.image = self.left

# BeefWellington Class: blueprint to create the beef wellington object to go to next level
class BeefWellington(pygame.sprite.Sprite): 
    def __init__(self, dx, dy, filename): # called to initialize beef wellington class
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = dx
        self.rect.y = dy
    def draw(self, screen): # when called, draw self on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

# initTutorial Function: function to reset tutorial variables in order to allow for replayability
def initTutorial():
    pygame.display.set_caption("Gordon's Cookoff")
    variables.goingUp = False
    variables.goingDown = False
    variables.goingRight = False
    variables.goingLeft = False
    variables.gordonTalking = True
    variables.tutorialText = 1
    player.rect.x = 200
    player.rect.y = 200
    print("initialized tutorial")

player = Player(200, 200, 'images/character/idle/1R.png') # create singular objects that are used within the level
beef = BeefWellington(700, 300, 'images/beefwellington.png')

# MAIN TUTORIAL LOOP
def tutorial():
    variables.screen.fill(variables.blue)

    # MOVEMENT UPDATING
    if(variables.goingUp == True): # if player is going up
        player.moveUp() # move coordinates up
    if(variables.goingDown == True):
        player.moveDown()
    if(variables.goingRight == True):
        player.moveRight()
    if(variables.goingLeft == True):
        player.moveLeft()

    # SPACE DETECTION
    if variables.ev.type == pygame.KEYUP: # if key released
            if variables.ev.key == pygame.K_SPACE: # if key is space
                if(variables.tutorialText < 6):
                    variables.tutorialText += 1 # go to next dialogue line
                elif(variables.tutorialText == 6):
                    variables.gordonTalking = False

    # MOVEMENT DETECTION (START)
    if variables.ev.type == pygame.KEYDOWN: # if key pressed
        if variables.ev.key == pygame.K_w: # if key is w
            variables.goingUp = True # update movement boolean
        elif variables.ev.key == pygame.K_s:
            variables.goingDown = True
        elif variables.ev.key == pygame.K_d:
            variables.goingRight = True
        elif (variables.ev.key == pygame.K_a):
            variables.goingLeft = True
    # MOVEMENT DETECTION (STOP)
    if variables.ev.type == pygame.KEYUP: # if key released
        if variables.ev.key == pygame.K_w: # if key is w
            variables.goingUp = False; # update movement boolean
        elif variables.ev.key == pygame.K_s: 
            variables.goingDown = False; 
        elif variables.ev.key == pygame.K_d:
            variables.goingRight = False; 
        elif variables.ev.key == pygame.K_a:
            variables.goingLeft = False; 
    
    # PLAYER BEEF COLLISION DETECTION
    if pygame.sprite.collide_rect(player, beef): # if player rectangle collides with beef wellington rectangle
        fishing.initFishing()
        variables.gameState = "fishing" # go to fishing level
        powerupSound.play()

    # DRAW GRASS
    for y in range(0, variables.screenY, 16): # for # of rows on screen (Y value), increase by 16 each loop
        if(y >= 336): # if on lower screen
            for x in range(0, variables.screenX, 16): # draw light grass tiles
                variables.screen.blit(grassImage, (x, y), (0, 144, 16, 16))
        else: # if on higher screen
            for x in range(0, variables.screenX, 16): # draw dark grass tiles
                variables.screen.blit(grassImage, (x, y), (0, 128, 16, 16))

    # DRAW TREES
    variables.screen.blit(tree1, (60,120)); variables.screen.blit(tree1, (500,230)); variables.screen.blit(tree1, (800,90)); variables.screen.blit(tree1, (1190,130)) # draw dark trees
    variables.screen.blit(tree2, (300,400)); variables.screen.blit(tree2, (750,480)); variables.screen.blit(tree2, (1050,370)) # draw light trees

    # GORDON TALKING SEQUENCE
    if(variables.gordonTalking == True): # if tutorial text is active
        variables.screen.blit(gordonPixelImage, (-20, 490)) # display gordon pixel image
        if(variables.tutorialText == 1): # depending on current dialogue, display text
            variables.screen.blit(tutorialText1, (160, 600))
        elif(variables.tutorialText == 2):
            variables.screen.blit(tutorialText2, (160, 600))
        elif(variables.tutorialText == 3):
            variables.screen.blit(tutorialText3, (160, 600))
        elif(variables.tutorialText == 4):
            variables.screen.blit(tutorialText4, (160, 600))
        elif(variables.tutorialText == 5):
            variables.screen.blit(tutorialText5, (160, 600))
        elif(variables.tutorialText == 6):
            variables.screen.blit(tutorialText6, (160, 600))

    beef.draw(variables.screen) # draw beef wellington object
    player.draw(variables.screen) # draw player object