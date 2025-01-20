from agent import *
from pathlib import Path
from constants import *
from assets import track_path
import numpy as np
from save import *
from selection import proper_selection, selection
from mutation import proper_mutation, mutation
import sys

import pygame as pg
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
    def __init__(self, p):

        self.fps = FPS
        self.display = False#True
        self.parameters = p
        np.random.seed(int(self.parameters.seed))
        if '-d' in sys.argv:
            self.display = True
        self.title = TITLE
        self.generation = 0
        self.agents = np.zeros(int(self.parameters.init_pop), dtype=object)
        if self.display:
            try:
                self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
                self.track = pg.image.load(track_path())
                self.clock = pg.time.Clock()
            except:
                pass
        self.debug_mode = int(self.parameters.debug) # See checkpoints
        self.dt = 0#self.clock.tick(self.fps)/1000
        self.timestep = 0
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
        #self.global_timer = 0
    def update_world(self, context):
        while context["running"] and self.generation <= self.parameters.max_generation:
            self.timestep += 1
            #self.dt = self.clock.tick(self.fps) / 1000
            #self.global_timer += self.dt
            #print(f"{self.timestep} ~ {SIMULATION_TIME}")
            if (self.timestep > float(self.parameters.simulation_time)):
                """
                for i in self.agents:
                    print(f"id: {i.id}, fitness: {i.fitness()}")
                    if (i.fitness() > 80000):
                        np.save(f"genes/gene_{i.id}_{i.fitness()}",i.chromosome)
                """
                self.restart_simulation()
            if self.display:
                self.pygame_handler(context)
            for agent in self.agents:
                #print(f"{agent.sensor_positions}")
                if agent.active:
                    agent.update(1/self.fps, self.checkpoint_coords, self.parameters)
                    if self.display:
                        agent.render(self.screen, self.debug_mode)
                
            if self.debug_mode and self.display:
                for c in self.checkpoint_coords:
                    try: 
                        pg.draw.circle(self.screen, (255,0,255), (c[0], c[1]), CHECKPOINT_RADIUS)
                    except:
                        pass

            if self.display:
                try: 
                    pg.display.flip()
                except:
                    pass
            #context["running"] = False
            #break #comment for rendering window
    def setup_world(self):
        if self.generation == 0:
            #genes_load = np.load("genes/gene_1_94564.9795999999.npy")
            for i in range(int(self.parameters.init_pop)):
                rand_chromo = np.random.uniform(-5000, 5000, (2,9,5))
                #rand_chromo = np.random.uniform(-1, 1, (2,9,5))
                if True:
                    agent = Agent(np.array([AGENT_INITAIL_X,AGENT_INITAIL_Y]), rand_chromo, self.checkpoint_coords, i, params=self.parameters) # x=0 + np.random.rand()*500 
                else:
                    agent = Agent(np.array([AGENT_INITAIL_X,AGENT_INITAIL_Y]), genes_load, self.checkpoint_coords, i, color_bruh=(0,255,255)) # x=0 + np.random.rand()*500 



                # print(i)
                self.agents[i] = agent
                #print(f"chromosome {self.agents[i].chromosome}")
            
        #print(f"Agent genome {agent.chromosome}")
        if self.display:
            try: 
                pg.init()
                self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
                pg.display.set_caption(self.title)
            except:
                pass

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
        save_genes(self.agents, self.generation, self.parameters)
        self.generation += 1
        #self.global_timer = 0
        self.timestep = 0
        if self.parameters.selection == 1:
            new_agents_genes = proper_selection(self.agents, self.parameters)
        else:
            new_agents_genes = np.zeros((int(self.parameters.init_pop), 2, 9, 5))
            for i in range(int(self.parameters.init_pop)):
                offspring = selection(self.agents, self.parameters)
                new_agents_genes[i] = offspring
        if self.parameters.mutation_type == 1:
            proper_mutation(new_agents_genes, self.parameters)
        else:
            mutation(new_agents_genes, self.parameters) # TODO: Mutation
            
        new_agents = np.zeros(int(self.parameters.init_pop), dtype=object)
        for i in range(int(self.parameters.init_pop)):
            new_agents[i] = Agent(np.array([AGENT_INITAIL_X,AGENT_INITAIL_Y]), new_agents_genes[i], self.checkpoint_coords, i, params=self.parameters)
        self.agents = new_agents

        print("restarting simulation")

        # Save
        # Crossover / Mutation
    def load_simulation(self):
        self.agents = load_genes(self.generation)

