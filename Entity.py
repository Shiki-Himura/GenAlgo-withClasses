#imports
from random import choice as rng

# class which holds information for every single entity


class Entity:
    def __init__(self):
        self.target = 'Sein oder nicht sein'
        self.dna_pool = ' aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
        self.dna = ""
        self.fitness = 1
        self.mut_rate = 1

    def rng_dna(self):
        for i in range(len(self.target)):
            self.dna += rng(self.dna_pool)

    def calc_fitness(self):
        for x in range(len(self.target)):
            if self.dna[x] == self.target[x]:
                self.fitness += 1