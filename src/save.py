import numpy as np
import agent
from constants import INITAL_POP
from pathlib import Path

script_dir = Path(__file__).parent
gene_path = script_dir / '..' / 'generations' / 'gen0' # should automate it
gene_path = str(gene_path)

def save_genes(agents):
    chromosomes = np.zeros((INITAL_POP, 2, 9, 5))
    for i in range(len(agents)):
        chromosomes[i] = agents[i].chromosome
    np.save(gene_path, chromosomes)