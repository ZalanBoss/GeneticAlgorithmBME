from agent import *
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
        self.agents = []
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.track = pg.image.load(track_path())
        self.clock = pg.time.Clock()

        self.dt = 0#self.clock.tick(self.fps)/1000
    def update_world(self, context):
        while context["running"]:
            self.dt = self.clock.tick(self.fps) / 1000
            self.pygame_handler(context)
            for agent in self.agents:
                agent.update(self.dt)
                #print(f"{agent.sensor_positions}")
                agent.render(self.screen)
            pg.display.flip()
            #context["running"] = False
            #break #comment for rendering window
    def setup_world(self):
        for i in range(INITAL_POP):
            rand_chromo = np.random.uniform(-5000, 5000, (2,9,5))
            agent = Agent(np.array([20,SCREEN_HEIGHT/2]), rand_chromo) # x=0 + np.random.rand()*500 
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
