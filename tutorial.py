import pygame
pygame.font.init()
import variables
import fishing

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
        if(self.rect.y >= -50):
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

class BeefWellington(pygame.sprite.Sprite):
    def __init__(self, dx, dy, filename):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = dx
        self.rect.y = dy
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

gordonPixelImage = pygame.image.load('images/gordPixels.png')
gordonPixelImageRect = gordonPixelImage.get_rect(center=(variables.screenX/2, variables.screenY/2))

characterImage = pygame.image.load('images/character/idle/1.png')

grassImage = pygame.image.load('images/grass.png')

tree1 = pygame.image.load('images/Tree1.png')
tree2 = pygame.image.load('images/Tree2.png')

tutorialText = ["Welcome to my cookoff!", "Use WASD to move" "Good luck!"]
tutorialText1 = variables.talkingFont.render("(Press space to continue conversation)", True, variables.white)
tutorialText2 = variables.talkingFont.render("Welcome to my cookoff..", True, variables.white)
tutorialText3 = variables.talkingFont.render("Use WASD to move..", True, variables.white)
tutorialText4 = variables.talkingFont.render("I have three cooking challenges for you..", True, variables.white)
tutorialText5 = variables.talkingFont.render("Collect my Beef Wellington to begin..", True, variables.white)
tutorialText6 = variables.talkingFont.render("Don't disappoint me.", True, variables.white)

player = Player(200, 200, 'images/character/idle/1.png')
beef = BeefWellington(700, 300, 'images/beefwellington.png')

def initTutorial():
    variables.goingUp = False
    variables.goingDown = False
    variables.goingRight = False
    variables.goingLeft = False
    variables.gordonTalking = True
    variables.tutorialText = 1
    player.rect.x = 200
    player.rect.y = 200

def tutorial():
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
                if(variables.tutorialText < 6):
                    variables.tutorialText += 1
                elif(variables.tutorialText == 6):
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
    
    # PLAYER BEEF COLLISION DETECTION
    if pygame.sprite.collide_rect(player, beef):
        fishing.initFishing()
        variables.gameState = "fishing"

    # DRAW GRASS
    for y in range(0, variables.screenY, 16):
        if(y >= 336):
            for x in range(0, variables.screenX, 16):
                variables.screen.blit(grassImage, (x, y), (0, 144, 16, 16))
        else:
            for x in range(0, variables.screenX, 16):
                variables.screen.blit(grassImage, (x, y), (0, 128, 16, 16))

    # DRAW TREES
    variables.screen.blit(tree1, (60,120)); variables.screen.blit(tree1, (500,230)); variables.screen.blit(tree1, (800,90)); variables.screen.blit(tree1, (1190,130))
    variables.screen.blit(tree2, (300,400)); variables.screen.blit(tree2, (750,480)); variables.screen.blit(tree2, (1050,370))

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
        elif(variables.tutorialText == 5):
            variables.screen.blit(tutorialText5, (160, 600))
        elif(variables.tutorialText == 6):
            variables.screen.blit(tutorialText6, (160, 600))

    beef.draw(variables.screen)

    player.draw(variables.screen)