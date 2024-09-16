import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Игра Тир')  #set_caption - ф-ция для установки заголовка окна
icon = pygame.image.load("img/Strelki.jpg")
pygame.display.set_icon(icon)  #Устанавливаем иконку icon-переменная, в которую ранее сохранили картинку

target_img = pygame.image.load('img/target.png')  # в папке img/ будет картинка с целью, пока-пусто
target_width = 140  #зададим ширину и высоту цели
target_height = 140

target_x = random.randint(0,SCREEN_WIDTH-target_width)
target_y = random.randint(0, SCREEN_HEIGHT-target_height)

color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        #зададим переменную цвета для заливки фона всего окна игры- рандомные цвета



running = True
while running:
    pass
pygame.quit()