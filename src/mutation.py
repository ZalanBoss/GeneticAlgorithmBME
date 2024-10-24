import numpy as np
from agent import *
from constants import MUTATION_CHANCE

def mutation(agent:Agent):
    chromosome = agent.chromosome
    flat_genes = chromosome.flattened()
    random_mutation = np.random.rand()
    if random_mutation <= MUTATION_CHANCE:
        mutation_number = np.random.randint(1, int(flat_genes.size*MUTATION_CHANCE))
        for mutations in range(mutation_number):
            random_index = np.random.randint(0, 2*9*5)
            mutation_value = np.random.randint(-5000, 5000)
            flat_genes[random_index] = mutation_value
    new_chromosome = flat_genes.reshape(chromosome.shape)
    return new_chromosome

def proper_mutation(genes):
    mutation = np.random.random((INITAL_POP, 2, 9, 5)) < 0.001
    genes = (1-mutation) * genes + mutation * np.random.normal(-5000, 5000, (INITAL_POP, 2, 9, 5))
    