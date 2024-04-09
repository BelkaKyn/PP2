import pygame
import sys
import random
from pygame.locals import *

# Инициализация Pygame
pygame.init()

# Установка FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Создание цветов
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Переменные для игры
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
ENEMY_SPEED = SPEED
# Установка шрифтов
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over_text = font.render("Game Over", True, BLACK)

background = pygame.image.load("AnimatedStreet.png")

# Создание окна
DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, ENEMY_SPEED)
        if self.rect.top > 600:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)


# Создание класса монет
class Coin(pygame.sprite.Sprite):
    def __init__(self, size=(30, 30)):
        super().__init__()
        self.image = pygame.image.load("coin.png").convert_alpha()
        if size == (30, 30):
            self.image = pygame.transform.scale(self.image, (30, 30))
            self.points = 1
        elif size == (40, 40):
            self.image = pygame.transform.scale(self.image, (40, 40))
            self.points = 1
        elif size == (50, 50):
            self.image = pygame.transform.scale(self.image, (50, 50))
            self.points = 1
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 30), 0)


# Создание класса монет1
class Coin1(pygame.sprite.Sprite):
    def __init__(self, size=(50, 50)):
        super().__init__()
        self.image = pygame.image.load("coin1.png").convert_alpha()
        if size == (50, 50):
            self.image = pygame.transform.scale(self.image, (50, 50))
            self.points = 3
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


# Создание спрайтов
P1 = Player()
E1 = Enemy()

# Создание групп спрайтов
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

# Создание группы монет
coins = pygame.sprite.Group()
coins1 = pygame.sprite.Group()

# Создание монет и добавление их в группу all_sprites
for _ in range(2): 
    coin = Coin()
    coins.add(coin)
    all_sprites.add(coin)

for _ in range(1): 
    coin1 = Coin1()
    coins1.add(coin1)
    all_sprites.add(coin1)

# Создание текста для отоброжения монеток
coin_font = pygame.font.SysFont("Verdana", 20)
coin_text = coin_font.render("Coins: 0", True, BLACK)
coin_text_rect = coin_text.get_rect(topright=(SCREEN_WIDTH - 100, 10))

# Основной игровой цикл
while True:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Создание монет и добавление их в группу all_sprites
    for _ in range(2 - len(coins)):  
        coin = Coin()
        coins.add(coin)
        all_sprites.add(coin)

    for _ in range(1 - len(coins1)):  
        coin1 = Coin1()
        coins1.add(coin1)
        all_sprites.add(coin1)

    # Очистка экрана
    DISPLAYSURF.blit(background, (0, 0))

    # Отображение счетчика монет
    DISPLAYSURF.blit(coin_text, coin_text_rect)

    # Перемещение и перерисовка всех спрайтов
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # Проверка столкновений монет с игроком и обновление счетчика монет
    for coin in pygame.sprite.spritecollide(P1, coins, True):
        SCORE += coin.points
        coin_text = coin_font.render("Coins: {}".format(SCORE), True, BLACK)

    for coin1 in pygame.sprite.spritecollide(P1, coins1, True):
        SCORE += coin1.points
        coin_text = coin_font.render("Coins: {}".format(SCORE), True, BLACK)
    
    if SCORE % 10 == 0 and SCORE != 0:
        ENEMY_SPEED += 0.01
        
    #   Проверка столкновений врагов с игроком
    if pygame.sprite.spritecollide(P1, enemies, False):
        DISPLAYSURF.blit(game_over_text, (30, 250))
        pygame.display.update()
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()

    # Обновление дисплея
    pygame.display.update()
    FramePerSec.tick(FPS)
