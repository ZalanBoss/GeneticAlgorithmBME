import sys
from constants import *  # Ensure these constants are defined
import numpy as np

class Flags():
    def __init__(self, flag):
        self.flag_set = False
        self.param_value = None
        self.args = sys.argv[1:]
        self.flag = flag
        self.flag_index = None

    def see_flag(self):
        if self.flag in self.args:
            self.flag_set = True
            self.flag_index = self.args.index(self.flag)
            # Check if a value exists after the flag
            if self.flag_index + 1 < len(self.args):
                potential_value = self.args[self.flag_index + 1]
                # Ensure it's not another flag
                if not potential_value.startswith('--'):
                    self.param_value = potential_value


def define_parameters(flag_name, default):                    
    # Process flag
    const_flag = Flags(flag_name)
    const_flag.see_flag()
    if const_flag.param_value is None:
        const = default
    else:
        try:
            const = float(const_flag.param_value)
        except ValueError:
            print(f"Error: Invalid value for {flag_name}: {const_flag.param_value}")
            sys.exit(1)
    return const


class Parameters():
    def __init__(self):
        self.max_acc = define_parameters('--maxacc', MAX_ACC)
        self.max_vel = define_parameters('--maxvel', MAX_VEL)
        self.max_ang_vel = define_parameters('--maxangvel', MAX_ANG_VEL)
        self.max_ang_acc = define_parameters('--maxangacc', MAX_ANG_ACC)
        self.simulation_time = define_parameters('--time', SIMULATION_TIME)
        self.init_pop = define_parameters('--initial', INITAL_POP)
        self.mutation_chance = define_parameters('--mutationchance', MUTATION_CHANCE)
        self.mutation_type = define_parameters('--mutationtype', 1)
        self.fitness = define_parameters('--fitness', 1)
        self.map = define_parameters('--map', 1)
        self.selection = define_parameters('--selection', 1)
        self.debug = define_parameters('--debug', 1)
        self.max_generation = define_parameters('--maxgen', 100)
        self.seed = define_parameters('--seed', 111)
        print(f"max accelecration {self.max_acc},"
              f"max velocity {self.max_vel},"
              f"max angular velocity {self.max_ang_vel}," 
              f"max angular accelecration {self.max_ang_acc},"
              f"simulation_time {self.simulation_time},"
              f"initial population {self.init_pop},"
              f"mutation chance {self.mutation_chance},"
              f"mutation type {self.mutation_type},"
              f"fitness type {self.fitness},"
              f"map {self.map},"
              f"selection {self.selection},")
