import pygame
from constants import *


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

while True:
    fill(color, rect=None, special_flags=0)
    pygame.display.flip()

def main ():
    print ("Starting Asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()