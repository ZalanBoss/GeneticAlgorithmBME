#!/bin/bash

# Define possible values for each parameter
mutation_types=(0 1)
initial_pops=(15 50)
maps=(0 1 2)
fitness_types=(0 1)
mutation_chances=(0.000125 0.0025 0.05)

seed=301  # Start seed from 1

# Loop over all possible combinations
for mutation_type in "${mutation_types[@]}"; do
  for initial in "${initial_pops[@]}"; do
    for map in "${maps[@]}"; do
      for fitness in "${fitness_types[@]}"; do
        for mutation_chance in "${mutation_chances[@]}"; do
          echo "Running simulation with seed=$seed, mutationtype=$mutation_type, initial=$initial, map=$map, fitness=$fitness, mutationchance=$mutation_chance"

          # Run the Python script with current parameters and seed
          python3 src/main.py --seed $seed \
                              --mutationtype $mutation_type \
                              --selection $mutation_type \
                              --maxacc 250 \
                              --maxvel 75 \
                              --initial $initial \
                              --map $map \
                              --fitness $fitness \
                              --mutationchance $mutation_chance \
                              --maxgen 50

          # Increment seed for next run
          ((seed++))
        done
      done
    done
  done
done