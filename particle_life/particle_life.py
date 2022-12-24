import pygame
import math


class Particle:

    def __init__(self, color, x, y, g):
        self.color = color
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.g =g



def gravity(a, b):
    fx = 0
    fy = 0
    dx = a.x - b.x
    dy = a.y - b.y
    d = math.sqrt(dx * dx + dy * dy)
    if d > 0:
        f = a.g * 1 / d
        fx += f * dx
        fy += f * dy
    a.vx += fx
    a.vy += fy
    a.x -= a.vx
    a.y -= a.vy
    if a.x <=0 or a.x >= 1000:
        a.vx *= -1
    if a.y <= 0 or a.y >= 1000:
        a.vy *= -1


class ParticleLifeSimulation:

    def __init__(self, width=1000, height=1000, tile=10, fps=6):
        self.width = width
        self.height = height
        self.tile = tile
        self.fps = fps
        pygame.init()
        self.surface = pygame.display.set_mode((self.width, self.height))
        self.particles = [
            Particle(color=(255, 0, 0), x=100, y=100, g=1),
            Particle(color=(0, 255, 0), x=900, y=900, g=1),
            Particle(color=(255, 0, 255), x=100, y=900, g=1),
            Particle(color=(255, 255, 0), x=900, y=100, g=1),


        ]

    def __apply_gravity(self):
        for i in range(len(self.particles)):
            for j in range(len(self.particles)):
                if i != j:
                    gravity(self.particles[i], self.particles[j])

    def __draw_particles(self):
        for p in self.particles:
            pygame.draw.circle(self.surface, color=p.color, center=(p.x, p.y), radius=20)

    def run(self):
        clock = pygame.time.Clock()
        while True:
            self.surface.fill(pygame.Color('black'))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            self.__draw_particles()
            self.__apply_gravity()
            pygame.display.flip()
            clock.tick(self.fps)


if __name__ == '__main__':
    life = ParticleLifeSimulation(fps=130)
    life.run()
