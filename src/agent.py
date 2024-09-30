import numpy as np
from constants import MAX_ACC, MAX_ANG_ACC, SEN_SIZE, SEN_POINT_RADIUS, MAX_VEL, MAX_ANG_VEL, GREEN, BLACK, MAP
from functions import rot_mat

class Agent():
    def __init__(self, initial_postion, initial_orientation=np.pi/2):           # Should add genes
        # TRAITS
            # MOVEMENT
        self.position = initial_postion
        self.velocity = 0
        self.acceleration = 0
        self.orientation = initial_orientation
        self.angular_velocity = 0
        self.angular_acceleration = 0
            # DETECTION
        self.sensor_size = SEN_SIZE
        s1 = [np.array([0, 3+SEN_POINT_RADIUS*i]) for i in range(SEN_SIZE//SEN_POINT_RADIUS)]
        s2 = [rot_mat(np.pi/4)@np.array([i,j]) for (i,j) in s1]
        s3 = [rot_mat(-np.pi/4)@np.array([i,j]) for (i,j) in s1]
        s4 = [rot_mat(-np.pi/2)@np.array([i,j]) for (i,j) in s1]
        s5 = [rot_mat(np.pi/2)@np.array([i,j]) for (i,j) in s1]
        #print(f"[1,0] vector rotated by 90 deg is: {rot_mat(np.pi/2)@np.array([1,0])}")
        #print(f"first se.. {self.s1}")
        self.sensor_positions = np.asarray([s1,s2,s3,s4,s5])
        #print(f"s-s: {self.sensor_positions}")
        # INPUTS
        self.sensors = np.full((5,9), -1)
        # OUTPUTS
        self.chromosome = np.random.uniform(-10, 10, (2,9,5))
    def update(self, dt):
        self.acceleration += self.handle_input()[0]
        self.acceleration = np.min([MAX_ACC,self.acceleration])
        
        self.angular_acceleration += self.handle_input()[1]
        #print(f"handle_input {self.handle_input()[1]}")
        self.angular_acceleration = np.min([MAX_ANG_ACC, self.angular_acceleration])
        #print(f"Initial acceleration: {self.acceleration}")
        self.velocity += self.acceleration*dt
        self.velocity = np.min([self.velocity, MAX_VEL])
        self.angular_velocity += self.angular_acceleration*dt
        self.angular_velocity = np.min([self.angular_velocity, MAX_ANG_VEL])

        self.position[0] += self.velocity*np.cos(self.orientation)*dt
        self.position[1] += self.velocity*np.sin(self.orientation)*dt
        self.orientation += self.angular_velocity*dt
    def render(self):
        pass #TODO
    def handle_input(self):
        acc = np.sum(np.matmul(self.sensors,self.chromosome[0]))
        ang_acc = np.sum(np.matmul(self.sensors,self.chromosome[1]))
        #print(f"{ang_vel}")
        #print(f"{self.chromosome[0].shape}")
        return (acc, ang_acc) 
    def detection(self, sensor_positions):                  # loop-hellt megoldom
        detect_positions = sensor_positions.round()         # én is hányok tőle
        for sensor in range(len(detect_positions)):
            for point in range(len(detect_positions[sensor])):
                x = detect_positions[sensor, point, 0]
                y = detect_positions[sensor, point, 1]
                if MAP[x, y] == GREEN:
                    self.sensors[sensor, point] = 1
                else:
                    self.sensors[sensor, point] = -1
    def fitness(self):
        """
        frames on path (or grass) / total frames  (for staying on the track)
        distance travelled  (for actually moving)
        optimal directon
        """
        pass #TODO logic


        
        

