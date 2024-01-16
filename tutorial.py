import pygame
pygame.font.init()
import variables

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
        self.rect.y = self.rect.y - variables.speed
    def moveDown(self):
        self.rect.y = self.rect.y + variables.speed
    def moveRight(self):
        self.rect.x = self.rect.x + variables.speed
    def moveLeft(self):
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

tutorialText = ["Welcome to my cookoff!", "Use WASD to move" "Good luck!"]
tutorialText1 = variables.talkingFont.render("(Press space to continue..)", True, variables.white)
tutorialText2 = variables.talkingFont.render("Welcome to my cookoff!", True, variables.white)
tutorialText3 = variables.talkingFont.render("Use WASD to move.", True, variables.white)
tutorialText4 = variables.talkingFont.render("I have three cooking challenges for you.", True, variables.white)
tutorialText5 = variables.talkingFont.render("Collect my Beef Wellington to continue.", True, variables.white)
tutorialText6 = variables.talkingFont.render("Don't disappoint me.", True, variables.white)

player = Player(200, 200, 'images/character/idle/1.png')
beef = BeefWellington(700, 300, 'images/beefwellington.png')

def initTutorial():
    variables.gordonTalking = True
    variables.tutorialText = 1

def tutorial():
    variables.screen.fill(variables.blue)

    if(variables.goingUp == True): # MOVEMENT UPDATING
        player.moveUp()
    if(variables.goingDown == True):
        player.moveDown()
    if(variables.goingRight == True):
        player.moveRight()
    if(variables.goingLeft == True):
        player.moveLeft()

    if variables.ev.type == pygame.KEYUP: # SPACE DETECTION
            if variables.ev.key == pygame.K_SPACE:
                if(variables.tutorialText < 6):
                    variables.tutorialText += 1
                elif(variables.tutorialText == 6):
                    variables.gordonTalking = False

    if variables.ev.type == pygame.KEYDOWN: # MOVEMENT DETECTION (START)
        if variables.ev.key == pygame.K_w:
            variables.goingUp = True
        elif variables.ev.key == pygame.K_s:
            variables.goingDown = True
        elif variables.ev.key == pygame.K_d:
            variables.goingRight = True
        elif (variables.ev.key == pygame.K_a):
            variables.goingLeft = True
    if variables.ev.type == pygame.KEYUP: # MOVEMENT DETECTION (STOP)
        if variables.ev.key == pygame.K_w:
            variables.goingUp = False; 
        elif variables.ev.key == pygame.K_s: 
            variables.goingDown = False; 
        elif variables.ev.key == pygame.K_d:
            variables.goingRight = False; 
        elif variables.ev.key == pygame.K_a:
            variables.goingLeft = False; 
    
    if pygame.sprite.collide_rect(player, beef): # PLAYER BEEF COLLISION DETECTION
        variables.gameState = "fishing"

    for y in range(0, variables.screenY, 16): # DRAW GRASS
        if(y >= 336):
            for x in range(0, variables.screenX, 16):
                variables.screen.blit(grassImage, (x, y), (0, 144, 16, 16))
        else:
            for x in range(0, variables.screenX, 16):
                variables.screen.blit(grassImage, (x, y), (0, 128, 16, 16))

    if(variables.gordonTalking == True): # GORDON TALKING SEQUENCE
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