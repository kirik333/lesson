import pygame
import random
from pygame import *
from RandomList import*

PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#FF6262"
WIN_WIDTH = 800
WIN_HEIGHT = 640
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND_COLOR = "#004400"

def main():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("Super Mario Boy")
    bg = Surface((PLATFORM_WIDTH,PLATFORM_HEIGHT))
    bg.fill(Color(PLATFORM_COLOR))
    x=0
    y=0
    a=1
    b=1
    while 1:
        for e in pygame.event.get():
            if e.type == QUIT:
                raise SystemExit
        x+=a
        y+=b
        if y >= WIN_HEIGHT - PLATFORM_HEIGHT:
            a = random.randint(-2,2)
            b = random.randint(1,2)*-1            
        if y<=0:
            a = random.randint(-2,2)
            b = random.randint(1,2)
        if x>=WIN_WIDTH - PLATFORM_WIDTH:
            a = random.randint(1,2)*-1
            b = random.randint(-2,2)
        if x<=0:
            a = random.randint(1,2)
            b = random.randint(-2,2)     
        screen.fill(Color(BACKGROUND_COLOR))
        screen.blit(bg, (x,y))
        pygame.display.update()
         
                 
if __name__ == "__main__":
    main()
