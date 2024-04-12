import pygame
import sys

# Инициализация Pygame
pygame.init()

# Установка размеров экрана
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Moving Ball")

# Определение цветов
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Создание шара
ball_radius = 25
ball_x = (SCREEN_WIDTH - ball_radius * 2) // 2
ball_y = (SCREEN_HEIGHT - ball_radius * 2) // 2
ball_speed = 20

# Основной цикл программы
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if ball_y - ball_speed >= 0:
                    ball_y -= ball_speed
            elif event.key == pygame.K_DOWN:
                if ball_y + ball_speed <= SCREEN_HEIGHT - ball_radius * 2:
                    ball_y += ball_speed
            elif event.key == pygame.K_LEFT:
                if ball_x - ball_speed >= 0:
                    ball_x -= ball_speed
            elif event.key == pygame.K_RIGHT:
                if ball_x + ball_speed <= SCREEN_WIDTH - ball_radius * 2:
                    ball_x += ball_speed

    # Очистка экрана
    screen.fill(WHITE)

    # Рисование шара
    pygame.draw.circle(screen, RED, (ball_x + ball_radius, ball_y + ball_radius), ball_radius)

    # Обновление экрана
    pygame.display.flip()

# Выход из Pygame
pygame.quit()
sys.exit()
