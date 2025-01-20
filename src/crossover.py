import numpy as np
from agent import *

import numpy as np
from agent import Agent

def crossover(parent1: Agent, parent2: Agent):
    gene1 = parent1.chromosome
    gene2 = parent2.chromosome
    index = np.random.randint(0, 2 * 9 * 5)  # Ensure this index is within bounds

    flat_gene1 = gene1.flatten()
    flat_gene2 = gene2.flatten()

    gene1_first_half = flat_gene1[:index]  # Fix slicing syntax
    gene2_second_half = flat_gene2[index:]  # Fix slicing syntax

    # Fix np.concatenate by passing a list of arrays
    offspring = np.concatenate([gene1_first_half, gene2_second_half]).reshape(gene1.shape)

    return offspring
