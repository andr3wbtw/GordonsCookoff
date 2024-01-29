#-----------------------------------------------------------------------------
# Name:        Gordon's Cookoff (main.py)
# Purpose:     Gordon's Cookoff is a 2D cooking challenge game, written entirely
#              in python. The goal is to complete all three of Gordon's challenges
#              to beat the game. Find various easter eggs and rare lose screens
#              in order to enjoy all the content that this game has to offer.
#
# Author:      Andrew Myrden
# Created:     15-Jan-2024
# Updated:     23-Jan-2024
#-----------------------------------------------------------------------------
#I think this project deserves a level 4+ because...
#   Gordon's Cookoff meets all the 4+ criteria mentioned in the rubric, and it goes
#   above and beyond all the concepts that we have learned throughout the year.
#   The code is very well organized internally and is separated into multiple files
#   for easier navigation. This year, I focused on making as much of the game object
#   oriented as I could, to take a more realistic approach for modern-day coding. 
#
#
#Features Added:
#   - Event Handler
#   - Directional Player Sprite
#   - Scrolling Menu
#   - Gun & Bullet Mechanics
#   - Randomized Characters (fish, potatoes, chickens)
#   - Collision Detection via colliderect and collidepoint
#   - Hands-on Tutorial
#   - Randomized Lose Screens
#   - Sound Effects and Music
#   - Gordon Ramsay Voice using AI
#   - Other Hidden Easter Eggs
#
#-----------------------------------------------------------------------------
#References:
#   Bullet Firing and Collision Inspired By:
#       https://stackoverflow.com/a/63496491
#
#-----------------------------------------------------------------------------

import pygame
from pygame.locals import*

import menu
import tutorial
import variables
import fishing
import fail
import steakCooking
import chicken
import win

pygame.mixer.music.load('sounds/music.wav')
pygame.mixer.music.play()

def main():
    ### MAIN GAME LOOP ###
    while True:
        variables.ev = pygame.event.poll()    # Look for any event

        variables.mouse = pygame.mouse.get_pos() # track mouse X and Y position
        variables.mouseX = variables.mouse[0]
        variables.mouseY = variables.mouse[1]

        if variables.ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop
            
        if variables.gameState == "menu": # menu state
            menu.menu()

        if variables.gameState == "tutorial": # tutorial state
            tutorial.tutorial()

        if variables.gameState == "fishing": # fishing state
            fishing.fishing()

        if variables.gameState == "fail": # fail state
            fail.fail()

        if variables.gameState == "steak": # steak cooking state
            steakCooking.steakCooking()

        if variables.gameState == "chicken": # chicken catch state
            chicken.chicken()

        if variables.gameState == "win": # win state
            win.win()

        variables.timer+= 1 # tick the timer

        pygame.display.flip()
    pygame.quit()

main()