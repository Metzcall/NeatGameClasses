import random

import pygame.draw

GENSET = ['A', 'B', 'C', 'D']


class bio():
    def __init__(self, name, position, scale, health, generation, body, brain):
        self.name = name
        self.position = position
        self.scale = scale
        self.health = health
        self.generation = generation
        self.body = body
        self.brain = brain

    def draw(self, win):
        pygame.draw.circle(win, (255, 0, 0), self.position, self.scale)

    def move(self, position):
        pass

    def evolve(self, brain, body):
        pass


class body():
    def __init__(self, **kwargs):
        #core header = 00 ... genome header = 11 by default and has 10 (instead of default 4) genes
        self.fullpayload = []
        self.core = genome(**{'header': '00'})
        self.eyes = genome(**{'header': '01'})
        self.mouth = genome(**{'header': '10'})
        self.genome = genome(numgen = kwargs.get('numgen',10))
        self.fullpayload.append(self.core.payload)
        self.fullpayload.append(self.eyes.payload)
        self.fullpayload.append(self.mouth.payload)
        self.fullpayload.append(self.genome.payload)

        print (self.fullpayload)



class genome():
    def __init__(self, **kwargs):
        self.header = kwargs.get('header', '11')
        self.footer = kwargs.get('footer', '00')
        #call with numgen for numgen genes
        self.payload = kwargs.get('payload', genome.randgen(self,kwargs.get('numgen',4)))

    def randgen(self, genes):
        i = 0
        payload = []
        while i < genes:
            payload.append(random.choice(GENSET))
            i += 1
        return payload


class brain():
    def __init__(self, inputL, hiddenL, outputL):
        self.inputL = inputL
        self.hiddenL = hiddenL
        self.outputL = outputL


