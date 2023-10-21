import numpy as np
import pygame as pg


def get_random_points(n, max_value):
    return np.random.randint(low=0, high=max_value, size=(n, 2))


def get_random_colors(n):
    return np.random.randint(low=0, high=255, size=(n, 3))


def draw_points(points, screen, radius=6):
    for i in range(len(points)):
        pg.draw.circle(screen, (255, 255, 255), points[i], radius)


def get_create_fild(width, height):
    spawn = np.full((width, height), False, dtype=bool)
    color = np.full((width, height, 3), 0, dtype=int)

    points = vn.get_random_points(n=100, max_value=window_size)
    colors = vn.get_random_colors(n=100)


def draw_array():
    pg.surfarray.blit_array(screen, self.color)
    pg.display.update()
