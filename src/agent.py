import numpy as np
from constants import *
from functions import rot_mat
import pygame as pg

class Agent():
    def __init__(self, initial_postion, chromosome, checkpoint_coordinates, identity,
                 params,
                 initial_orientation=np.pi/2, color_bruh =(0,100,255)):           # Should add genes
        try:
            self.surface = pg.Surface((AGENT_SIZE,AGENT_SIZE) )
            self.surface.fill(color_bruh)
        
            #self.surface.fill((0,200,250))
            self.surface_original = self.surface.copy()
        except:
            pass
        self.active = 1
        self.id = identity
        self.sensor_color = (255, 0, 0)
        self.checkpoint_traversed = 0
        self.checkpoint_coordinates = checkpoint_coordinates
        self.params = params
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

    def update(self, dt, check_coords, p):
        # Update lifetime, road time, acceleration, etc.
        if self.active:
            self.lifetime += dt
        if self.is_on_road:
            self.roadtime += dt
        if self.active:
            #   Handle inputs for acceleration and angular acceleration
            self.acceleration += self.handle_input()[0] * 0.1
            #self.acceleration = np.clip(self.acceleration, -p.max_acc, p.max_acc)
            self.acceleration = np.tanh(self.acceleration)*p.max_acc
           
            self.angular_acceleration += self.handle_input()[1]
            #self.angular_acceleration = np.clip(self.angular_acceleration, -MAX_ANG_ACC, MAX_ANG_ACC)
            self.angular_acceleration = np.tanh(self.angular_acceleration)*p.max_ang_acc
            self.collide_checkpoint(self.checkpoint_coordinates)
            # Update velocity and angular velocity
            self.velocity += self.acceleration * dt if self.is_on_road else self.acceleration * dt * DAMPING_FACTOR
            
            #self.velocity = np.clip(self.velocity, -MAX_VEL/5, MAX_VEL) if self.is_on_road else np.clip(self.velocity, -p.max_vel/5, p.max_vel) * DAMPING_FACTOR
            self.velocity = np.tanh(self.velocity)*p.max_vel if self.is_on_road else np.tanh(self.velocity)*p.max_vel*DAMPING_FACTOR
        
            self.angular_velocity += self.angular_acceleration * dt
            #self.angular_velocity = np.clip(self.angular_velocity, -MAX_ANG_VEL, MAX_ANG_VEL)
            self.angular_velocity = np.tanh(self.angular_velocity)*p.max_ang_vel

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
        try:
            self.surface_rect = self.surface.get_rect(center=(self.position[0], self.position[1]))
        except:
            pass
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
                    #print(f"the ith checkpoint: {self.checkpoint_traversed}")
                else:
                    self.checkpoint_coordinates = np.concatenate((self.checkpoint_coordinates[:i], self.checkpoint_coordinates[i+1:]))
                    #print(f"{self.id} traversed checkpoint {self.checkpoint_traversed}")
                break
        
        pass
    def convert_sensor_postion(self):
        absolute_sensor_position = np.zeros(self.sensor_positions.shape)
        for i in range(len(self.sensor_positions)):
            absolute_sensor_position[i] = (self.position + self.sensor_positions[i])
        return absolute_sensor_position
    
    def render(self, screen, debug=True):
        try:
            screen.blit(self.surface, self.surface_rect)
            for sensor_position in self.convert_sensor_postion():
                for s in sensor_position:
                    if debug:
                        pg.draw.circle(screen, self.sensor_color, (s[0], s[1]), 1)
                    else:
                        pass
        except:
            pass

    def handle_input(self):
        self.detection(self.convert_sensor_postion())
        if self.active:
            acc = 0.5*np.sum(np.matmul(self.sensors,self.chromosome[0]))
            ang_acc = 0.5*np.sum(np.matmul(self.sensors,self.chromosome[1]))
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
        
        return self.active*(self.roadtime*12 + 7*self.distance_travelled/self.lifetime + 3*int(self.params.fitness)*self.checkpoint_traversed + self.velocity * 2 )
    

#self.active*50000+self.lifetime*3.4 + self.roadtime*150 + 25*self.distance_travelled/self.lifetime + self.velocity * 200 + 20000*self.checkpoint_traversed
        #return self.active*2000+self.lifetime*3.4 + self.roadtime*2 + 100*self.distance_travelled/self.lifetime + 20000*self.checkpoint_traversed + self.velocity * 200
