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
bird_image = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird1.png"))), 
            pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird2.png"))),
            pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird3.png")))]

pipe_image = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pipe.png")))

base_image = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "base.png")))

background_image = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))

#----------------------------------------------------#


