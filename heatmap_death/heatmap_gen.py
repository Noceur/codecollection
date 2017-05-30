import numpy as np
import numpy.random
import matplotlib.pyplot as plt
#from scipy.misc import imread
from scipy import misc
import scipy
from data import *

# Generate some test data
#x = np.random.randn(8873)
#y = np.random.randn(8873)
#x = data.x
#y = data.y

heatmap, xedges, yedges = np.histogram2d(x, y, bins=200)
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
#img = imread(map_fishybusiness.png)
img = misc.imread("map_fishybusiness_live.bmp")

plt.clf()
#plt.scatter(x,y,img)
plt.imshow(heatmap.T, extent=extent, origin='lower')
plt.show()