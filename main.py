from agent import *
from build import *

def main():
    world = World()
    setup = world.setup_world()   
    context = {"running": True}
    world.update_world(0, context)

if __name__ == "__main__":
    main()