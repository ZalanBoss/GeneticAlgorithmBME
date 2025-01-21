import csv
import os
import numpy as np

def save_best_fitness(generation, best_fitness, params):
    # Construct filename dynamically from params object attributes
    filename = os.path.join(
        "logs/fitness",
        f"seed{params.seed}"
        f"fitness_mut_type{params.mutation_type}_"
        f"mut_chance{params.mutation_chance}_"
        f"selection{params.selection}_"
        f"max_acc{params.max_acc}_"
        f"max_vel{params.max_vel}_"
        f"init_pop{params.init_pop}_"
        f"map{params.map}_"
        f"fitness{params.fitness}.csv"
    )

    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([generation, best_fitness])

def save_genes(genes, params):
    filename = os.path.join(
        "logs/genes",
        f"seed{params.seed}_"
        f"fitness_mut_type{params.mutation_type}_"
        f"mut_chance{params.mutation_chance}_"
        f"selection{params.selection}_"
        f"max_acc{params.max_acc}_"
        f"max_vel{params.max_vel}_"
        f"init_pop{params.init_pop}_"
        f"map{params.map}_"
        f"fitness{params.fitness}.npz"
    )

    os.makedirs(os.path.dirname(filename), exist_ok=True)

    np.savez_compressed(filename, genes)

    print(f"succesfully saved: {filename}")