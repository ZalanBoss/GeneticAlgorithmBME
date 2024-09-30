import os
from pathlib import Path
import matplotlib.pyplot as plt

# Get the absolute path to the current script
script_dir = Path(__file__).parent

# Build the relative path to the image
img_path = script_dir / '..' / 'assets' / 'mytrack.png'

# Convert to string if needed for matplotlib
img_path = str(img_path)

# Now read the image

track = plt.imread(img_path)







