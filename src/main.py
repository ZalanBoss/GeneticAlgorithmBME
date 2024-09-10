from agent import *
from build import *
import pygame
import numpy

def main():
    world = World()
    setup = world.setup_world()   
    context = {"running": True}
    world.update_world(context)

if __name__ == "__main__":
    main()