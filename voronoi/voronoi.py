import numpy as np
import pygame as pg


def draw_points(points, screen, radius=3):
    for i in range(len(points)):
        pg.draw.circle(screen, (255, 255, 255), points[i], radius)


