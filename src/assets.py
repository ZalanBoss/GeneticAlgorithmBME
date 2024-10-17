import os
from pathlib import Path
import matplotlib.pyplot as plt


script_dir = Path(__file__).parent
img_path = script_dir / '..' / 'assets' / 'mytrack.png'
img_path = str(img_path)


track = plt.imread(img_path)

def track_path():
    return img_path










