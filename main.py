import pygame
import os
import random
from pygame.locals import*

import menu
import tutorial
import variables

def main():
    ### MAIN GAME LOOP ###
    while True:
        variables.ev = pygame.event.poll()    # Look for any event

        variables.mouse = pygame.mouse.get_pos() # track mouse X and Y position
        variables.mouseX = variables.mouse[0]
        variables.mouseY = variables.mouse[1]

        if variables.ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop
        '''if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_w:
                variables.goingUp = True
            elif ev.key == pygame.K_s:
                variables.goingDown = True
            elif ev.key == pygame.K_d:
                variables.goingRight = True
            elif (ev.key == pygame.K_a) and (variables.enviroPosX < 570):
                variables.goingLeft = True
        if ev.type == pygame.KEYUP:
            if ev.key == pygame.K_w:
                variables.goingUp = False; variables.animateNum = 0
            elif ev.key == pygame.K_s: 
                variables.goingDown = False; variables.animateNum = 0
            elif ev.key == pygame.K_d:
                variables.goingRight = False; variables.animateNum = 0
            elif ev.key == pygame.K_a:
                variables.goingLeft = False; variables.animateNum = 0'''
            
        if variables.gameState == "menu": # menu state
            menu.menu()

        pygame.display.flip()
        if variables.gameState == "tutorial":
            tutorial.tutorial()

        variables.timer+= 1 # tick the timer

        pygame.display.flip()
    pygame.quit()

main()