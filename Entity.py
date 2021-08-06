#imports
from random import choice as rng

# class which holds information for every single entity


class Entity:
    def __init__(self):
        self.target = 'Sein oder nicht sein'
        self.dna_pool = ' aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
        self.dna = ""

    def rng_dna(self):
        for i in range(len(self.target)):
            self.dna += rng(self.dna_pool)
        return self.dna

    def calc_fitness(self):
        fitness = 1
        for x in range(len(self.target)):
            if self.dna[x] == self.target[x]:
                fitness += 1

        return fitness