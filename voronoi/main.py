import pygame
import sys

import voronoi as vn

window_size = 1000
width, height = window_size, window_size
background_color = (0, 0, 0)
n_points = 100

pygame.init()

screen = pygame.display.set_mode((window_size, window_size))
pygame.display.set_caption('Voronoi')





while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(background_color)
    vn.draw_points(points, screen)
    pygame.display.flip()
