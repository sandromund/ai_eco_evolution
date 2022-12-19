import numpy as np
from numba import njit
import random
import pygame
from copy import deepcopy


@njit(fastmath=True)
def iterate(grid, new_grid, weight, height, n_states):
    for i in range(weight):
        for j in range(height):
            value = grid[i][j]
            if value != n_states - 1:
                if i - 1 > 0:
                    if grid[i - 1][j] == value + 1:
                        new_grid[i][j] = grid[i - 1][j]
                        continue
                if i + 1 < weight:
                    if grid[i + 1][j] == value + 1:
                        new_grid[i][j] = grid[i + 1][j]
                        continue
                if j - 1 > 0:
                    if grid[i][j - 1] == value + 1:
                        new_grid[i][j] = grid[i][j - 1]
                        continue
                if j + 1 < height:
                    if grid[i][j + 1] == value + 1:
                        new_grid[i][j] = grid[i][j + 1]
                        continue
            else:
                if i - 1 > 0:
                    if grid[i - 1][j] == 0:
                        new_grid[i][j] = 0
                        continue
                if i + 1 < weight:
                    if grid[i + 1][j] == 0:
                        new_grid[i][j] = 0
                        continue
                if j - 1 > 0:
                    if grid[i][j - 1] == 0:
                        new_grid[i][j] = 0
                        continue
                if j + 1 < height:
                    if grid[i][j + 1] == 0:
                        new_grid[i][j] = 0
                        continue
    return new_grid


class CyclicCellularAutomat:

    def __init__(self, weight, height, n_states, tile, fps):
        self.weight = weight
        self.height = height
        self.__w = self.weight // tile
        self.__h = self.height // tile
        self.n_states = n_states
        self.tile = tile
        self.grid = np.random.randint(n_states, size=(self.__w, self.__h))
        self.next = np.zeros(shape=(self.__w, self.__h))
        self.color_dict = self.__get_init_dict()
        pygame.init()
        self.surface = pygame.display.set_mode((self.weight, self.height))
        self.fps = fps

    def __get_init_dict(self):
        color_dict = dict()
        for i in range(self.n_states + 1):
            color_dict[i] = (random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256))
        return color_dict

    def __draw_grid(self, grid):
        for x in range(self.__w):
            for y in range(self.__h):
                color = self.color_dict[grid[x][y]]
                pygame.draw.rect(self.surface, color,
                                 rect=(x * self.tile , y * self.tile, self.tile , self.tile))

    def run(self):
        pygame.init()
        new_grid, grid = self.next, self.grid
        clock = pygame.time.Clock()
        w, h, n = self.__w, self.__h, self.n_states
        while True:
            self.surface.fill(pygame.Color('black'))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            new_grid = iterate(grid, new_grid, w, h, n)
            self.__draw_grid(grid)
            grid = deepcopy(new_grid)
            pygame.display.flip()
            clock.tick(self.fps)


if __name__ == '__main__':
    automat = CyclicCellularAutomat(weight=1000, height=1000, n_states=8, tile=5, fps=60)
    automat.run()
