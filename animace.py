#!/usr/bin/env python3
import pygame
from pygame.locals import *
from random import randrange

FPS = 30

# Colors
WHITE = (255, 255, 255)
RED   = (250,  50,  50)
GREEN = (  0, 200,   0)
BLUE  = (  0,   0, 250)
ORANGE= pygame.Color('orange')
BLACK = (  0,   0,   0)

BGCOLOR = WHITE


class Snowflake:

    def __init__(self, pos=(0, 0)):
        self.pos = [pos[0] - 25, pos[1] - 25]
        self.dolu = randrange(3, 8)
        self.image = pygame.image.load('snowflake.png')

    def blit(self, surface):
        if randrange(10) == 0:
            self.pos[0] += randrange(-5, 6)
        self.pos[1] += self.dolu
        surface.blit(self.image, self.pos)


class ChristmasProgram:
    running = False

    def __init__(self):
        pygame.init()

        # Získání velikosti okna
        info = pygame.display.Info()
        self.width = info.current_w
        self.height = info.current_h

        self.surface = pygame.display.set_mode((self.width, self.height), FULLSCREEN)
        pygame.display.set_caption('Snowflakes')
        self.clock = pygame.time.Clock()

    def run(self):
        self.running = True
        vlocky = []

        while self.running:
            for udalost in pygame.event.get():
                if udalost.type == QUIT:
                    self.running = False
                elif udalost.type == KEYDOWN:
                    if udalost.key == K_ESCAPE:
                        self.running = False

                elif udalost.type == MOUSEBUTTONDOWN:
                    flake = Snowflake(udalost.pos)
                    vlocky.append(flake)

            self.surface.fill(BGCOLOR)

            for flake in vlocky:
                flake.blit(self.surface)

            pygame.display.update()
            self.clock.tick(FPS)

    def __del__(self):
        pygame.quit()


if __name__ == '__main__':
    app = ChristmasProgram()
    app.run()
