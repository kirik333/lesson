import pygame
from pygame import*
import random

#Объявляем переменные
WIN_WIDTH = 800 #Ширина создаваемого окна
WIN_HEIGHT = 640 # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT) # Группируем ширину и высоту в одну переменную
BACKGROUND_COLOR = "#004400"
PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
DISPLAY123 = (PLATFORM_WIDTH, PLATFORM_HEIGHT)
PLATFORM_COLOR = "#FF6262"

def main():
    pygame.init() # Инициация PyGame, обязательная строчка 
    screen = pygame.display.set_mode(DISPLAY) # Создаем окошко
    pygame.display.set_caption("Super Mario Boy") # Пишем в шапку
    bg = Surface((WIN_WIDTH,WIN_HEIGHT)) # Создание видимой поверхности
                                         # будем использовать как фон
    bg.fill(Color(BACKGROUND_COLOR))# Заливаем поверхность сплошным цветом
    bg123 = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
    bg123.fill(Color(PLATFORM_COLOR))
    x = 50
    y = 50
    a = 1
    b = 1

    while 1: # Основной цикл программы
        for e in pygame.event.get(): # Обрабатываем события
            if e.type == QUIT:
                raise SystemExit
        screen.blit(bg, (0,0))      # Каждую итерацию необходимо всё перерисовывать
        screen.blit(bg123,(x,y))
        x+=a
        y+=b
        if y == WIN_HEIGHT - PLATFORM_HEIGHT:
            a = random.randint(-2,2)
            b = random.randint(1,2)*-1  #надо
        if y == 0 + PLATFORM_HEIGHT:
            a = random.randint(-2,2)
            b = random.randint(1,2)     #надо
        if x == WIN_WIDTH - PLATFORM_WIDTH:
            a = random.randint(1,2)*-1  #надо
            b = random.randint(-2,2)
        if x == 0 + PLATFORM_WIDTH:
            a = random.randint(1,2)     #надо
            b = random.randint(-2,2)
            
        pygame.display.update()     # обновление и вывод всех изменений на экран
        

if __name__ == "__main__":
    main()
