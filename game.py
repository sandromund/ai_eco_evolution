import pygame
from creature import Creature
import random
import time


dis_width = 1000
dis_height = 1000


creature = []
for i in range(20):
    r, g, b = random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)
    c = Creature(random.randrange(0, dis_width), random.randrange(0, dis_height), 10, (r, g, b), dis_width, dis_height)
    creature.append(c)

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
clock = pygame.time.Clock()


dis = pygame.display.set_mode((dis_width, dis_width))
pygame.display.set_caption('Sandro ist cool.')


game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    dis.fill(white)
    for c in creature:
        pygame.draw.circle(dis, c.color, (c.x, c.y), c.size)
        pygame.draw.circle(dis, 0, (c.x, c.y), c.size*8, 1)
    for c in creature:
        c.move()
    pygame.time.wait(50)
    pygame.display.update()


