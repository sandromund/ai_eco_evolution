import pygame
from pygame import mixer


class Player():

    def __init__(self, x, y, screen_height, world):
        self.images_right = []
        self.images_left = []
        self.images_jump = []
        self.images_standing = []
        self.index = 0
        self.jump_index = 0
        self.standing_index = 0
        self.scale = (80, 150)
        for num in range(1, 3):
            img = pygame.image.load(f'img/standing_{num}.png')
            self.images_standing.append(pygame.transform.scale(img, self.scale))
        for num in range(1, 4):
            img_jump = pygame.image.load(f'img/jump_{num}.png')
            img_jump = pygame.transform.scale(img_jump, self.scale)
            self.images_jump.append(img_jump)
        for num in range(1, 4):
            img_right = pygame.image.load(f'img/walk_{num}.png')
            img_right = pygame.transform.scale(img_right,  self.scale)
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)
        self.image = self.images_standing[self.standing_index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_y = 0
        self.jumped = False
        self.screen_height = screen_height
        self.walk_cooldown = 10
        self.walk_counter = 0
        self.jump_cooldown = 12
        self.jump_counter = 0
        self.standing_cooldown = 25
        self.standing_counter = 0
        self.direction = 0
        self.max_jumps = 2
        self.remaining_jumps = self.max_jumps
        self.is_jumping = False
        self.is_walking = False
        self.is_standing = True

        self.world = world
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.is_on_ground = True

        self.jump_fx = pygame.mixer.Sound('sound/jump.wav')
        self.jump_fx.set_volume(0.5)

    def update(self):
        dx = 0
        dy = 0

        #get keypresses
        key = pygame.key.get_pressed()

        if self.is_on_ground:
            self.remaining_jumps = self.max_jumps
            self.is_jumping = False
            self.is_walking = False
            self.is_standing = True

        if key[pygame.K_SPACE] and self.jumped is False and \
                (self.is_on_ground or self.remaining_jumps > 0):
            self.jump_fx.play()
            self.vel_y = -25
            self.jumped = True
            self.remaining_jumps -= 1
            self.is_jumping = True
            self.is_walking = False
            self.is_standing = False



        if key[pygame.K_SPACE] is False:
            self.jumped = False

        if key[pygame.K_LEFT]:
            dx -= 5
            self.walk_counter += 1
            self.direction = -1
            self.is_walking = True
            self.is_standing = False
        if key[pygame.K_RIGHT]:
            dx += 5
            self.walk_counter += 1
            self.direction = 1
            self.is_walking = True
            self.is_standing = False


        """
      
        if key[pygame.K_LEFT] is False and key[pygame.K_RIGHT] is False:
            self.walk_counter = 0
            self.index = 0
            if self.direction == 1:
                self.image = self.images_right[self.index]
            if self.direction == -1:
                self.image = self.images_left[self.index]
       
        if self.is_walking or self.is_jumping:
            self.is_standing = False

        if not self.is_standing and not self.is_jumping:
            self.is_standing = True
            self.is_walking = False
        """

        # ------------------------------ handle animation --------------------------------------

        if self.is_standing:
            if self.standing_counter > self.standing_cooldown:
                self.standing_counter = 0
                self.standing_index += 1
                if self.standing_index >= len(self.images_standing):
                    self.standing_index = 0
                self.image = self.images_standing[self.standing_index]
            self.standing_counter += 1

        if self.is_walking:
            if self.walk_counter > self.walk_cooldown:
                self.walk_counter = 0
                self.index += 1
                if self.index >= len(self.images_right):
                    self.index = 0
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                if self.direction == -1:
                    self.image = self.images_left[self.index]
        else:
            self.walk_counter = 0
            self.index = 0

        if self.is_jumping:
            if self.jump_counter > self.jump_cooldown:
                self.jump_counter = 0
                self.jump_index += 1
                if self.jump_index >= len(self.images_jump):
                    self.jump_index = 0
                self.image = self.images_jump[self.jump_index]
            self.jump_counter += 1
        else:
            self.jump_counter = 0
            self.jump_index = 0

        # --------------------------------------------------------------------------------------



        #add gravity
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y

        self.is_on_ground = False
        #check for collision
        for rect in self.world:
            #check for collision in x direction
            if rect.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
            #check for collision in y direction
            if rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                #check if below the ground i.e. jumping
                if self.vel_y < 0:
                    dy = rect.bottom - self.rect.top
                    self.vel_y = 0
                #check if above the ground i.e. falling
                elif self.vel_y >= 0:
                    dy = rect.top - self.rect.bottom
                    self.vel_y = 0

                    self.is_on_ground = True



        #update player coordinates
        self.rect.x += dx
        self.rect.y += dy



#       print(self.is_standing, self.is_jumping, self.is_walking)