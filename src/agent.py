import numpy as np
from constants import *
from functions import rot_mat
import pygame as pg


class Agent():
    def __init__(self, initial_postion, chromosome, initial_orientation=np.pi/2, ):           # Should add genes
        self.surface = pg.Surface((AGENT_SIZE,AGENT_SIZE))
<<<<<<< HEAD
        self.surface.fill((200,0,200))
=======
        self.surface.fill((0,200,250))
>>>>>>> c9d6e168244c665c722a9810566a5751b3dca79e
        self.surface_original = self.surface.copy()

        # TRAITS
            # MOVEMENT
        self.lifetime = 0
        self.distance_travelled = 0
        self.roadtime = 0
        self.position = (initial_postion)
        self.velocity = 0
        self.acceleration = 0
        self.orientation = initial_orientation
        self.angular_velocity = 0
        self.angular_acceleration = 0
            # DETECTION
        self.is_on_road = True
        self.sensor_size = SEN_SIZE
        s1 = [np.array([0, 3+SEN_POINT_RADIUS*i]) for i in range(SEN_SIZE//SEN_POINT_RADIUS)]
        s2 = [rot_mat(np.pi/4)@np.array([i,j]) for (i,j) in s1]
        s3 = [rot_mat(-np.pi/4)@np.array([i,j]) for (i,j) in s1]
        s4 = [rot_mat(-np.pi/2)@np.array([i,j]) for (i,j) in s1]
        s5 = [rot_mat(np.pi/2)@np.array([i,j]) for (i,j) in s1]
        #print(f"[1,0] vector rotated by 90 deg is: {rot_mat(np.pi/2)@np.array([1,0])}")
        #print(f"first se.. {self.s1}")
        self.sensor_positions = np.asarray([s1,s2,s3,s4,s5]) # When working with detector ADD self.position
        #print(f"s-s: {self.sensor_positions}")
        # INPUTS
        self.sensors = np.full((5,9), -1)
        # OUTPUTS
        self.chromosome = chromosome
    def update(self, dt):
        # Update lifetime, road time, acceleration, etc.
        self.lifetime += 1
        if self.is_on_road:
            self.roadtime += 1

        #   Handle inputs for acceleration and angular acceleration
        self.acceleration += self.handle_input()[0] * 0.1
        self.acceleration = np.clip(self.acceleration, -MAX_ACC, MAX_ACC)
       
        self.angular_acceleration += self.handle_input()[1]
        self.angular_acceleration = np.clip(self.angular_acceleration, -MAX_ANG_ACC, MAX_ANG_ACC)

        # Update velocity and angular velocity
        self.velocity += self.acceleration * dt if self.is_on_road else self.acceleration * dt * DAMPING_FACTOR
        
        self.velocity = np.clip(self.velocity, -MAX_VEL/5, MAX_VEL) if self.is_on_road else np.clip(self.velocity, -MAX_VEL/5, MAX_VEL) * DAMPING_FACTOR
    
        self.angular_velocity += self.angular_acceleration * dt
        self.angular_velocity = np.clip(self.angular_velocity, -MAX_ANG_VEL, MAX_ANG_VEL)

        # Update position based on velocity and orientation
        self.position = (
            self.position[0] + self.velocity * np.cos(self.orientation) * dt,
            self.position[1] + self.velocity * np.sin(self.orientation) * dt
        )
        self.distance_travelled += self.velocity * dt

        # Update orientation
        self.orientation += self.angular_velocity * dt

        # Always rotate the original surface based on the current orientation (to avoid the growing square issue)
        #rotated_surface = pg.transform.rotate(self.surface_original, -np.degrees(self.orientation))

        # Re-center the surface
        #self.surface = rotated_surface
        self.surface_rect = self.surface.get_rect(center=(self.position[0], self.position[1]))

        # Update sensor positions with the new rotation
        for i in range(len(self.sensor_positions)):
            self.sensor_positions[i] = (rot_mat(self.angular_velocity * dt) @ self.sensor_positions[i].T).T
    def convert_sensor_postion(self):
        absolute_sensor_position = np.zeros(self.sensor_positions.shape)
        for i in range(len(self.sensor_positions)):
            absolute_sensor_position[i] = (self.position+self.sensor_positions[i])
        return absolute_sensor_position
    def render(self, screen):
        #pg.draw.circle(screen, (255,0,0), (self.position[0], self.position[1]), 10) 
        screen.blit(self.surface, self.surface_rect)
        for sensor_position in self.convert_sensor_postion():
            for s in sensor_position:
                pg.draw.circle(screen, (255,0,0), (s[0], s[1]), 1)

    def handle_input(self):
        self.detection(self.convert_sensor_postion())
        self.collide()        

        acc = 1*np.sum(np.matmul(self.sensors,self.chromosome[0]))
        ang_acc = 1*np.sum(np.matmul(self.sensors,self.chromosome[1]))
        #print(f"{ang_vel}")
        #print(f"{self.chromosome[0].shape}")
        return (acc, ang_acc)
    
    def collide(self):
        pos = self.position#.round()
        if np.allclose(MAP[int(pos[1]), int(pos[0])], GREEN):
            self.is_on_road = False
        else:
            self.is_on_road = True 
            

    def detection(self, sensor_positions):
        x_min = 0
        x_max = 799
        y_min = 0
        y_max = 599                  # loop-hellt megoldom
        detect_positions = sensor_positions.round()         # én is hányok tőle
        for sensor in range(len(detect_positions)):
            for point in range(len(detect_positions[sensor])):
                x = max(x_min, min(int(detect_positions[sensor, point, 0]), x_max))
                y = max(y_min, min(int(detect_positions[sensor, point, 0]), y_max))
                
    
                if np.array_equal(MAP[y,x], GREEN):
                    self.sensors[sensor, point] = 1
                    #print(f"sensor{sensor} point{point} ({x},{y})")

                else:
                    self.sensors[sensor, point] = -1
                    #print(f"sensor{sensor} point{point} ({x},{y})")
                    

        #print(f"sensor1:{self.sensors[0]}")
        
        
        
        

