class Agent():
    def __init__(self, initial_postion, initial_orientation):
        self.position = initial_postion
        self.velocity = [0,0]
        self.acceleration = [0,0]
        self.orientation = initial_orientation
        self.angular_velocity = 0
    def update(self, dt):
        self.velocity += self.acceleration*dt
        self.position += self.velocity*dt
        self.orientation += self.angular_velocity*dt
    def render(self):
        pass
