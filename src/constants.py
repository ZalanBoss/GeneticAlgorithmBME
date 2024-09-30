import os
import assets
#=======
import numpy as np

### TODO: REMOVE FROM CONSTANTS
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
### 

FPS = 60
TITLE = "Genetic Algorithm"

PARENT_PATH = os.path.join(os.path.dirname(__file__), '..')
MAX_ACC = 10
MAX_ANG_ACC = 10
SEN_SIZE = 54
SEN_POINT_RADIUS = 6
MAX_VEL = 200
MAX_ANG_VEL = 200
INITAL_POP = 250
DAMPING_FACTOR = 0.01


MAP = assets.track
GREEN = MAP[100, 100]
BLACK = MAP[400, 300]



