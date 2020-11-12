import pygame
import neat
import time
import os
import random

#using CAPS as naming convention for numerical values
WIN_WIDTH = 600
WIN_HEIGHT = 800

#Loading image of Flappy Bird
birdImage = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird1.png"))), 
            pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird2.png"))),
            pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird3.png")))]

