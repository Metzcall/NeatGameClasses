import random
import pygame
import matplotlib.pyplot as plt

import Mono

pygame.init()
pygame.display.set_caption('Primordial Soup')

BG_COLOR = (255, 255, 255)
WIDTH, HEIGHT = 800, 600
FPS = 20

POP = 5
AGING = 2

window = pygame.display.set_mode((WIDTH, HEIGHT))


def draw(win, bio):
    win.fill((0, 0, 0))
    for i in bio:
        i.draw(win)
    pygame.display.update()


def firstgen(pop):
    # TEST bio for drawing and moving
    biomes = []
    while pop > 0:
        pop -= 1
        celebro = Mono.brain(3, 3, 3)
        puerpo = Mono.body(numgen=random.randrange(5, 10))
        biogen = Mono.bio('Mono' + str(pop), (random.randrange(0, WIDTH), random.randrange(0, HEIGHT)), 1, puerpo,
                          celebro)
        biogen.att()
        biomes.append(biogen)
    return biomes


def action(biomes):
    biosize = []
    biohealth = []
    for i in biomes:
        if i.health <= 0:
            biomes.remove(i)
        dice = random.randint(1, 3)
        if dice ==1:
            i.health -= AGING * 2
            mov = tuple(val + (random.randint(i.speed * (-1), i.speed)) for val in i.position)
            i.position = mov
        if dice == 2:
            i.health -= AGING
            i.scale += 1
        biosize.append(i.scale)
        biohealth.append(i.health)
    return biosize,biohealth

def pinta(gentime):
    i=0
    genpro=[]
    for item in gentime:
        proce = (sum(item)/len(item))
        x= [i+1]
        i+=1
        gentime.remove(item)
        genpro.append(proce)
    plt.plot(genpro)
    plt.show()

def main(win):
    clock = pygame.time.Clock()
    primer = firstgen(POP)
    sizetime = []
    healthtime = []
    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        sizetime.append(action(primer)[0])
        healthtime.append(action(primer)[1])
        draw(win, primer)
        if len(primer) == 0:
            break

    pinta(sizetime)

    pygame.quit()
    quit()


if __name__ == '__main__':
    main(window)
