# imports
from Entity import Entity

# base class which holds information about everything connected to a DNA entity


class Generation:
    def __init__(self):
        self.origin = []
        self.heritage = []
        self.pop_size = 2000
        self.mut_rate = 1
        self.fitness = 0
        self.generation = 0
        self.is_Target = False

    def generate_origin(self):
        for i in range(self.pop_size):
            entry = Entity()
            self.origin.append((entry.rng_dna(), entry.calc_fitness()))
        print(self.origin)