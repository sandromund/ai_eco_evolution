import pygame
from pygame import mixer

from player import Player

pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()
pygame.init()

screen_width = 1600
screen_height = 1200

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Platformer')
clock = pygame.time.Clock()
fps = 60

#load sounds
pygame.mixer.music.load('sound/617305__davejf__melody-loop-125-bpm.mp3')
#pygame.mixer.music.play(-1, 0.0, 5000)
#pygame.mixer.music.set_volume(0.8)


bg = pygame.image.load("img/background.png").convert_alpha()




world = [pygame.Rect(300, 800, 1000, 20)]

player = Player(400, 700, screen_height, world)

#define font
font = pygame.font.SysFont('Bauhaus 93', 70)
font_score = pygame.font.SysFont('Bauhaus 93', 30)


run = True
while run:

    clock.tick(fps)

    #draw background
    #screen.fill((255,255,255))
    screen.blit(bg, (0, 0))

    for rect in world:
        pygame.draw.rect(screen, (0, 0, 0), rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    player.update()
    screen.blit(player.image, player.rect)  # draw player onto screen
    pygame.display.update()

pygame.quit()