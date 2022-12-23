import pygame


class ParticleLifeSimulation:

    def __init__(self, width=1500, height=900, tile=15, fps=6):
        self.width = width
        self.height = height
        self.tile = tile
        self.fps = fps
        pygame.init()
        self.surface = pygame.display.set_mode((self.width, self.height))

    def run(self):
        clock = pygame.time.Clock()
        while True:
            self.surface.fill(pygame.Color('black'))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            pygame.display.flip()
            clock.tick(self.fps)


if __name__ == '__main__':
    life = ParticleLifeSimulation()
    life.run()
