from agent import *

class World():
    def __init__(self):
        self.fps = 60
        self.title = ""
        self.agents = []
    def update_world(self, dt, context):
        while context["running"]:
            for agent in self.agents:
                agent.update(0)
                agent.render()
            break
    def setup_world(self):
        agent = Agent([1,1],1)
        self.agents.append(agent)