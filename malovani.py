import pygame
from random import randrange

SIRKA = 960
VYSKA = 540
POZADI = (255, 255, 255)

pygame.init()
okno = pygame.display.set_mode((SIRKA, VYSKA))
pygame.display.set_caption('Malování')
hodinky = pygame.time.Clock()

pismo = pygame.font.SysFont('Ubuntu', 50)
text = []
cary = []
barva = (0, 0, 0)

for t in ('Spusť kliknutím', '...'):
    text.append(
        pismo.render(t, True, (0, 130, 0), POZADI)
    )

def tiskni_text():
    vyska = 0
    for řádek in text:
        vyska += řádek.get_height() + 5
    y = (VYSKA - vyska) / 2

    for i, řádek in enumerate(text):
        okno.blit(řádek, ((SIRKA - řádek.get_width()) / 2, y))
        y += řádek.get_height() + 5

def kresli():
    for cara in cary:
        if len(cara['body']) > 1:
            pygame.draw.lines(okno, cara['barva'], False, cara['body'], 4)
        else:
            pygame.draw.circle(okno, cara['barva'], cara['body'][0], 2)

obrazovka = 'úvodní'
kreslim = False
bezi = True
while bezi:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            bezi = False
        elif udalost.type == pygame.MOUSEBUTTONDOWN:
            if obrazovka == 'kreslení':
                kreslim = True
                cary.append({
                    'body': [udalost.pos],
                    'barva': barva
                })
            else:
                obrazovka = 'kreslení'
        elif udalost.type == pygame.MOUSEMOTION:
            if kreslim:
                cary[-1]['body'].append(udalost.pos)
        elif udalost.type == pygame.MOUSEBUTTONUP:
            kreslim = False
        elif udalost.type == pygame.KEYUP:
            if udalost.key == pygame.K_SPACE:
                barva = (randrange(0, 256), randrange(0, 256), randrange(0, 256))

                if kreslim:
                    body = []
                    if len(cary) > 0:
                        body.append(cary[-1]['body'][-1])

                    cary.append({
                        'body': body,
                        'barva': barva
                    })

    okno.fill(POZADI)
    if obrazovka == 'úvodní':
        tiskni_text()
    elif obrazovka == 'kreslení':
        kresli()

    pygame.display.update()
    hodinky.tick(30)

pygame.quit()
