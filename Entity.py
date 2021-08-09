#imports
from random import choice as rng
from random import randint

# class which holds information for every single entity
import Evolution


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
        self.fitness = 1
        for x in range(len(self.target)):
            if self.dna[x] == self.target[x]:
                self.fitness += 1

    def crossover_by_selection(self, dnaA, dnaB):
        temp_dna = dnaA.dna[:10]
        temp_dna += dnaB.dna[10:]
        self.dna = self.mutation(temp_dna)

    def mutation(self, temp_dna):
        temp = ""
        for char in temp_dna:
            mutated = randint(0, 100)
            if mutated < 1:
                temp += rng(self.dna_pool)
            else:
                temp += char
        return temp