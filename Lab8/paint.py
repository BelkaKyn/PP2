import pygame
import sys

pygame.init()


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(WHITE)  
pygame.display.set_caption("Simple Paint")

brush_color = BLACK
brush_size = 5
drawing = False
last_pos = None
start_pos = None
rectangle_mode = False  
circle_mode = False  
eraser_mode = False  
while True:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  
                drawing = True
                if rectangle_mode or circle_mode:
                    start_pos = event.pos
                else:
                    last_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1: 
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
                    brush_color = WHITE  
                pygame.draw.line(screen, brush_color, last_pos, event.pos, brush_size)
                last_pos = event.pos
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:  
                circle_mode = not circle_mode
                rectangle_mode = False
                eraser_mode = False
            elif event.key == pygame.K_f: 
                rectangle_mode = not rectangle_mode
                circle_mode = False
                eraser_mode = False
            elif event.key == pygame.K_e:  
                eraser_mode = not eraser_mode
                rectangle_mode = False
                circle_mode = False
            elif event.key == pygame.K_p:  
                brush_color = BLACK
            elif event.key == pygame.K_r:  
                brush_color = RED
            elif event.key == pygame.K_g:  
                brush_color = GREEN
            elif event.key == pygame.K_b:  
                brush_color = BLUE
            elif event.key == pygame.K_s:  
                brush_size = max(1, brush_size - 1)
            elif event.key == pygame.K_l: 
                brush_size += 1

   
    pygame.display.flip()
    