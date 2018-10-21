import pygame
from pygame.locals import *

WIDTH = 1000
HEIGHT = 500
FPS = 30

RED = (200, 50, 50)
WHITE = (255, 255, 255)

pygame.init()
s = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Úvod do pygame')
pygame.mouse.set_pos(10, 100)
clock = pygame.time.Clock()

running = True
painting = False
points = [(10, 10), (100, 10), (100, 100), (10, 100)]

x = 0
y = 0

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEMOTION:
            #x = event.pos[0]
            y = event.pos[1]
            if painting:
                points.append(event.pos)
        elif event.type == MOUSEBUTTONDOWN:
            painting = not painting

    s.fill(WHITE)
    
    x = x + 5
    if x >= WIDTH:
        x = -50

    pygame.draw.rect(s, RED, (x, y, 50, 50))
    pygame.draw.lines(s, (200, 200, 250), False, points, 3)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
