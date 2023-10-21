import pygame as pg
from numba import njit


def draw_points(points, screen, radius=3):
    for i in range(len(points)):
        pg.draw.circle(screen, (255, 255, 255), points[i], radius)


@njit(fastmath=True)
def cal_coloring(points, width, height, colors, fild):
    for x in range(width):
        for y in range(height):
            min_dist = None
            for i in range(len(points)):
                d = (((x - points[i][0]) ** 2 + (y - points[i][1]) ** 2) ** 0.5)
                if min_dist is None or d < min_dist:
                    if x == y == 0:
                        print(points[i], colors[i], d)
                    fild[x, y] = colors[i]
    print(fild.shape)
    return fild
