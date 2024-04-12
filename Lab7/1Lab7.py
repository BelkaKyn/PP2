import pygame
import sys
from datetime import datetime

pygame.init()

# Установка ширины и высоты экрана 
SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 1000
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Clock")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Загрузка изображений для стрелок и фона часов
minute_hand_image = pygame.image.load("minute_hand.png").convert_alpha()
second_hand_image = pygame.image.load("second_hand.png").convert_alpha()
clock_face_image = pygame.image.load("clock_face.png").convert_alpha()

def blit_rotate_center(surf, image, topleft, angle):
    """Поворачивает изображение вокруг его центра"""
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=topleft).center)
    surf.blit(rotated_image, new_rect.topleft)

def draw_clock_hands():
    """Отрисовывает часы на экране"""
    # Получение времени
    current_time = datetime.now().time()
    seconds = current_time.second
    minutes = current_time.minute

    # Расчет углов поворота для стрелок
    seconds_angle = -(seconds / 60) * 360 + 90
    minutes_angle = -(minutes / 60) * 360 + 90

    # Отрисовка фона часов
    screen.blit(clock_face_image, (0, 0))

    # Отрисовка стрелок
    blit_rotate_center(screen, second_hand_image, (500, 350), seconds_angle)
    blit_rotate_center(screen, minute_hand_image, (540, 400), minutes_angle)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Заполнение фона
    screen.fill(WHITE)

    # Отрисовка стрелок и фона часов
    draw_clock_hands()

    # Обновление дисплея
    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
