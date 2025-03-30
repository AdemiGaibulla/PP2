import pygame
import time
import random

# Initialize pygame
pygame.init()

# Game settings
window_x = 720
window_y = 480
snake_speed = 10

# Colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Create game window
game_window = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption('Snake Game with Levels')

# FPS controller
fps = pygame.time.Clock()

# Snake position and body
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

# Function to generate food position

def generate_food():
    size_options = {  
        "small": (10, 10, 3),
        "medium": (15, 15, 2),
        "large": (20, 20, 1) 
    }
    
    size_key = random.choice(list(size_options.keys()))  # Choosing random key
    new_size = size_options[size_key][:2]  # Giving first two values
    new_score = size_options[size_key][2]
    
    while True:
        food_x = random.randint(1, (window_x - new_size[0]) // 10) * 10
        food_y = random.randint(1, (window_y - new_size[1]) // 10) * 10
        if [food_x, food_y] not in snake_body:
            return [food_x, food_y, new_size, new_score, time.time()]  # Add timestamp

fruit_position = generate_food()
fruit_spawn = True

# Snake movement direction
direction = 'RIGHT'
change_to = direction

# Score and level
score = 0
level = 1

# Function to display score and level

def show_info():
    font = pygame.font.SysFont('times new roman', 20)
    score_surface = font.render(f'Score: {score}  Level: {level}', True, white)
    game_window.blit(score_surface, [10, 10])

# Function to end game

def game_over():
    font = pygame.font.SysFont('times new roman', 50)
    message = font.render(f'Game Over! Score: {score}', True, red)
    game_window.blit(message, [window_x // 4, window_y // 3])
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

# Main game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'
    
    # Move the snake
    if direction == 'UP':
        snake_position[1] -= 10
    elif direction == 'DOWN':
        snake_position[1] += 10
    elif direction == 'LEFT':
        snake_position[0] -= 10
    elif direction == 'RIGHT':
        snake_position[0] += 10

    # Check for border collision
    if (snake_position[0] < 0 or snake_position[0] >= window_x or
        snake_position[1] < 0 or snake_position[1] >= window_y):
        game_over()

    # Update snake body
    snake_body.insert(0, list(snake_position))
    if snake_position[:2] == fruit_position[:2]:
        score += 10
        fruit_spawn = False
        if score % 30 == 0:
            level += 1
            snake_speed += 2  # Increase speed per level
    else:
        snake_body.pop()

    # Check if food time expired
    if time.time() - fruit_position[4] > 10:  # Food disappears after 10 sec
        fruit_spawn = False
    
    # Generate new food position if eaten or expired
    if not fruit_spawn:
        fruit_position = generate_food()
        fruit_spawn = True
    
    # Check if snake collides with itself
    for block in snake_body[1:]:
        if snake_position == block:
            game_over()

    # Draw game elements
    game_window.fill(black)
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, red, pygame.Rect(fruit_position[0], fruit_position[1], fruit_position[2][0], fruit_position[2][1]))
    
    # Display score and level
    show_info()
    
    # Refresh screen
    pygame.display.update()
    fps.tick(snake_speed)
