import random
import pygame
from boid import Boid, distance

WIDTH = 1600
HEIGHT = 1200
N_BOIDS = 100

background_color = (175, 247, 252)
dis = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sandro ist cool.')


boids = [Boid(WIDTH, HEIGHT) for _ in range(N_BOIDS+1)]

FPS: int = 60
pygame.init()
clock = pygame.time.Clock()
out = False
pause = False
while not out:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            out = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause = not pause
    if not pause:
        pygame.Surface.fill(dis, background_color)
        for boid in boids:

            neighbours = []
            for neighbour in boids:
                if boid != neighbour and distance([boid.x, boid.y], [neighbour.x, neighbour.y]) < boid.vision:
                    neighbours.append(neighbour)
            if len(neighbours) > 0:
                boid.cohesion(neighbours)
                boid.seperation(neighbours)
                boid.alignment(neighbours)
            boid.fly()
            pygame.draw.circle(dis, boid.color, (boid.x, boid.y), boid.size)
            for i in range(len(boid.history)-1):
                p1 = (boid.history[i][0], boid.history[i][1])
                p2 = (boid.history[i+1][0], boid.history[i+1][1])
                pygame.draw.line(dis, boid.color, p1, p2)
        pygame.display.update()
