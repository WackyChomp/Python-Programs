import pygame
import neat
import time
import os
import random

#using CAPS as naming convention for numerical values
WIN_WIDTH = 600
WIN_HEIGHT = 800

#----------------------------------------------------#

#Loading image of Flappy Bird / pipe / base / background
#using snake_case
bird_images = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird1.png"))), 
            pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird2.png"))),
            pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird3.png")))]

pipe_image = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pipe.png")))

base_image = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "base.png")))

background_image = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))

#----------------------------------------------------#

class Bird:
    images = bird_images
    MAX_ROTATION = 25     #how much the image tilts
    ROT_VEL = 20          #rotation velocity
    ANIMATION_TIME = 5

    def __init__(self, x, y):     #starting point of Flappy Bird
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.images[0]      #references images > bird_images

    def jump(self):
        self.vel = 10.5        #negative velocity to move up
        self.tick_count = 0    #keeps track of last jump
        self.height = self.y

    def move(self):

while True:
    bird.move()            #no need to calculate how much the bird moves

#----------------------------------------------------#
