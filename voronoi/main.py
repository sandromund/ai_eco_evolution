import pygame
import sys
import numpy as np

import voronoi as vn

n = 100
window_size = 1000
width, height = window_size, window_size
background_color = (0, 0, 0)
n_points = 100

pygame.init()

screen = pygame.display.set_mode((window_size, window_size))
pygame.display.set_caption('Voronoi')

points = np.random.randint(low=0, high=window_size, size=(n, 2))  # TODO
colors = np.random.randint(low=0, high=255, size=(n, 3))
fild = np.full((width, height, 3), 0, dtype=int)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(background_color)
    pygame.surfarray.blit_array(screen, fild)

    vn.draw_points(points, screen)
    pygame.display.flip()
