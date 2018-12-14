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
BLACK = (  0,   0,   0)


class Activity:

    def __init__(self, program):
        self.program = program

    def vykresli(self):
        pass

    def zkontroluj_udalosti(self, udalost):
        pass


class Uvod(Activity):

    def __init__(self, program):
        Activity.__init__(self, program)

        self.font = pygame.font.SysFont('Ubuntu', 150)
        self.text = self.font.render('Vítejte', True, BLACK, WHITE)

    def vykresli(self):
        self.program.povrch.blit(
            self.text,
            ((SCREEN_WIDTH - self.text.get_width()) // 2, (SCREEN_HEIGHT - self.text.get_height()) // 2)
        )

    def zkontroluj_udalosti(self, udalost):
        if udalost.type == MOUSEBUTTONDOWN:
            self.program.aktualni = Hra(self.program)


class Hra(Activity):

    def __init__(self, program):
        Activity.__init__(self, program)

        self.x = 0
        self.y = 0

    def vykresli(self):
        pygame.draw.rect(self.program.povrch, RED, (self.x, self.y, 30, 30))

    def zkontroluj_udalosti(self, udalost):
        if udalost.type == KEYDOWN:
            self.x += 5
            if udalost.key == K_p:
                self.y += 1

        elif udalost.type == MOUSEBUTTONDOWN:
            self.program.aktualni = Uvod(self.program)


class GraphicsProgram:
    running = False

    def __init__(self):
        pygame.init()
        self.povrch = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Had (snake)')
        self.clock = pygame.time.Clock()

        activity = {
            'Úvodní stránka': Uvod(self),
            'Hra samotná': Hra(self),
        }
        self.aktualni = activity['Úvodní stránka']


    def run(self):
        self.running = True

        while self.running:
            for udalost in pygame.event.get():
                if udalost.type == QUIT:
                    self.running = False
                elif udalost.type == KEYDOWN:
                    if udalost.key == K_ESCAPE:
                        self.running = False

                self.aktualni.zkontroluj_udalosti(udalost)

            self.povrch.fill(WHITE)

            # Vykreslení aktuální aktivity
            self.aktualni.vykresli()

            pygame.display.update()
            self.clock.tick(FPS)

    def __del__(self):
        pygame.quit()


if __name__ == '__main__':
    app = GraphicsProgram()
    app.run()
