import os
#=======
import numpy as np

### TODO: REMOVE FROM CONSTANTS
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
### 

FPS = 60
TITLE = "Genetic Algorithm"

PARENT_PATH = os.path.join(os.path.dirname(__file__), '..')
MAX_ACC = 1000
MAX_ANG_ACC = 5000
SEN_SIZE = 54
SEN_POINT_RADIUS = 6
MAX_VEL = 50
MAX_ANG_VEL = 3 
INITAL_POP = 5
DAMPING_FACTOR = 0.1
AGENT_SIZE = 15

### TODO: AUTOMATE IT
GREEN = np.array([0.2, 0.1, 0.1, 1])
BLACK = np.array([0, 0, 0, 1])
MAP = np.full((800, 600, 4), 1)
###
