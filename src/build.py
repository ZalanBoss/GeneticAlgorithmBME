from agent import *
import pygame as pg
from constants import *

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
        self.screen = None
        #self.clock = pg.clock

        self.dt = 0#self.clock.tick(self.fps)/1000
    def update_world(self, context):
        while context["running"]:
            self.pygame_handler(context)
            for agent in self.agents:
                agent.update(self.dt)
                agent.render()
            break #comment for rendering window
    def setup_world(self):
        agent = Agent([1,1])
        self.agents.append(agent)
        
        print(f"Agent genome {agent.chromosome}")
        pg.init()
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption(self.title)
        
    def pygame_handler(self, context):
        self.screen.fill((255, 255, 255))
        for event in pg.event.get():
        # Did the user hit a key?
            if event.type == KEYDOWN:
                
            # Was it the Escape key? If so, stop the loop.
                if event.key == K_ESCAPE:
                    context["running"] = False
            elif event.type == QUIT:
                context["running"] = False
