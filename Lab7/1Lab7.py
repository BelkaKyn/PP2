import pygame
import sys
from datetime import datetime

pygame.init()

# Установка ширины и высоты экрана 
SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 1000
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Микки Маус Часы")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Загрузка изображений для стрелок и фона часов
minute_hand_image = pygame.image.load("minute_hand.png").convert_alpha()
second_hand_image = pygame.image.load("second_hand.png").convert_alpha()
clock_face_image = pygame.image.load("clock_face.png").convert_alpha()

def rot_center(image, angle):
    """Поворачивает изображение, сохраняя его центр и размер"""
    # Получаем исходный прямоугольник изображения
    orig_rect = image.get_rect()
    # Поворачиваем изображение
    rot_image = pygame.transform.rotate(image, angle)
    # Получаем прямоугольник нового повернутого изображения
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    # Пересекаем прямоугольник повернутого изображения с прямоугольником исходного изображения
    subsurf_rect = rot_rect.clip(image.get_rect())
    return rot_image


# Основная функция отрисовки часов
def draw_clock_hands():
    # Получение текущего времени
    current_time = datetime.now().time()
    seconds = current_time.second
    minutes = current_time.minute

    # Расчет углов поворота для стрелок
    seconds_angle = -(seconds / 60) * 360 + 90
    minutes_angle = -(minutes / 60) * 360 + 90

    # Поворот и отрисовка стрелок
    rotated_second_hand = rot_center(second_hand_image, seconds_angle)
    rotated_minute_hand = rot_center(minute_hand_image, minutes_angle)
    
   

    # Расчет позиций стрелок
    second_hand_rect = rotated_second_hand.get_rect(center=(600, 450))
    minute_hand_rect = rotated_minute_hand.get_rect(center=(600, 300))


    # Отрисовка фона часов
    screen.blit(clock_face_image, (0, 0))

    # Отрисовка стрелок
    screen.blit(rotated_second_hand, second_hand_rect)
    screen.blit(rotated_minute_hand, minute_hand_rect)

# Основной цикл
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

    # Управление частотой кадров
    pygame.time.Clock().tick(60)

# Завершение работы Pygame
pygame.quit()
sys.exit()
