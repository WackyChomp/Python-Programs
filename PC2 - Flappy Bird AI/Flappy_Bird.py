import pygame
import neat
import time
import os
import random
pygame.font.init()

#using CAPS as naming convention for numerical values
WIN_WIDTH = 500
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

stat_font = pygame.font.SysFont("comicsans", 50)

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
        self.tick_count += 1

        d = self.vel*self.tick_count + 1.5*self.tick_count**2      #references physics equation
        if d >= 16:
            d = 16
        if d < 0:         #adjust jump height
            d -= 2

        self.y = self.y + d
        if d < 0 or self.y < self.height + 50:     #slightly tilt up when moving up
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else:
            if self.tilt > -90:        #rotate 90 degrees nose-dive towads the ground
                self.tilt -= self.ROT_VEL

    def draw(self, win):
        self.img_count += 1     #animate bird with tick

        if self.img_count < self.ANIMATION_TIME:        #img_count less than 5 displays 1st flappy bird image
            self.img = self.images[0]
        elif self.img_count < self.ANIMATION_TIME*2:    #img_count less than 10 displays 2nd flappy bird image
            self.img = self.images[1]
        elif self.img_count < self.ANIMATION_TIME*3:    #img_count less than 15 displays 3rd flappy bird image
            self.img = self.images[2]            
        elif self.img_count < self.ANIMATION_TIME*4:
            self.img = self.images[1]
        elif self.img_count == self.ANIMATION_TIME*4 + 1:
            self.img = self.images[0]
            self.img_count = 0
        #resetting after the last image would reposition back to 1st image and not show the transition

        if self.tilt <= -80:
            self.img = self.images[1]          #not flap wings when moving downward
            self.image_count = self.ANIMATION_TIME*2   #shows the animation count of 10 (images[1])

        rotated_image = pygame.transform.rotate(self.img, self.tilt)        #rotates the image
        new_rect = rotated_image.get_rect(center = self.img.get_rect(topleft = (self.x, self.y)).center)
        win.blit(rotated_image, new_rect.topleft)

    def get_mask(self):        #collision for objects
        return pygame.mask.from_surface(self.img)

class Pipe:
    GAP = 200       #space between pipes
    VEL = 5

    def __init__ (self, x):
        self.x = x
        self.height = 0
        self.gap = 100

        self.top = 0
        self.bottom = 0
        self.PIPE_TOP = pygame.transform.flip(pipe_image, False, True)
        self.PIPE_BOTTOM = pipe_image

        self.passed = False          #collision purposes
        self.set_height()         #define where the top and bottom is

    def set_height(self):
        self.height = random.randrange(50, 450)
        self.top = self.height - self.PIPE_TOP.get_height()       #identify top left image of pipe
        self.bottom = self.height + self.GAP

    def move(self):
        self.x -= self.VEL       #change the x position based on velocity that the pipe moves each frame

    def draw(self, win):       #display the pipes
        win.blit(self.PIPE_TOP, (self.x, self.top))
        win.blit(self.PIPE_BOTTOM, (self.x, self.bottom))

    def collide(self, bird):       #references from above: def get_mask(self)
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.PIPE_TOP)
        bottom_mask = pygame.mask.from_surface(self.PIPE_BOTTOM)

        top_offset = (self.x - bird.x, self.top - round(bird.y))
        bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))
        
        t_point = bird_mask.overlap(top_mask, top_offset)
        b_point = bird_mask.overlap(bottom_mask, bottom_offset)

        if t_point or b_point:
            return True
        return False

class Base:
    VEL = 5
    WIDTH = base_image.get_width()
    IMG = base_image

    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.WIDTH

    def move(self):
        self.x1 -= self.VEL
        self.x2 -= self.VEL

        if self.x1 + self.WIDTH < 0:         #if certain part of the base image leaves off screen, it moves to the 2nd base image
            self.x1 = self.x2 + self.WIDTH

        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH

    def draw(self, win):
        win.blit(self.IMG, (self.x1, self.y))
        win.blit(self.IMG, (self.x2, self.y))
#----------------------------------------------------#

def draw_window(win, bird, pipes, base, score):
    win.blit(background_image, (0,0))         #render background image
    for pipe in pipes:
        pipe.draw(win)

    text = stat_font.render("Score: " + str(score), 1, (255, 255, 255))      #renders score
    win.blit(text, (WIN_WIDTH - 10 - text.get_width(), 10))        #the score text scales with screen size

    base.draw(win)
    bird.draw(win)                     #renders flappy bird
    pygame.display.update()

def main(genomes, config):          #runs main loop of the 
    nets = []
    ge = []
    birds = []        #position of the birds

    for g in genomes:
        net = neat.nn.FeedForwardNetwork(g, config)
        nets.append(net)
        birds.append(Bird(230, 350))
        ge.append(g)
        g.fitness = 0

    base = Base(730)     #base height at bottom of the screen
    pipes = [Pipe(600)]     #changing width changes rate of pipe spawn
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()

    score = 0     #point score after successfully pass through pipe

    run = True
    while run:
        clock.tick(30)
        for event in pygame.event.get():     #if any events happen, it loops
            if event.type == pygame.QUIT:
                run = False

        pipe_ind = 0
        if len(birds) > 0:
            if len(pipes) > 1 and birds[0].x > pipes[0].x + pipes[0].PIPE_TOP.get_width():
                pipe_ind = 1

        add_pipe = False
        rem = []     #list that removes pipes when off screen
        for pipe in pipes:         #collision between pipe and bird
            for x, bird in enumerate(birds):      #1.1: for every collision, the value 1 is removed from the fitness score.
                if pipe.collide(bird):            #1.2: Prevents favoring the birds that go far and bump into the pipes.
                    ge[x].fitness -= 1
                    birds.pop(x)      #removes the bird that is associated with the neural network
                    nets.pop(x)
                    ge.pop(x)

                if not pipe.passed and pipe.x < bird.x:
                    pipe.passed = True
                    add_pipe = True

            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                rem.append(pipe)

            pipe.move()

        if add_pipe:        #add new pipe after passing through pipe
            score += 1
            for g in ge:
                g.fitness += 5       #gain 5 fitness points. Encourages bird to go through more pipes
            pipes.append(Pipe(600))      #changing width changes the rate of pipe spawn
        
        for r in rem:
            pipes.remove(r)

        for x, bird in enumerate(birds):
            if bird.y + bird.img.get_height() >= 730:      #hitting the ground results in losing
                birds.pop(x)
                nets.pop(x)
                ge.pop(x)

        base.move()
        draw_window(win, bird, pipes, base, score)

    pygame.quit()
    quit()

#----------------------------------------------------#

main()

def run(config_path):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
    neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)

    p = neat.Population(config)       #setting the population

    p.add_reporter(neat.StdOutReporter(True))    #gives us the output
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    champ = p.run(main,50)          #call the main function and the number of generations

if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)      #gives us the path to the directory we're currently in
    config_path = os.path.join(local_dir, "config-feedforward.txt")
    run(config_path)
