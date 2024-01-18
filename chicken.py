import pygame
pygame.font.init()
import variables
import fail
import math
import random

tutorialText1 = variables.talkingFont.render("Your next challenge is to cook some steak..", True, variables.black)
tutorialText2 = variables.talkingFont.render("Press space bar when the temperature is in the middle!", True, variables.black)
tutorialText3 = variables.talkingFont.render("Impressive.. onto my last challenge.", True, variables.black)

def initChicken():
    print("initialized chicken")

def chicken():
    variables.screen.fill(variables.black)