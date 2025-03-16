import pygame
import sys

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((800, 600))

play_img = pygame.image.load("PP2/TSIS7/images/play.jpg")
next_img = pygame.image.load("PP2/TSIS7/images/next.jpg")
stop_img = pygame.image.load("PP2/TSIS7/images/stop.jpg")
previous_img = pygame.image.load("PP2/TSIS7/images/previous.jpg")

song1 = pygame.image.load("PP2/TSIS7/images/viva la vida.webp")
song2 = pygame.image.load("PP2/TSIS7/images/maniac.webp")
song3 = pygame.image.load("PP2/TSIS7/images/laufey.webp")

button = pygame.Surface((150, 150))
screen.fill((255, 255, 255))

songs = ["PP2/TSIS7/songs/Coldplay_-_Viva_La_Vida_76651123.mp3","PP2/TSIS7/songs/Conan_Gray_-_Maniac_67072230.mp3","PP2/TSIS7/songs/From_The_Start_-_Laufey_76374123.mp3"]
song_names = ["Coldplay - Viva La Vida", "Conan Gray - Maniac", "Laufey - From The Start"]
song_img = [song1, song2, song3]

current_song = 0
play = False

font = pygame.font.Font(None, 40) 


def play_song():
    global play
    pygame.mixer.music.load(songs[current_song])
    pygame.mixer.music.play()
    play = True


def play_next():
    global current_song
    if current_song < len(songs) - 1:
        current_song += 1
    else:
        current_song = 0
    play_song()


def play_previous():
    global current_song
    if current_song > 0:
        current_song -= 1
    else:
        current_song = len(songs) - 1 
    play_song()


play_song()


while True:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if keys[pygame.K_LEFT]:
            play_next()
        if keys[pygame.K_RIGHT]:
            play_previous()
        if keys[pygame.K_SPACE]:
            if play:
                pygame.mixer.music.pause()
            else:
                pygame.mixer.music.unpause()
            play = not play

    if play:
        button.blit(stop_img, (0, 0))
    else:
        button.blit(play_img, (0, 0))
    
    screen.fill((255, 255, 255))
    screen.blit(previous_img, (100, 400))  
    screen.blit(next_img, (500, 400))  
    screen.blit(button, (300, 400))

    text_surface = font.render(song_names[current_song], True, (0, 0, 0))
    screen.blit(text_surface, (235, 370))

    screen.blit(song_img[current_song], (230, 10))

    pygame.display.flip() 
