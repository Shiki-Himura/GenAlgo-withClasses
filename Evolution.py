# imports
from Entity import Entity
from random import choice as rng

# base class which holds information about everything connected to a DNA entity


class Generation:
    def __init__(self):
        self.origin = []
        self.heritage = []
        self.pop_size = 2000
        self.mut_rate = 1
        self.fitness = 1
        self.generation = 0
        self.is_Target = False

    def generate_origin(self):
        entry = Entity()
        temp_origin = []
        for i in range(self.pop_size):
            entry.rng_dna()
            entry.calc_fitness()
            self.origin.append(entry)
        self.heritage = self.dna_list(self.origin)

        for x in range(self.pop_size):
            dnaA = rng(self.heritage)
            dnaB = rng(self.heritage)
            entry.crossover_by_selection(dnaA, dnaB)
            temp_origin.append(entry)
        self.origin = temp_origin

    def dna_list(self, origin):
        temp = []
        for x in origin:
            if x.fitness == 1:
                temp.append(x)
            else:
                temp += x.fitness * [x]
        return temp
