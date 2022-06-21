# Test 1 Mandelbrot Sets
import numpy as np
import matplotlib.pyplot as plt
from numpy import newaxis

def mandelbrot(n, N_max, threshold):
    '''
    compute the Mandelbrot fractal with the Mandelbrot iteration
    Parameters
    ----------
    n : length of Mandelbrot
    N_max : max number of iteratioin
    threshold : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    
    #construct an n×n grid (2D array) of points (x, y) 
    #in range [−2, 1]×[−1.5, 1.5]
    x = np.linspace(-2, 1, n)
    y = np.linspace(-1.5, 1.5, n)

    #corresponding complex values c = x + yi 
    c = x[:, newaxis] + 1j*y[newaxis, :]

    
    #perform the iteration as outlined above to compute z
    #for each complex value in the grid
    z = c
    for j in range (N_max):
        z = z**2 + c
    
    # form a 2-D boolean array mask indicating which points are in the set
    mask = (abs(z) < threshold)
    return mask
    
# experiment the function with different n   
n = 10000
N_max = 50
threshold = 50
 
mask = mandelbrot(n, N_max, threshold)    
    
    
#save the result to an image   
plt.imshow(mask.T, extent=[-2, 1, -1.5, 1.5 ])
plt.gray()
plt.savefig('mandelbrot.png')