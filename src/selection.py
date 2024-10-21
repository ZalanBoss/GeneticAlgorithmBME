from agent import *
from constants import INITAL_POP
import numpy as np

def selection(agents):
    fitness_vals = np.zeros(100)
    counter = 0
    while counter < INITAL_POP:
        fitness_vals[counter] = agents[counter].fitness()
    
    sorted_indices = np.argsort(fitness_vals)
    fitness_vals = fitness_vals[sorted_indices]
    agents = agents[sorted_indices]
    sum_of_fitness = np.sum(fitness_vals)
    normal_fitness = fitness_vals/sum_of_fitness
    chosen_indices = np.random.choice(len(normal_fitness), size = 2, replace = False, p = normal_fitness)
    return (agents[chosen_indices[0]], agents[chosen_indices[1]])
