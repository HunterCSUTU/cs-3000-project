import opensimplex
import numpy
import time
import matplotlib.pyplot as plt
import seaborn as sns
# the number has to be between 0 and 1 with precision of 2.

# Generates 2D OpenSimplex noise using Numpy arrays for increased performance.
# :param x: numpy array of x-coords
# :param y: numpy array of y-coords
# :return:  2D numpy array of shape (y.size, x.size) with the generated noise
# for the supplied coordinates
start_time = time.time()
rng = numpy.random.default_rng(seed=0)
ix, iy = rng.random(100), rng.random(100) # generating a 1,000 by 1,000 array (takes 8.6 seconds to complete so it's not too easy )
arr = opensimplex.noise2array(ix, iy)
end_time = time.time()
time_creation = end_time - start_time

sns.heatmap(arr, annot=True, cmap="YlGnBu", linewidths=.5, fmt=".2f", cbar_kws={'shrink':.75})
plt.show()