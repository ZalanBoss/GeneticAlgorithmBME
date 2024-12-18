import os
import assets
#=======
import numpy as np

### TODO: REMOVE FROM CONSTANTS
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
### 

FPS = 75
TITLE = "Genetic Algorithm"

CHECKPOINT_RADIUS = 15
SIMULATION_TIME = 1200
PARENT_PATH = os.path.join(os.path.dirname(__file__), '..')
MAX_ACC = 50000
MAX_ANG_ACC = 5000
SEN_SIZE = 54
SEN_POINT_RADIUS = 6
MAX_VEL = 150
MAX_ANG_VEL = 3
INITAL_POP = 50
DAMPING_FACTOR = 0.45
AGENT_SIZE = 15
MUTATION_CHANCE = 0.01

AGENT_INITAIL_Y = SCREEN_HEIGHT/2
AGENT_INITAIL_X = 35

MAP =  assets.track
GREEN = MAP[100, 100]
BLACK = MAP[400, 300]
RED = MAP[0,0] # will change it

