from agent import *
from build import *
import pygame
import numpy as np


def main():
    world = World()
    world.setup_world()  # tpye=ignore
    context = {"running": True}
    world.update_world(context)


if __name__ == "__main__":
    main()
