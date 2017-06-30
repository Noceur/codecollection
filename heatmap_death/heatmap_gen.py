import numpy as np
import numpy.random
import matplotlib.pyplot as plt
#from scipy.misc import imread
from scipy import misc
import scipy
from data import *
from PIL import Image, ImageEnhance




#fig, ax = plt.subplots()
#ax.plot(range(10))
#
#for item in [fig, ax]:
#	item.patch.set_visible(False)

#fig.show()
#with open('test2.png', 'w') as outfile:
#	fig.canvas.print_png(outfile)

#ax.show()

# Generate some test data
#x = np.random.randn(8873)
#y = np.random.randn(8873)
#x = data.x
#y = data.y

heatmap, xedges, yedges = np.histogram2d(x, y, bins=200)
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
#img = imread(map_fishybusiness.png)
img = misc.imread("map_fishybusiness_live.bmp")

#extent = []
#extent.append(0)
#extent.append(450)
#extent.append(0)
#extent.append(450)
print (extent)

#plt.clf() # clears current figure
#plt.scatter(x,y,img)
plt.imshow(heatmap.T, extent=extent, origin='lower')
plt.savefig('test.png',bbox_inches='tight')

plt.show()


img2 = Image.open('test.png')
img1 = Image.open('map_fishybusiness.png')
img2.putalpha(ImageEnhance.Brightness(img2.split()[3]).enhance(0.5))
img1 = Image.composite(img2, img1, img2)
#img1.save('out.png')
#img1.show()

#plt.show()