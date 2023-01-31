import numba
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

    def __init__(self, width=1600, height=1200):
        self.width = width
        self.height = height
        self.fps = 60
        self.background_color = (255, 255, 255)
        self.size = 1
        self.reproduce_chance = 3

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

    def draw(self):
        pygame.surfarray.blit_array(self.display, self.color)

    def draw_old(self):
        for x in range(self.__w):
            for y in range(self.__h):
                if self.spawn[x][y]:
                    rect = pygame.Rect(x * self.size, y * self.size, self.size, self.size)
                    pygame.draw.rect(self.display, self.color[x][y], rect)

    def run(self):

        while True:
            self.display.fill(self.background_color)


            if len(self.parents):
                self.parents, self.spawn, self.color = create_offspring(np.array(self.parents), h=self.__h, w=self.__w,
                                                                        spawn=self.spawn,
                                                                        reproduce_chance=self.reproduce_chance,
                                                                        color=self.color,
                                                                        mutation_selection=self.mutation_selection,
                                                                        mutation_amount=self.mutation_amount)
            self.draw()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            print(self.clock.get_fps())
            self.clock.tick(self.fps)


if __name__ == '__main__':
    art = Art()
    art.run()
