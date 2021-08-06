# imports
from Entity import Entity

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
        for i in range(self.pop_size):
            entry = Entity()
            entry.rng_dna()
            entry.calc_fitness()
            self.origin.append((entry.dna, entry.fitness))
        print(self.origin)
        self.heritage = self.dna_list(self.origin)

    def dna_list(self, origin):
        temp = []
        for x in origin:
            if x[1] == 1:
                temp.append(x[0])
            else:
                temp += x[1] * [x[0]]
        print(len(temp))
        return temp

    #def crossover_by_selection(self, heritage):
