import os
from pathlib import Path
import matplotlib.pyplot as plt

"""
script_dir = Path(__file__).parent
img_path = script_dir / '..' / 'assets' / 'mytrack.png'
img_path = str(img_path)

track = plt.imread(img_path)
"""

def get_track(p):
    script_dir = Path(__file__).parent
    if p.map == 1:
        img_path = script_dir / '..' / 'assets' / 'mytrack.png'
    elif p.map == 2:
        img_path = script_dir / '..' / 'assets' / 'map2.png'
    else:
        img_path = script_dir / '..' / 'assets' / 'map3.png'
    img_path = str(img_path)
    return plt.imread(img_path)



def track_path(p):
    script_dir = Path(__file__).parent
    if p.map == 1:
        img_path = script_dir / '..' / 'assets' / 'mytrack.png'
    elif p.map == 2:
        img_path = script_dir / '..' / 'assets' / 'map2.png'
    else:
        img_path = script_dir / '..' / 'assets' / 'map3.png'
    img_path = str(img_path)
    return img_path