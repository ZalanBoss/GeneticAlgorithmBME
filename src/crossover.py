import numpy as np
from agent import *

def crossover(parent1:Agent, parent2:Agent):
    gene1 = parent1.chromosome
    gene2 = parent2.chromosome
    index = np.random.randint(0, 2*9*5)
    flat_gene1 = gene1.flattened()
    flat_gene2 = gene2.flattened()
    gene1_first_half = flat_gene1[0:index]
    gene1_second_half = flat_gene1[index:]
    gene2_first_half = flat_gene2[0:index]
    gene2_second_half = flat_gene2[index:]
    offspring1 = np.concatenate(gene1_first_half, gene2_second_half).reshape(gene1.shape)
    offspring2 = np.concatenate(gene2_first_half, gene1_second_half).reshape(gene2.shape)

    return (offspring1, offspring2)