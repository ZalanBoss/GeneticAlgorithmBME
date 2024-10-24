from agent import *
from pathlib import Path
import pygame as pg
from constants import *
from assets import track_path
import numpy as np


from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

class World():
    def __init__(self):
        self.fps = FPS
        self.title = TITLE
        self.generation = 0
        self.agents = []
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.track = pg.image.load(track_path())
        self.clock = pg.time.Clock()
        self.debug_mode = True # See checkpoints
        self.dt = 0#self.clock.tick(self.fps)/1000
        self.checkpoint_coords = np.array([
            [170, 430],
            [335, 360],
            [435, 250],
            [565, 175],
            [740, 290],
            [565, 430],
            [435, 350],
            [335, 230],
            [170, 165],
        ])
        self.global_timer = 0
    def update_world(self, context):
        while context["running"]:
            self.dt = self.clock.tick(self.fps) / 1000
            self.global_timer += self.dt
            if (self.global_timer > SIMULATION_TIME):
                for i in self.agents:
                    print(f"id: {i.id}, fitness: {i.fitness()}")
                    if (i.fitness() > 80000):
                        np.save(f"genes/gene_{i.id}_{i.fitness()}",i.chromosome)
                self.restart_simulation()
                break
            self.pygame_handler(context)
            for agent in self.agents:
                agent.update(self.dt, self.checkpoint_coords)
                #print(f"{agent.sensor_positions}")
                agent.render(self.screen)
                
            if self.debug_mode:
                for c in self.checkpoint_coords:
                    pg.draw.circle(self.screen, (255,0,255), (c[0], c[1]), CHECKPOINT_RADIUS)


            pg.display.flip()
            #context["running"] = False
            #break #comment for rendering window
    def setup_world(self):
        genes_load = np.load("genes/gene_1_94564.9795999999.npy")
        for i in range(INITAL_POP):
            rand_chromo = np.random.uniform(-5000, 5000, (2,9,5))
            if i != 3:
                agent = Agent(np.array([AGENT_INITAIL_X,AGENT_INITAIL_Y]), rand_chromo, self.checkpoint_coords, i) # x=0 + np.random.rand()*500 
            else:
                agent = Agent(np.array([AGENT_INITAIL_X,AGENT_INITAIL_Y]), genes_load, self.checkpoint_coords, i, color_bruh=(0,255,255)) # x=0 + np.random.rand()*500 



            #print(rand_chromo)
            self.agents.append(agent) 
        #print(f"Agent genome {agent.chromosome}")
        pg.init()
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption(self.title)
        
    def pygame_handler(self, context):
        #self.screen.fill((255, 255, 255))
        self.screen.blit(self.track, (0, 0))
        for event in pg.event.get():
        # Did the user hit a key?
            if event.type == KEYDOWN:
                
            # Was it the Escape key? If so, stop the loop.
                if event.key == K_ESCAPE:
                    context["running"] = False
            elif event.type == QUIT:
                context["running"] = False
    def restart_simulation(self):
        self.generation += 1
        self.global_timer = 0
        # Save
        # Crossover / Mutation
        pass
    def load_simulation(self):
        pass
