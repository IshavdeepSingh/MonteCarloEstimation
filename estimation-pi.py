import numpy as np
import time 
import matplotlib.pyplot as plt 

def plot_construction():
    fig, axis = plt.subplots(1, 2, figsize=(10, 5))

    # Generated Dots
    axis[0].set_title('Random Generated Dots')
    axis[0].set_aspect('equal')
    axis[0].set_xlim([-1, 1])
    axis[0].set_ylim([-1, 1])

    # Plot of Approximation
    axis[1].set_title('Approximating π ~')
    axis[1].set_xlim([0, 1000])
    axis[1].set_ylim([0, 10])
    axis[1].grid()

    return axis

N_samples = np.arange(1, 1000) # an array of samples from 1 to 1000 
pi_counter = 0 #this will be our number of dots in the circle 

for N in N_samples:
    x = np.random.uniform(-1,1)
    y = np.random.uniform(-1,1)

    #check if the coordinates of this particular dot is within the circle

    if np.sqrt(x**2 + y**2) <= 1: #if the point is within the radius
        pi_counter += 1  

    
    probability = pi_counter/N_samples 
    approx_pi = 4*probability
