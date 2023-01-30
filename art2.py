import numpy as np
import pygame
import sys


class Art:

    def __init__(self, width=1600, height=1200):
        self.width = width
        self.height = height
        self.fps = 60
        self.background_color = (255, 255, 255)

        # index of the rgb color that gets mutated
        self.mutation_selection = np.random.randint(low=0, high=3, size=(self.width, self.height))

        # values that gets added to the selected part of the color
        self.mutation_amount = np.random.randint(low=-10, high=11, size=(self.width, self.height))

    def run(self):
        pygame.init()
        clock = pygame.time.Clock()
        dis = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Art')
        while True:
            dis.fill(self.background_color)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            clock.tick(self.fps)


if __name__ == '__main__':
    art = Art()
    art.run()
