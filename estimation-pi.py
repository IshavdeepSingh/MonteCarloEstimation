import numpy as np

N_samples = np.arange(1, 1000) # an array of samples from 1 to 1000 
pi_counter = 0 #this will be our number of dots in the circle 

for N in N_samples:
    x = np.random.uniform(-1,1)
    y = np.random.uniform(-1,1)

    #check if the coordinates of this particular dot is within the circle

    if np.sqrt(x**2 + y**2) <= 1: #if the point is within the radius
        pi_counter += 1  

    
    probability = pi_counter/N_samples 

    print(4*probability)

