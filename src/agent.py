import numpy as np
from constants import MAX_ACC, MAX_ANG_VEL, SEN_SIZE, SEN_POINT_RADIUS
from functions import rot_mat

class Agent():
    def __init__(self, initial_postion, initial_orientation=np.pi/2):
        # TRAITS
            # MOVEMENT
        self.position = initial_postion
        self.velocity = 0
        self.acceleration = 0
        self.orientation = initial_orientation
        self.angular_velocity = 0
            # DETECTION
        self.sensor_size = SEN_SIZE
        self.s1 = [np.array([0, 3+SEN_POINT_RADIUS*i]) for i in range(SEN_SIZE//SEN_POINT_RADIUS)]
        self.s2 = [rot_mat(np.pi/4)@np.array([i,j]) for (i,j) in self.s1]
        self.s3 = [rot_mat(-np.pi/4)@np.array([i,j]) for (i,j) in self.s1]
        self.s4 = [rot_mat(-np.pi/2)@np.array([i,j]) for (i,j) in self.s1]
        self.s5 = [rot_mat(np.pi/2)@np.array([i,j]) for (i,j) in self.s1]
        print(f"[1,0] vector rotated by 90 deg is: {rot_mat(np.pi/2)@np.array([1,0])}")
        #print(f"first se.. {self.s1}")
        self.sensor_positions = [self.s1,self.s2,self.s3,self.s4,self.s5]
        #print(f"s-s: {self.sensor_positions}")
        # INPUTS
        self.sensors = np.array([[-1,-1,-1], [-1,-1,-1], [-1,-1,-1], [-1,-1,-1], [-1,-1,-1]])
        # OUTPUTS
        self.chromosome = np.random.uniform(-10, 10, (2,3,5))
    def update(self, dt):
        self.acceleration += self.handle_input()[0]
        if self.acceleration > MAX_ACC:
            self.acceleration = MAX_ACC
        
        self.angular_velocity += self.handle_input()[1]
        #print(f"handle_input {self.handle_input()[1]}")
        if self.angular_velocity > MAX_ANG_VEL:
            self.angular_velocity = MAX_ANG_VEL
        #print(f"Initial acceleration: {self.acceleration}")
        self.velocity += self.acceleration*dt
        self.position[0] += self.velocity*np.cos(self.orientation)*dt
        self.position[1] += self.velocity*np.sin(self.orientation)*dt
        self.orientation += self.angular_velocity*dt
    def render(self):
        pass #TODO
    def handle_input(self):
        acc = np.sum(np.matmul(self.sensors,self.chromosome[0]))
        ang_vel = np.sum(np.matmul(self.sensors,self.chromosome[1]))
        #print(f"{ang_vel}")
        #print(f"{self.chromosome[0].shape}")
        return (acc, ang_vel) 
    def detection(self, point):
        pass
