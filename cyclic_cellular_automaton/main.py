import pygame
import random
from cell_grid import CellGrid
WIDTH = 1000
HEIGHT = 1000
N = 10
SIZE = 20

background_color = (175, 247, 252)
dis = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sandro ist cool.')

color_dic = {}
for i in range(N+1):
    color_dic[i] = (random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256))

world = CellGrid(WIDTH, HEIGHT, N, SIZE)


def draw_grid():
    for i in range(0, WIDTH, SIZE):
        for j in range(0, HEIGHT, SIZE):
            color = color_dic[world.grid[i // SIZE][j // SIZE]]
            # dis.set_at((i, j), color)
            pygame.draw.rect(dis, color, rect=(i, j, i + SIZE, j + SIZE))


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
        draw_grid()
        world.iterate()
        pygame.display.update()
        #pause = True