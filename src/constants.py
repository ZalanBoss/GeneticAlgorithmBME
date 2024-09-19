import numpy as np

### TODO: REMOVE FROM CONSTANTS
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
### 

FPS = 60
TITLE = "Genetic Algorithm"

MAX_ACC = 10
MAX_ANG_ACC = 10
SEN_SIZE = 54
SEN_POINT_RADIUS = 6
MAX_VEL = 200
MAX_ANG_VEL = 200
INITAL_POP = 250

### TODO: AUTOMATE IT
GREEN = np.array([0.2, 0.1, 0.1, 1])
BLACK = np.array([0, 0, 0, 1])
MAP = np.full((800, 600, 4), 1)
###
