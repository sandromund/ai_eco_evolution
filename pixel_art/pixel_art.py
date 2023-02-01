import numpy as np
import pygame
import sys
import random
from numba import njit


@njit(fastmath=True)
def create_offspring(parents, h, w, spawn, reproduce_chance, color, mutation_selection, mutation_amount):
    new_parents = []
    n = len(parents)
    for i in range(n):
        x, y = parents[i]
        neighbors = []
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if 0 <= i < w and 0 <= j < h and not spawn[i][j]:
                    neighbors.append((i, j))
        for neighbor in neighbors:
            i, j = neighbor
            if spawn[i][j]:
                continue
            if random.randrange(1, reproduce_chance) == 1:
                spawn[i][j] = True
                color[i][j] = color[x][y]
                k = mutation_selection[i][j]
                c = color[i][j][k] + mutation_amount[i][j]
                if 0 <= c <= 255:
                    color[i][j][k] = c
                new_parents.append(neighbor)
    return new_parents, spawn, color


class Art:

    def __init__(self, width=1000, height=1000, reproduce_chance=3):
        assert 1 < reproduce_chance < 6
        self.reproduce_chance = reproduce_chance
        self.width = width
        self.height = height
        self.fps = 100

        # Arrays to handle the pixel colors
        self.mutation_selection = None
        self.mutation_amount = None
        self.color = None
        self.spawn = None

        pygame.init()
        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Pixel Art')
        self.parents = []

    def init_set_arrays(self):
        # index of the rgb color that gets mutated
        self.mutation_selection = np.random.randint(low=0, high=3, size=(self.width, self.height))
        # values that gets added to the selected part of the color
        self.mutation_amount = np.random.randint(low=-10, high=11, size=(self.width, self.height))
        self.spawn = np.full((self.width, self.height), False, dtype=bool)
        self.color = np.full((self.width, self.height, 3), 0, dtype=int)

    def spawn_init_pixel(self):
        x, y = self.width // 2, self.height // 2
        self.spawn[x][y] = True
        for i in range(3):
            self.color[x][y][i] = random.randrange(0, 255)
        self.parents.append((x, y))

    def draw(self):
        pygame.surfarray.blit_array(self.display, self.color)
        pygame.display.update()

    def run(self):
        while True:
            if len(self.parents) > 0:
                self.parents, self.spawn, self.color = \
                    create_offspring(np.array(self.parents), h=self.height, w=self.width,
                                     spawn=self.spawn,
                                     reproduce_chance=self.reproduce_chance,
                                     color=self.color,
                                     mutation_selection=self.mutation_selection,
                                     mutation_amount=self.mutation_amount)
            else:
                self.init_set_arrays()
                self.spawn_init_pixel()
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.clock.tick(self.fps)


if __name__ == '__main__':
    art = Art()
    art.run()
