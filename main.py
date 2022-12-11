import random

import pygame
import Mono

pygame.init()
pygame.display.set_caption('Primordial Soup')

BG_COLOR = (255, 255, 255)
WIDTH, HEIGHT = 800, 600
FPS = 60
PLAYER_VEL = 5

POP = 8

window = pygame.display.set_mode((WIDTH, HEIGHT))


def draw(window, bio):
    for i in bio:
        i.draw(window)
    pygame.display.update()

def firstgen(pop=7):
    ##TEST bio for drawing and moving
    biomes = []
    while pop > 0:
        pop -= 1
        celebro = Mono.brain(3, 3, 3)
        puerpo = Mono.body(numgen=random.randrange(5, 10))
        biogen = Mono.bio(random.randrange(5), (random.randrange(0, WIDTH), random.randrange(0, HEIGHT)),
                          random.randrange(10, 50), 100, 1, puerpo, celebro)
        biomes.append(biogen)
    return biomes

def main(window):
    clock = pygame.time.Clock()
    primer = firstgen(POP)
    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        draw(window, primer)


    pygame.quit()
    quit()


if __name__ == '__main__':
    main(window)
