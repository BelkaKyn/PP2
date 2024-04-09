import pygame
import sys

# Инициализация Pygame
pygame.init()

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Размеры экрана
WIDTH, HEIGHT = 800, 600

# Создание экрана и его заполнение белым цветом
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(WHITE)  # Заполнение экрана белым цветом
pygame.display.set_caption("Simple Paint")

# Параметры кисти
brush_color = BLACK
brush_size = 5
drawing = False
last_pos = None
start_pos = None
rectangle_mode = False  # Флаг режима рисования прямоугольника
circle_mode = False  # Флаг режима рисования круга
eraser_mode = False  # Флаг режима ластика

# Основной цикл программы
while True:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Левая кнопка мыши для рисования
                drawing = True
                if rectangle_mode or circle_mode:
                    start_pos = event.pos
                else:
                    last_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Отпустить левую кнопку мыши
                drawing = False
                if rectangle_mode:
                    rect_width = abs(event.pos[0] - start_pos[0])
                    rect_height = abs(event.pos[1] - start_pos[1])
                    pygame.draw.rect(screen, brush_color, (min(start_pos[0], event.pos[0]), min(start_pos[1], event.pos[1]), rect_width, rect_height), brush_size)
                elif circle_mode:
                    radius = max(abs(event.pos[0] - start_pos[0]), abs(event.pos[1] - start_pos[1]))
                    pygame.draw.circle(screen, brush_color, start_pos, radius, brush_size)
        elif event.type == pygame.MOUSEMOTION:
            if drawing and not rectangle_mode and not circle_mode:
                if eraser_mode:
                    brush_color = WHITE  # Установка цвета кисти на белый для ластика
                pygame.draw.line(screen, brush_color, last_pos, event.pos, brush_size)
                last_pos = event.pos
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:  # Переключение режима рисования круга по нажатии "C"
                circle_mode = not circle_mode
                rectangle_mode = False
                eraser_mode = False
            elif event.key == pygame.K_f:  # Переключение режима рисования прямоугольника по нажатии "F"
                rectangle_mode = not rectangle_mode
                circle_mode = False
                eraser_mode = False
            elif event.key == pygame.K_e:  # Переключение режима ластика по нажатии "E"
                eraser_mode = not eraser_mode
                rectangle_mode = False
                circle_mode = False
            elif event.key == pygame.K_p:  # Изменить цвет кисти при нажатии "P"
                brush_color = BLACK
            elif event.key == pygame.K_r:  # Изменить цвет кисти при нажатии "R"
                brush_color = RED
            elif event.key == pygame.K_g:  # Изменить цвет кисти при нажатии "G"
                brush_color = GREEN
            elif event.key == pygame.K_b:  # Изменить цвет кисти при нажатии "B"
                brush_color = BLUE
            elif event.key == pygame.K_s:  # Уменьшить размер кисти при нажатии "S"
                brush_size = max(1, brush_size - 1)
            elif event.key == pygame.K_l:  # Увеличить размер кисти при нажатии "L"
                brush_size += 1

    # Обновление экрана
    pygame.display.flip()
    