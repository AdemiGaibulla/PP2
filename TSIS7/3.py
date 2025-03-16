import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))

x, y = 250,250

running = True
while running:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x - 25 - 20 >= 0:
        x -= 20
    if keys[pygame.K_RIGHT] and x + 25 + 20 <= 500:
        x += 20
    if keys[pygame.K_UP] and y - 25 - 20 >= 0:
        y -= 20
    if keys[pygame.K_DOWN] and y + 25 + 20 <= 500:
        y += 20

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 25)
    pygame.display.flip()

pygame.quit()
