from agent import *
from build import *
import pygame
import numpy as np
from matplotlib import image as mpimg
from matplotlib import pyplot as plt
from parameters import *

'''def plotting(track):
    plt.imshow(track)
    plt.show()
    pass
'''
def main():
    p = Parameters()
    world = World(p)
    world.setup_world()  # tpye=ignore
    context = {"running": True}
    world.update_world(context)
    #plotting(world.track)


if __name__ == "__main__":
    main()
