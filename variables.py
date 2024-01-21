import pygame

# Images #
iconImage = pygame.image.load('images/icon.png')

# # # # # # # # # # # # # # # # # # # # # # # # #
# Essentials #
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()  #Force frame rate to be slower
pygame.display.set_caption("Gordon's Cookoff") # change window name
pygame.display.set_icon(iconImage) # change window icon
gameState = "menu"

ev = pygame.event.poll() # EVENT POLL
# # # # # # # # # # # # # # # # # # # # # # # # #
# Colors #
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
red = pygame.Color(255,0,0)
blue = pygame.Color(0,0,255)
brown = pygame.Color(26,15,6)
# # # # # # # # # # # # # # # # # # # # # # # # #
# Fonts #
tastyFont = pygame.font.Font('fonts/TastyFood.otf',100)
tastyBoldFont = pygame.font.Font('fonts/TastyFoodBold.otf',120)
crispyFoodFont = pygame.font.Font('fonts/CrispyFood.ttf',60)
talkingFont = pygame.font.Font('fonts/CrispyFood.ttf',40)
# # # # # # # # # # # # # # # # # # # # # # # # #

info = pygame.display.Info()
w = info.current_w
h = info.current_h

gordonTalking = False
tutorialText = 1

screenX = 1280
screenY = 680
screen = pygame.display.set_mode((screenX, screenY))

mouse = pygame.mouse.get_pos() # track mouse X and Y position
mouseX = mouse[0]
mouseY = mouse[1]

start = (10, 10)
end = start
bulletSpeed = 2

speed = 1
fishSpeed = 10 #3 before
fishShot = False
talkStatus = "intro"

potatoCollected = False
potatoTimerBegin = 0
potatoTimerEnd = 0
potatoTimer = 5

fireDirection = "right"
fireSpeed = -8
fireX = 0

bucketX = 0
bucketSpeed = -4
bucketDirection = "none"

steaksCooked = 0
steakDetection = False

failSequence = "chicken"

ammo = 5

goingUp = False
goingDown = False
goingRight = False
goingLeft = False

animateNum = 0
sheetNum = 0

timer = 0
localFlashTimer = 0
menuFlash = False