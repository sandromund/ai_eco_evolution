import numpy as np
import pygame
import sys
import random
from numba import njit


@njit(fastmath=True)
def create_offspring(neighbors):
    pass


class Art:

    def __init__(self, width=1600, height=1200):
        self.width = width
        self.height = height
        self.fps = 60
        self.background_color = (255, 255, 255)
        self.size = 3
        self.reproduce_chance = 3  # 1/3

        self.__w = self.width // self.size
        self.__h = self.height // self.size

        # index of the rgb color that gets mutated
        self.mutation_selection = np.random.randint(low=0, high=3, size=(self.__w, self.__h))

        # values that gets added to the selected part of the color
        self.mutation_amount = np.random.randint(low=-10, high=11, size=(self.__w, self.__h))
        self.color = np.full((self.__w, self.__h, 3), 255, dtype=int)
        self.spawn = np.full((self.__w, self.__h), False, dtype=bool)

        x, y = self.__w // 2, self.__h // 2
        self.spawn[x][y] = True
        for i in range(3):
            self.color[x][y][i] = random.randrange(0, 255)

        pygame.init()
        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Art')

        self.parents = [(x, y)]

    def get_neighbors(self, parent):
        neighbors = []
        x, y = parent
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if 0 <= i < self.__w and 0 <= j < self.__h and not self.spawn[i][j]:
                    neighbors.append((i, j))
        return neighbors

    def create_offspring(self):
        new_parents = []
        for (x, y) in self.parents:
            for neighbor in self.get_neighbors((x, y)):
                i, j = neighbor
                if self.spawn[i][j]:
                    continue
                if random.randrange(1, self.reproduce_chance) == 1:
                    i, j = neighbor
                    self.spawn[i][j] = True
                    self.color[i][j] = self.color[x][y]
                    k = self.mutation_selection[i][j]
                    c = self.color[i][j][k] + self.mutation_amount[i][j]
                    if 0 <= c <= 255:
                        self.color[i][j][k] = c
                    new_parents.append(neighbor)
        self.parents = new_parents

    def draw(self):
        for x in range(self.__w):
            for y in range(self.__h):
                if self.spawn[x][y]:
                    rect = pygame.Rect(x * self.size, y * self.size, self.size, self.size)
                    pygame.draw.rect(self.display, self.color[x][y], rect)

    def run(self):

        while True:
            self.display.fill(self.background_color)

            self.draw()
            self.create_offspring()

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.clock.tick(self.fps)


if __name__ == '__main__':
    art = Art()
    art.run()
