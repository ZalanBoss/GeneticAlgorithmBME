from agent import *
from constants import INITAL_POP
import numpy as np

def selection(agents, p):
    fitness_vals = np.zeros(100)
    counter = 0
    while counter < int(p.init_pop):
        fitness_vals[counter] = agents[counter].fitness()
    
    sorted_indices = np.argsort(fitness_vals)
    fitness_vals = fitness_vals[sorted_indices]
    agents = agents[sorted_indices]
    sum_of_fitness = np.sum(fitness_vals)
    normal_fitness = fitness_vals/sum_of_fitness
    chosen_indices = np.random.choice(len(normal_fitness), size = 2, replace = False, p = normal_fitness)
    return (agents[chosen_indices[0]], agents[chosen_indices[1]])

def proper_selection(agents, p):
    fitness_vals = np.zeros(int(p.init_pop))
    genes= np.zeros((int(p.init_pop), 2, 9, 5))
    for i in range(len(fitness_vals)):
        fitness_vals[i] = agents[i].fitness()
    for i in range(len(agents)):
        genes[i] = agents[i].chromosome
    agents = (-fitness_vals).argsort()
    print(f"The best score: {np.max(fitness_vals)}")
    #genes = (-fitness_vals).argsort()
    #genes = (-fitness_vals).argsort()
#>>>>>>> update_code
    for i in range(int(p.init_pop)//2, int(p.init_pop)):
        parent1, parent2 = np.random.choice(range(int(p.init_pop)//2), 2, replace=False)
        repro = np.random.random((2,9,5)) < 0.5
        genes[agents[i]] = genes[agents[parent1]]*repro + genes[agents[parent2]]*(1-repro)
    
    return genes

        
