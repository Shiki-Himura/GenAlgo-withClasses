# imports
import Entity
from random import choice as rng

# base class which holds information about everything connected to a DNA entity


class Generation:
    def __init__(self):
        self.origin = []
        self.heritage = []
        self.pop_size = 2000
        self.mut_rate = 1
        self.fitness = 1
        self.is_Target = False
        self.best_match = ""
        self.gen = 0

    def generate_origin(self):
        temp = []
        for i in range(self.pop_size):
            entry = Entity.Entity()
            entry.rng_dna()
            entry.calc_fitness()
            temp.append(entry)
        self.origin = temp
        self.generate_heritage()

    def generate_heritage(self):
        temp_rng = self.dna_list()

        for x in range(self.pop_size):
            entry = Entity.Entity()
            dnaA = rng(temp_rng)
            dnaB = rng(temp_rng)
            entry.crossover_by_selection(dnaA, dnaB)
            self.heritage.append(entry)
            entry.calc_fitness()
            if entry.dna == entry.target:
                print(entry.dna)
                self.is_Target = True
                exit()
        self.origin = []
        self.origin = self.heritage
        self.heritage = []

    def dna_list(self):
        temp = []
        for x in self.origin:
            if x.fitness == 1:
                temp.append(x)
            else:
                temp += x.fitness * [x]
        return temp
