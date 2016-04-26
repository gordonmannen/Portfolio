# Game - TJ Pig

import pygame
import time
import sys
 
# Defines some basic colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Sets the width and height of the screen [width, height]
size = (1080, 720)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("TJ Pig")
 
# Loop will continue until user clicks the close button.
done = False
 
# clock effects the speed at which the screen will update.
clock = pygame.time.Clock()

# Background for game screen
background_image = pygame.image.load("farm.jpg").convert()

# player (TJ Pig) image
player_image = pygame.image.load("coolFlyingPig.png").convert()
player_image.set_colorkey(WHITE)
oink_sound = pygame.mixer.Sound("oink.wav")

# Hide mouse cursor
pygame.mouse.set_visible(False)

def oink_text(screen, text = "Oink, Oink!", x = 500, y = 350, size = 50, color = (0, 0, 0), font_type = 'Calibri'):

    try:
        text = str(text)
        font = pygame.font.SysFont(font_type, size)
        text = font.render(text, True, color)
        screen.blit(text, (x, y))

    except Exception as e:
        print("Font Error, I'm sorry you don't have Calibri")
        raise e

# -------- Main Game Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            oink_sound.play()


           

    # main event loop above, other events below
 
    # Calls the various images that will be drawn.
    screen.blit(background_image, [0,0])

    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    y = player_position[1]
    screen.blit(player_image, [x,y] )
    oink_text(screen)


    
 
    # --- Updates the game screen with what has been drawn.
    pygame.display.flip()
 
    # --- Limits FPS to 60
    clock.tick(60)
 
# Closes the game window and quits.
pygame.quit()