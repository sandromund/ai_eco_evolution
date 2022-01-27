import random


class Creature:
    def __init__(self, x, y, size, color, dis_width, dis_height, vision, speed):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.dis_width = dis_width
        self.dis_height = dis_height
        self.last_move = random.randrange(0, 4)
        self.is_alive = True
        self.vision = vision
        self.speed = speed

        self.state = 0
        self.target = None

    def move(self):
        if self.state == 0:
            self.random_move()
        if self.state == 1:
            self.follow()

    def follow(self):
        x, y = self.target
        if self.x < x:
            if self.speed > x - self.x:
                self.x = x
            else:
                self.x += self.speed
        if self.x > x:
            if self.speed > self.x - x:
                self.x = x
            else:
                self.x -= self.speed
        if self.y < y:
            if self.speed > y - self.y:
                self.y = y
            else:
                self.y += self.speed
        if self.y > y:
            if self.speed > self.y - y:
                self.y = y
            else:
                self.y -= self.speed



    def random_move(self):
        if random.randrange(0, 101) < 95:
            r = self.last_move
        else:
            r = random.randrange(0, 4)
            self.last_move = r
        move = 0
        speed = self.speed
        if r == 0:  # LEFT
            if self.x - self.size > 0:
                self.x -= speed + move
        elif r == 1:  # RIGHT
            if self.x + self.size < self.dis_width:
                self.x += speed - move
        elif r == 2:  # UP
            if self.y - self.size > 0:
                self.y -= speed + move
        elif r == 3:  # DOWN
            if self.y + self.size < self.dis_height:
                self.y += speed - move
        elif r == 4:    # LEFT UP
            if self.x - self.size > 0:
                self.x -= self.size + move
            if self.y - self.size > 0:
                self.y -= self.size + move
        elif r == 4:    # LEFT DOWN
            if self.x - self.size > 0:
                self.x -= self.size + move
            if self.y + self.size < self.dis_height:
                self.y += self.size - move
        elif r == 5:    # RIGHT UP
            if self.x + self.size < self.dis_width:
                self.x += self.size - move
            if self.y - self.size > 0:
                self.y -= self.size + move
        elif r == 6:    # RIGHT DOWN
            if self.x + self.size < self.dis_width:
                self.x += self.size - move
            if self.y + self.size < self.dis_height:
                self.y += self.size - move


