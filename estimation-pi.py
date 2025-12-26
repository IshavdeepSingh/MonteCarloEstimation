import numpy as np
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

    return axis()
plt.show()

axis = plot_construction()

N_samples = np.arange(1, 1000) # an array of samples from 1 to 1000 
pi_counter = 0 #this will be our number of dots in the circle 

dot_x = []
dot_y = []

dots_color = []
pi_array = []


for N in N_samples:
    x = np.random.uniform(-1,1)
    y = np.random.uniform(-1,1)

    dots_x.append(x)
    dots_x.append(y)

    #check if the coordinates of this particular dot is within the circle

    if np.sqrt(x**2 + y**2) <= 1: #if the point is within the radius
        pi_counter += 1  
        dots_color.append('red') # if it is indeed in the circle 

    else:
        dots_color.append('blue') #if not in circle 

    
    probability = pi_counter/N_samples 
    approx_pi = 4*probability

    pi_array.append(approx_pi)

