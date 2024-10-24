import numpy as np
from constants import *
from functions import rot_mat
import pygame as pg

class Agent():
    def __init__(self, initial_postion, chromosome, checkpoint_coordinates, initial_orientation=np.pi/2, ):           # Should add genes
        self.surface = pg.Surface((AGENT_SIZE,AGENT_SIZE) )
        self.surface.fill((200,0,200))
        self.surface.fill((0,200,250))
        self.surface_original = self.surface.copy()
        self.active = 1
        self.sensor_color = (255, 0, 0)
        self.checkpoint_traversed = 0
        self.checkpoint_coordinates = checkpoint_coordinates
        # TRAITS
        # MOVEMENT
        self.lifetime = 0
        self.distance_travelled = 0
        self.roadtime = 0
        self.position = initial_postion
        self.velocity = 0
        self.acceleration = 0
        self.orientation = initial_orientation
        self.angular_velocity = 0
        self.angular_acceleration = 0

        # DETECTION
        self.is_on_road = True
        self.sensor_size = SEN_SIZE
        s1 = [np.array([0, 3 + SEN_POINT_RADIUS * i]) for i in range(SEN_SIZE // SEN_POINT_RADIUS)]
        s2 = [rot_mat(np.pi / 4) @ np.array([i, j]) for (i, j) in s1]
        s3 = [rot_mat(-np.pi / 4) @ np.array([i, j]) for (i, j) in s1]
        s4 = [rot_mat(-np.pi / 2) @ np.array([i, j]) for (i, j) in s1]
        s5 = [rot_mat(np.pi / 2) @ np.array([i, j]) for (i, j) in s1]
        self.sensor_positions = np.asarray([s1, s2, s3, s4, s5])

        # INPUTS
        self.sensors = np.full((5, 9), -1)

        # OUTPUTS
        self.chromosome = chromosome

    def update(self, dt, check_coords):
        # Update lifetime, road time, acceleration, etc.
        if self.active:
            self.lifetime += dt
        if self.is_on_road:
            self.roadtime += 1
        if self.active:
            #   Handle inputs for acceleration and angular acceleration
            self.acceleration += self.handle_input()[0] * 0.1
            self.acceleration = np.clip(self.acceleration, -MAX_ACC, MAX_ACC)
           
            self.angular_acceleration += self.handle_input()[1]
            self.angular_acceleration = np.clip(self.angular_acceleration, -MAX_ANG_ACC, MAX_ANG_ACC)
            self.collide_checkpoint(self.checkpoint_coordinates)
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
        self.surface_rect = self.surface.get_rect(center=(self.position[0], self.position[1]))
        # Update sensor positions with the new rotation
        if self.active:
            for i in range(len(self.sensor_positions)):
                self.sensor_positions[i] = (rot_mat(self.angular_velocity * dt) @ self.sensor_positions[i].T).T
    def collide_checkpoint(self, check_coords):
        for i,val in enumerate(check_coords):
            if (AGENT_SIZE/2 + CHECKPOINT_RADIUS) >= np.sqrt((val[0]-self.position[0])**2+(val[1]-self.position[1])**2):
                #self.sensor_color = (200,0,200)
                #self.active = 0
                self.checkpoint_traversed+=1
                if i-1 > len(check_coords):
                    self.checkpoint_coordinates = self.checkpoint_coordinates[:i]
                    print(f"the ith checkpoint: {self.checkpoint_traversed}")
                else:
                    self.checkpoint_coordinates = np.concatenate((self.checkpoint_coordinates[:i], self.checkpoint_coordinates[i+1:]))
                    print(f"checkpoint_traversed : {self.checkpoint_traversed}")
                break
        
        pass
    def convert_sensor_postion(self):
        absolute_sensor_position = np.zeros(self.sensor_positions.shape)
        for i in range(len(self.sensor_positions)):
            absolute_sensor_position[i] = (self.position + self.sensor_positions[i])
        return absolute_sensor_position

    def render(self, screen):
        screen.blit(self.surface, self.surface_rect)
        for sensor_position in self.convert_sensor_postion():
            for s in sensor_position:
                pg.draw.circle(screen, self.sensor_color, (s[0], s[1]), 1)

    def handle_input(self):
        self.detection(self.convert_sensor_postion())
        if self.active:
            acc = 1*np.sum(np.matmul(self.sensors,self.chromosome[0]))
            ang_acc = 1*np.sum(np.matmul(self.sensors,self.chromosome[1]))
        else:
            acc = 0
            ang_acc = 0
        #print(f"{ang_vel}")
        #print(f"{self.chromosome[0].shape}")
        self.collide()        
        return (acc, ang_acc)
    def collide(self):
        pos = self.position
        if np.allclose(MAP[int(pos[1]), int(pos[0])], GREEN):
            self.is_on_road = False
        else:
            self.is_on_road = True 

        if (pos[0] > SCREEN_WIDTH - 10):
            self.active = 0
        elif (pos[0] < 0):
            self.active = 0
        elif (pos[1] > SCREEN_HEIGHT - 10):
            self.active = 0
        elif (pos[1] < 0):
            self.active = 0

    def detection(self, sensor_positions):
        detect_positions = np.round(sensor_positions).astype(int)
        x_positions = np.clip(detect_positions[..., 0], 0, SCREEN_WIDTH - 1)
        y_positions = np.clip(detect_positions[..., 1], 0, SCREEN_HEIGHT - 1)
        map_values = MAP[y_positions, x_positions]
        black_mask = np.all(map_values == BLACK, axis=-1)
        self.sensors[black_mask] = -1
        self.sensors[~black_mask] = 1 

    def fitness(self):
        
        return self.active*200+self.lifetime*1.4 + self.roadtime*5 + 3*self.distance_travelled/self.lifetime
