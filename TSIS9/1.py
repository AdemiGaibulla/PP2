#Imports
import pygame, sys
from pygame.locals import *
import random, time

#Initializing pygame
pygame.init()

#Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

#Colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Game variables
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COIN_SCORE = 0

#Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

#Background image
background = pygame.image.load("PP2/TSIS8/images/AnimatedStreet.png")

#Game screen
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

#Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("PP2/TSIS8/images/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(80, SCREEN_WIDTH - 80), 0) #random coordinates at the top(0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > 600:  #Reset enemy when it leaves screen
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(80, SCREEN_WIDTH - 80), 0)

#Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("PP2/TSIS8/images/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)  #Move left
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:        
            self.rect.move_ip(5, 0)  #Move right
                  
#Coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self, enemies):
        super().__init__()
        self.enemies = enemies
        self.spawn()  #Spawn at a safe location
        self.sound = pygame.mixer.Sound("PP2/TSIS8/melody/mixkit-game-success-alert-2039.wav")

    def spawn(self):
        size_options = {  
            "small": (20, 20, 1),
            "medium": (35, 35, 2),
            "large": (50, 50, 3) 
        }

        size_key = random.choice(list(size_options.keys()))  #Choosing random key
        new_size = size_options[size_key][:2] #Giving first two values
        new_score = size_options[size_key][2]

        original_image = pygame.image.load("PP2/TSIS8/images/Coin.png")
        self.image = pygame.transform.scale(original_image, new_size)
        self.rect = self.image.get_rect()

        self.value = new_score 

        while True:  
            new_x = random.randint(80, SCREEN_WIDTH - 80)
            new_y = random.randint(50, 300)
            self.rect.center = (new_x, new_y)

            #Check if coin spawns on enemy
            collision = any(self.rect.colliderect(enemy.rect) for enemy in self.enemies)
            if not collision:
                break

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > 600:  #Reset coin if it leaves screen
            self.spawn()

    def check_collision(self, player):
        global COIN_SCORE
        if pygame.sprite.collide_rect(self, player):  #Check if player touches coin
            COIN_SCORE += self.value
            self.sound.play()  #Play sound
            self.spawn()  #Spawn new coin

#Create player
P1 = Player()

#Create enemy
enemies = pygame.sprite.Group()
E1 = Enemy()
enemies.add(E1)

#Create coin
C1 = Coin(enemies)

#Groups for easy handling
coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

#Speed increase event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

n = 5
#Game loop
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED and COIN_SCORE >= n:
            SPEED += 0.5
            n += 5      
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #Draw background
    DISPLAYSURF.blit(background, (0,0))

    #Display scores
    scores = font_small.render(f"Score: {SCORE}", True, BLACK)
    coin_scores = font_small.render(f"Coins: {COIN_SCORE}", True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    DISPLAYSURF.blit(coin_scores, (10,30))

    #Move and draw all objects
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    C1.check_collision(P1)  #Check if player collects coin

    #Check if player hits enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('PP2/TSIS8/melody/crash.wav').play()
        pygame.time.delay(1000) #Pause
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30,250))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        time.sleep(2)
        pygame.quit()
        sys.exit()        

    pygame.display.update()
    FramePerSec.tick(FPS)
