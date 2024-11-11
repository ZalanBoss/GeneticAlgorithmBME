import numpy as np
import agent
from constants import INITAL_POP
from pathlib import Path



def save_genes(agents, generation):
    gen_num = 'gen' + str(generation)
    script_dir = Path(__file__).parent
    gene_path = script_dir / '..' / 'generations' / gen_num 
    gene_path = str(gene_path)
    chromosomes = np.zeros((INITAL_POP, 2, 9, 5))
    for i in range(len(agents)):
        chromosomes[i] = agents[i].chromosome
    np.save(gene_path, chromosomes)

def load_genes(generation):
    dir_script = 'gen' + str(generation)
    generation_dir = Path(__file__).parent
    generation_path = generation_dir / '..' / 'generations' / dir_script
    generation_path = str(generation_path) + '.npy'
    return np.load(generation_path)


