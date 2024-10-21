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

PARENT_PATH = os.path.join(os.path.dirname(__file__), '..')
MAX_ACC = 50000
MAX_ANG_ACC = 5000
SEN_SIZE = 54
SEN_POINT_RADIUS = 6
MAX_VEL = 150
MAX_ANG_VEL = 3 
INITAL_POP = 8
INITAL_POP = 100
DAMPING_FACTOR = 0.55
AGENT_SIZE = 15


MAP =  assets.track
GREEN = MAP[100, 100]
BLACK = MAP[400, 300]
RED = MAP[0,0] # will change it

