import sys
from constants import MAX_ACC, MAX_VEL  # Ensure these constants are defined

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

class Parameters():
    def __init__(self):
        # Process --ma flag
        max_acc_flag = Flags('--ma')
        max_acc_flag.see_flag()
        if max_acc_flag.param_value is None:
            self.max_acc = MAX_ACC
        else:
            try:
                self.max_acc = float(max_acc_flag.param_value)
            except ValueError:
                print(f"Error: Invalid value for --ma: {max_acc_flag.param_value}")
                sys.exit(1)

        # Process --mv flag
        max_vel_flag = Flags('--mv')
        max_vel_flag.see_flag()
        if max_vel_flag.param_value is None:
            self.max_vel = MAX_VEL
        else:
            try:
                self.max_vel = float(max_vel_flag.param_value)
            except ValueError:
                print(f"Error: Invalid value for --mv: {max_vel_flag.param_value}")
                sys.exit(1)

