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

        if variables.gameState == "tutorial":
            tutorial.tutorial()

        if variables.gameState == "fishing":
            fishing.fishing()

        if variables.gameState == "fail":
            fail.fail()

        if variables.gameState == "steak":
            steakCooking.steakCooking()

        if variables.gameState == "chicken":
            chicken.chicken()

        if variables.gameState == "win":
            win.win()

        variables.timer+= 1 # tick the timer

        pygame.display.flip()
    pygame.quit()

main()