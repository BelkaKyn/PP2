import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    points = []
    shapes = []
    
    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
            
                # determine if a letter key was pressed
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_e:
                    mode = 'erase'
                elif event.key == pygame.K_c:
                    mode = 'circle'
                elif event.key == pygame.K_p:
                    mode = 'polygon'
                elif event.key == pygame.K_s:
                    mode = 'square'
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # left click grows radius
                    if mode != 'polygon':
                        radius = min(200, radius + 1)
                elif event.button == 3: # right click shrinks radius
                    if mode != 'polygon':
                        radius = max(1, radius - 1)
                elif event.button == 4: # scroll up
                    radius = min(200, radius + 5)
                elif event.button == 5: # scroll down
                    radius = max(1, radius - 5)
                elif event.button == 2: # middle click clears screen
                    points = []
                    shapes = []
            
            if event.type == pygame.MOUSEMOTION:
                # if mouse moved, add point to list
                position = event.pos
                if mode == 'erase':
                    points = [p for p in points if pygame.math.Vector2(p).distance_to(position) > radius]
                else:
                    points = points + [position]
                    points = points[-256:]
                
                if mode == 'circle':
                    shapes = [(mode, (255, 0, 0), position, radius)]
                elif mode == 'polygon':
                    shapes = [(mode, (0, 255, 0), points)]
                elif mode == 'square':
                    shapes = [(mode, (0, 0, 255), position, radius)]
        
        screen.fill((0, 0, 0))
        
        # draw all points
        i = 0
        while i < len(points) - 1:
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
            i += 1
        
        # draw all shapes
        for shape in shapes:
            drawShape(screen, shape)
        
        pygame.display.flip()
        
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    elif color_mode == 'erase':
        color = (0, 0, 0)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

def drawShape(screen, shape):
    mode, color, *args = shape
    if mode == 'circle':
        position, radius = args
        pygame.draw.circle(screen, color, position, radius)
    elif mode == 'polygon':
        points = args[0]
        pygame.draw.polygon(screen, color, points)
    elif mode == 'square':
        position, radius = args
        pygame.draw.rect(screen, color, (position[0]-radius, position[1]-radius, radius*2, radius*2))

main()
