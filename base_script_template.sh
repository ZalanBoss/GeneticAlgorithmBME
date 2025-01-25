#!/bin/bash

# Define possible values for each parameter
mutation_types=(0 1)
selections=(0 1)
max_accs=(75 250 475)
max_vels=(75 150 225)
initial_pops=(15 50 100)
maps=(0 1 2)
fitness_types=(0 1)
mutation_chances=(0.000125 0.0025 0.05)

seed=1  # Start seed from 1

# Loop over all possible combinations
for mutation_type in "${mutation_types[@]}"; do
  for selection in "${selections[@]}"; do
    for max_acc in "${max_accs[@]}"; do
      for max_vel in "${max_vels[@]}"; do
        for initial in "${initial_pops[@]}"; do
          for map in "${maps[@]}"; do
            for fitness in "${fitness_types[@]}"; do
              for mutation_chance in "${mutation_chances[@]}"; do
                echo "Running simulation with seed=$seed, mutationtype=$mutation_type, selection=$selection, maxacc=$max_acc, maxvel=$max_vel, initial=$initial, map=$map, fitness=$fitness, mutationchance=$mutation_chance"

                # Run the Python script with current parameters and seed
                python3 src/main.py --seed $seed \
                                    --mutationtype $mutation_type \
                                    --selection $selection \
                                    --maxacc $max_acc \
                                    --maxvel $max_vel \
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
    done
  done
done
