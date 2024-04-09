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
square_mode = False  # Флаг режима рисования квадрата
circle_mode = False  # Флаг режима рисования круга
triangle_mode = False  # Флаг режима рисования треугольника
iso_triangle_mode = False  # Флаг режима рисования равнобедренного треугольника
rhombus_mode = False  # Флаг режима рисования ромба
eraser_mode = False  # Флаг режима ластика


def draw_iso_triangle(screen, top, base_length, height, color, thickness):
    """Рисует равнобедренный треугольник с вершиной в указанной точке, длиной основания, высотой и цветом"""
    half_base = base_length / 2
    points = [
        (top[0], top[1]),  # Вершина
        (top[0] - half_base, top[1] + height),  # Левый угол
        (top[0] + half_base, top[1] + height)  # Правый угол
    ]
    pygame.draw.polygon(screen, color, points, thickness)


def draw_rhombus(screen, top, side_length, color, thickness):
    """Рисует ромб с верхней точкой в указанной точке, длиной стороны и цветом"""
    half_side = side_length / 2
    points = [
        (top[0], top[1]),  # Верхняя точка
        (top[0] - half_side, top[1] + half_side),  # Левая нижняя точка
        (top[0], top[1] + 2 * half_side),  # Нижняя точка
        (top[0] + half_side, top[1] + half_side)  # Правая нижняя точка
    ]
    pygame.draw.polygon(screen, color, points, thickness)


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
            if rectangle_mode or circle_mode or square_mode or triangle_mode or iso_triangle_mode or rhombus_mode:
                    start_pos = event.pos  # Инициализация start_pos здесь
            else:
                    last_pos = event.pos

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Отпустить левую кнопку мыши
                drawing = False
                if rectangle_mode:
                    rect_width = abs(event.pos[0] - start_pos[0])
                    rect_height = abs(event.pos[1] - start_pos[1])
                    pygame.draw.rect(screen, brush_color, (min(start_pos[0], event.pos[0]), min(start_pos[1], event.pos[1]), rect_width, rect_height), brush_size)
                elif square_mode:
                    side_length = max(abs(event.pos[0] - start_pos[0]), abs(event.pos[1] - start_pos[1]))
                    pygame.draw.rect(screen, brush_color, (start_pos[0], start_pos[1], side_length, side_length), brush_size)
                elif circle_mode:
                    radius = max(abs(event.pos[0] - start_pos[0]), abs(event.pos[1] - start_pos[1]))
                    pygame.draw.circle(screen, brush_color, start_pos, radius, brush_size)
                elif triangle_mode:
                    side_length = max(abs(event.pos[0] - start_pos[0]), abs(event.pos[1] - start_pos[1]))
                    pygame.draw.polygon(screen, brush_color, [(start_pos[0], start_pos[1]), (event.pos[0], event.pos[1]), (start_pos[0] + side_length, start_pos[1])], brush_size)
                elif iso_triangle_mode:
                    base_length = max(abs(event.pos[0] - start_pos[0]), abs(event.pos[1] - start_pos[1]))
                    height = base_length * (3 ** 0.5) / 2  # Формула высоты равнобедренного треугольника
                    draw_iso_triangle(screen, start_pos, base_length, height, brush_color, brush_size)
                elif rhombus_mode:
                    side_length = max(abs(event.pos[0] - start_pos[0]), abs(event.pos[1] - start_pos[1]))
                    draw_rhombus(screen, start_pos, side_length, brush_color, brush_size)
                elif eraser_mode:
                    pygame.draw.circle(screen, WHITE, event.pos, brush_size)  # "Стирание" цвета
        elif event.type == pygame.MOUSEMOTION:
            if drawing and not (rectangle_mode or circle_mode or square_mode or triangle_mode or iso_triangle_mode or eraser_mode or rhombus_mode):
                # Рисование линии между предыдущей и текущей позицией
                pygame.draw.line(screen, brush_color, last_pos, event.pos, brush_size)
                last_pos = event.pos
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:  # Очистить экран при нажатии "C"
                screen.fill(WHITE)  # Заполнить экран белым цветом
            elif event.key == pygame.K_b:  # Изменить цвет кисти при нажатии "B"
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
            elif event.key == pygame.K_f:  # Активировать режим рисования прямоугольника
                rectangle_mode = not rectangle_mode
                circle_mode = False
                square_mode = False
                triangle_mode = False
                iso_triangle_mode = False
                rhombus_mode = False
                eraser_mode = False
            elif event.key == pygame.K_s:  # Активировать режим рисования квадрата
                square_mode = not square_mode
                rectangle_mode = False
                circle_mode = False
                triangle_mode = False
                iso_triangle_mode = False
                rhombus_mode = False
                eraser_mode = False
            elif event.key == pygame.K_c:  # Активировать режим рисования круга
                circle_mode = not circle_mode
                rectangle_mode = False
                square_mode = False
                triangle_mode = False
                iso_triangle_mode = False
                rhombus_mode = False
                eraser_mode = False
            elif event.key == pygame.K_t:  # Активировать режим рисования треугольника
                triangle_mode = not triangle_mode
                rectangle_mode = False
                square_mode = False
                circle_mode = False
                iso_triangle_mode = False
                rhombus_mode = False
                eraser_mode = False
            elif event.key == pygame.K_i:  # Активировать режим рисования равнобедренного треугольника
                iso_triangle_mode = not iso_triangle_mode
                rectangle_mode = False
                square_mode = False
                circle_mode = False
                triangle_mode = False
                rhombus_mode = False
                eraser_mode = False
            elif event.key == pygame.K_e:  # Активировать режим ластика
                eraser_mode = not eraser_mode
                rectangle_mode = False
                square_mode = False
                circle_mode = False
                triangle_mode = False
                iso_triangle_mode = False
                rhombus_mode = False
            elif event.key == pygame.K_o:  # Активировать режим рисования ромба
                rhombus_mode = not rhombus_mode
                rectangle_mode = False
                square_mode = False
                circle_mode = False
                triangle_mode = False
                iso_triangle_mode = False
                eraser_mode = False

    # Обновление экрана
    pygame.display.flip()
