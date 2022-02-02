import random
import math


class Boid:
    def __init__(self, width, height):
        self.color = (random.randrange(0, 101), random.randrange(0, 101), 210 + random.randrange(-100, 41))
        self.x = random.randrange(0, width)     # location x
        self.y = random.randrange(0, height)    # location y
        self.width = width
        self.height = height
        self.centering_factor = 0.05
        self.min_distance = 50
        self.vx = rand_float_range(-10, 11)
        self.vy = rand_float_range(-10, 11)
        self.size = 10
        self.margin = 150
        self.margin_factor_x = 1.0
        self.margin_factor_y = 1.0
        self.max_speed = 5
        self.vision = 60
        self.avoid_factor = 0.05
        self.matching_factor = 0.015

        self.history = []

    def cohesion(self, neighbours):
        """
        steer to move toward the average position of local flockmates
        """
        x, y, n = 0, 0, 0
        # Find the center of mass
        for boid in neighbours:
            n += 1
            x += boid.x
            y += boid.y
        if n > 0:
            x = x / n
            y = y / n

        # adjust velocity slightly to point towards the center of mass
        self.vx += (x - self.x) * self.centering_factor
        self.vy += (y - self.y) * self.centering_factor

    def seperation(self, neighbours):
        """
        steer to avoid crowding local flockmates
        """
        x, y = 0, 0
        for boid in neighbours:
            if distance([self.x, self.y], [boid.x, boid.y]) < self.min_distance:
                x += self.x - boid.x
                y += self.y - boid.y
        self.vx += x * self.avoid_factor
        self.vy += y * self.avoid_factor

    def alignment(self, neighbours):
        """
        steer towards the average heading of local flockmates
        """
        vx, vy, n = 0, 0, 0
        for boid in neighbours:
            vx += boid.vx
            vy += boid.vy
            n += 1
        if n > 0:
            vx = vx / n
            vy = vy / n
        self.vx += (vx - self.vx) * self.matching_factor
        self.vy += (vy - self.vx) * self.matching_factor

    def stay_in_view(self):
        """

        :return:
        """
        if self.x < self.margin:
            self.vx += self.margin_factor_x
        if self.x > self.width - self.margin:
            self.vx -= self.margin_factor_x
        if self.y < self.margin:
            self.vy += self.margin_factor_y
        if self.y > self.height - self.margin:
            self.vy -= self.margin_factor_y

        #if self.x < 0:
        #    self.x = self.width - 1
        #elif self.x >= self.width:
        #    self.x = 0
        #if self.y < 0:
        #    self.y = self.height -1
        #elif self.y >= self.height:
        #    self.y = 0

    def fly(self):
        self.history.insert(0, (self.x, self.y))
        if len(self.history) > 70:
            self.history = self.history[:70]
        # Update the position based on the current velocity
        if self.vx >= self.max_speed:
            self.vx = self.max_speed
        elif self.vx <= - self.max_speed:
            self.vx = - self.max_speed
        if self.vy >= self.max_speed:
            self.vy = self.max_speed
        elif self.vy <= - self.max_speed:
            self.vy = - self.max_speed
        self.x += self.vx
        self.y += self.vy
        self.stay_in_view()


def distance(p1, p2):
    return math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))


def rand_float_range(start, end):
    return random.random() * (end - start) + start