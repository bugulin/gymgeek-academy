#!/usr/bin/env python3
import pygame
from pygame.locals import *

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
FPS = 30

# Colors
WHITE = (255, 255, 255)
RED   = (250,  50,  50)
GREEN = (  0, 200,   0)
BLUE  = (  0,   0, 250)
ORANGE= pygame.Color('orange')
BLACK = (  0,   0,   0)

BGCOLOR = BLACK


class GraphicsProgram:
    running = False

    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Graphics Program')
        self.clock = pygame.time.Clock()

    def draw(self):
        pygame.draw.polygon(self.surface, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
        pygame.draw.line(self.surface, BLUE, (60, 60), (120, 60), 4)
        pygame.draw.line(self.surface, BLUE, (120, 60), (60, 120))
        pygame.draw.line(self.surface, BLUE, (60, 120), (120, 120), 4)
        pygame.draw.circle(self.surface, BLUE, (300, 50), 20, 0)
        pygame.draw.ellipse(self.surface, RED, (300, 250, 40, 80), 1)
        pygame.draw.rect(self.surface, ORANGE, (200, 150, 100, 50))

    def run(self):
        self.running = True

        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.running = False

            self.surface.fill(BGCOLOR)
            self.draw()
            pygame.display.update()
            self.clock.tick(FPS)

    def __del__(self):
        pygame.quit()


if __name__ == '__main__':
    app = GraphicsProgram()
    app.run()
