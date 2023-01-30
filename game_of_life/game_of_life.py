import pygame
from numba import njit
import numpy as np
from copy import deepcopy


@njit(fastmath=True)
def update_cells(current_field, next_field, w, h):
    res = []
    for x in range(1, w - 1):
        for y in range(1, h - 1):
            count = 0
            for j in range(y - 1, y + 2):
                for i in range(x - 1, x + 2):
                    if current_field[j][i] == 1:
                        count += 1
            if current_field[y][x] == 1:
                count -= 1
                if count == 2 or count == 3:
                    next_field[y][x] = 1
                    res.append((x, y))
                else:
                    next_field[y][x] = 0
            else:
                if count == 3:
                    next_field[y][x] = 1
                    res.append((x, y))
                else:
                    next_field[y][x] = 0
    return next_field, res


class GameOfLive:

    def __init__(self, width=1500, height=900, tile=15, fps=6):
        self.width = width
        self.height = height
        self.tile = tile
        self.fps = fps
        self.__w = self.width // self.tile
        self.__h = self.height // self.tile
        self.resolution = self.width, self.height
        self.next_field = np.zeros(shape=(self.__w, self.__h))
        self.current_field = np.random.randint(2, size=(self.__w, self.__h))
        pygame.init()
        self.surface = pygame.display.set_mode(self.resolution)

    def __draw_cells(self, res):
        for x, y, in res:
            pygame.draw.rect(self.surface, pygame.Color('darkgreen'),
                             (x * self.tile + 2, y * self.tile + 2, self.tile - 2, self.tile - 2))

    def run(self):
        next_field, current_field = self.next_field, self.current_field
        clock = pygame.time.Clock()
        w, h = self.__w, self.__h
        while True:
            self.surface.fill(pygame.Color('white'))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            next_field, res = update_cells(current_field, next_field, w, h)
            self.__draw_cells(res)
            current_field = deepcopy(next_field)
            pygame.display.flip()
            clock.tick(self.fps)


if __name__ == '__main__':
    game = GameOfLive(width=1600, height=900, tile=10, fps=30)
    game.run()
