import pygame
from pygame import*
import pygame
pygame.init()
size = [800, 600]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
                # пишем свой код
    # обновляем значения
    screen.fill((200, 100, 0))
    pygame.draw.rect(screen, (0, 255, 0), ((300, 150), (100, 150)))
    pygame.display.flip()
    clock.tick(30)
pygame.quit()
