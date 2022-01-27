import pygame
from creature import Creature
import random
import time
import math


def overlap(x1, y1, r1, x2, y2, r2):
    # return r2 >= math.sqrt((x1 - x2)**2 + (y1 - y2)**2) +r1
    return (r1 - r2)**2 >= (x1 - x2)**2 + (y1 - y2)**2


dis_width = 1600
dis_height = 1200


creature = []
for i in range(30):
    r, g, b = random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)
    c = Creature(random.randrange(0, dis_width), random.randrange(0, dis_height), random.randrange(5, 11),
                 (r, g, b), dis_width, dis_height, random.randrange(50, 101), random.randrange(1, 6))
    creature.append(c)

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
clock = pygame.time.Clock()


dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Sandro ist cool.')


game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    for c1 in creature:
        c1.state = 0
        c1.target = None
        for c2 in creature:
            if c1 != c2 and c1.is_alive and c2.is_alive:
                # check if creatures meet
                # bigger creatures eat smaller ones
                if overlap(c1.x, c1.y, c1.size, c2.x, c2.y, c2.size):
                    if c1.size > c2.size:
                        c1.size += c2.size // 3
                        c2.is_alive = False
                if overlap(c1.x, c1.y, c1.vision, c2.x, c2.y, c2.size):
                    if c1.size > c2.size:
                        c1.target = (c2.x, c2.y)
                        c1.state = 1 # the hunt begin




    dis.fill(white)
    for c in creature:
        if c.is_alive:
            pygame.draw.circle(dis, c.color, (c.x, c.y), c.size)
            pygame.draw.circle(dis, 0, (c.x, c.y), c.vision, 1)
        if c.target:
            pygame.draw.line(dis, c.color, (c.x, c.y), (c.target[0], c.target[1] ))
    for c in creature:
        if c.is_alive:
            c.move()
    pygame.time.wait(50)
    pygame.display.update()


