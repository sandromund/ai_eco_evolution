import numpy as np
import pygame
import random


class Plant:
    def __init__(self, color, dis, x, y, size):
        self.color = color
        self.neighbours = []
        self.dis = dis
        self.x = x
        self.y = y
        self.size =size

    def find_neighbours(self):
        n1 = (self.x + self.size, self.y)
        n2 = (self.x - self.size, self.y)
        n3 = (self.x, self.y + self.size)
        n4 = (self.x, self.y - self.size)
        n5 = (self.x + self.size, self.y + self.size)
        n6 = (self.x - self.size, self.y - self.size)
        n7 = (self.x - self.size , self.y + self.size)
        n8 = (self.x + self.size, self.y - self.size)
        neighbours = []
        for n in [n1, n2, n3, n4, n5, n6, n7, n8]:
            if n[0] < self.dis[0] and n[1] < self.dis[1]:
                if random.randrange(1,3) == 1:
                    neighbours.append(n)
        return neighbours

    def create_offspring(self, x, y):
        c = list(self.color)
        i = random.randrange(0, 3)
        # for i in range(len(self.color)):
        new_val = self.color[i] + random.randrange(-5, 5)
        if 0 <= new_val <= 255:
            c[i] = new_val
        return Plant(c, self.dis, x, y, self.size)


dis_x = 1600
dis_y = 1200

plant_list = []
init_color_1 = random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)
init_color_2 = random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)

plant_list.append(Plant((150,150,150), (1600, 1200), 800, 600, 4))
#plant_list.append(Plant(init_color_2, (1600, 1200), 1599, 1199, 5))


position_occupied = np.zeros((dis_x, dis_y))
position_occupied[plant_list[0].x, plant_list[0].y] = 1

pygame.init()
clock = pygame.time.Clock()
dis = pygame.display.set_mode((dis_x, dis_y))
pygame.display.set_caption('Sandro ist cool.')

last_plants = plant_list


#ox, oy, oa, ob = 300, 200, 30, 500
#for xi in range(ox, ox + oa - 2):
#    for yi in range(oy, oy + ob):
#        position_occupied[xi][yi] = 1

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    dis.fill((255, 255, 255))

    #pygame.draw.rect(dis, (0, 0, 0), pygame.Rect(ox, oy, oa, ob))

    for plant in plant_list:
        pygame.draw.rect(dis, plant.color, pygame.Rect(plant.x, plant.y, plant.size, plant.size))
    #pygame.time.wait(50)
    pygame.display.update()
    new_plants = []
    for plant in last_plants:
        for neighbour in plant.find_neighbours():
            x, y = neighbour
            if x < dis_x and y < dis_y:
                if position_occupied[x, y] == 0:
                    new_plants.append(plant.create_offspring(x,y))
                    position_occupied[x, y] = 1
    last_plants = new_plants
    plant_list += last_plants

    #if len(last_plants) == 0:
    #    init_color_i = random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)
    #    plant_list = [Plant(init_color_i, (1600, 1200), 800, 600, 4)]
    #    last_plants = plant_list
    #    position_occupied = np.zeros((dis_x, dis_y))
    #    position_occupied[plant_list[0].x, plant_list[0].y] = 1
