import numpy as np


class CellGrid:

    def __init__(self, weight, height, n_states, size):
        self.weight = weight // size
        self.height = height // size
        self.n_states = n_states
        self.size = size
        self.grid = np.random.randint(n_states, size=(self.weight, self.height))

    def iterate(self):
        new_grid = self.grid.copy()
        for i in range(self.weight):
            for j in range(self.height):
                value = self.grid[i][j]

                if value != self.n_states -1:
                    if i-1 > 0:
                        if self.grid[i-1][j] == value + 1 :    # left
                            new_grid[i][j] = self.grid[i-1][j]
                            continue
                    if i + 1 < self.weight:
                        if self.grid[i+1][j] == value + 1:   # right
                            new_grid[i][j] = self.grid[i+1][j]
                            continue
                    if j - 1 > 0:
                        if self.grid[i][j-1] == value + 1:    # left
                            new_grid[i][j] = self.grid[i][j-1]
                            continue
                    if j + 1 < self.height:
                        if self.grid[i][j+1] == value + 1:    # left
                            new_grid[i][j] = self.grid[i][j+1]
                            continue
                else:
                    if i-1 > 0:
                        if self.grid[i-1][j] == 0:    # left
                            new_grid[i][j] = 0
                            continue
                    if i + 1 < self.weight:
                        if self.grid[i+1][j] == 0:    # right
                            new_grid[i][j] = 0
                            continue
                    if j - 1 > 0:
                        if self.grid[i][j-1] == 0:    # left
                            new_grid[i][j] = 0
                            continue
                    if j + 1 < self.height:
                        if self.grid[i][j+1] == 0:    # left
                            new_grid[i][j] = 0
                            continue
        self.grid = new_grid


