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

target_x = random.randint(0,SCREEN_WIDTH-target_width) # андомная координата лев верх. угла цели
target_y = random.randint(0, SCREEN_HEIGHT-target_height)

color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        #зададим переменную цвета для заливки фона всего окна игры- рандомные цвета



running = True
while running:
    screen.fill(color) # заполняем окно игры рандомным цветом из переменной color
    for event in pygame.event.get():  #все события в игре сохраняются в виде коллекции(с пом.pygame.event.get()) и цикл for м.эту коллекцию перебрать.

                                        #на каждой итерации событие из коллекции сохр-ся в переменную event
        if event.type == pygame.QUIT:
            running = False  #завершаем цикл и мы можем норм выйти из игры. Если это не сделать, игра зависнет при наж на крестик
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos() #если мышь нажата, определяет координаты клика мышью. get_pos() -получаем коор-ты в виде кортежа и соотв, запис их в две переменные
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)  #попали ли мы в диапазон цели? (начало координат цели - target_x, а target_x+target_width - правая граница цели, (левая х +ширина цели)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
    screen.blit(target_img, (target_x, target_y)) #отрисуем мишень.с пом спец.ф-ции blit(), и разместим мишень на определенных координатах
    pygame.display.update() #Обновляем экран с новым расположением мишени
pygame.quit()