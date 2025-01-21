import numpy as np

def rot_mat(theta):
    return np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])

def get_best_fitness(agents, p):
    fitness_vals = np.zeros(int(p.init_pop))
    
    # Calculate fitness values safely
    for counter in range(int(p.init_pop)):
        fitness_vals[counter] = max(0, agents[counter].fitness())
    return np.max(fitness_vals)

def get_agent_genes(agents, p):
    genes = np.zeros((int(p.init_pop), 2, 9, 5))
    for counter in range(len(agents)):
        genes[counter] = agents[counter].chromosome
    return genes