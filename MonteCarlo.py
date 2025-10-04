import numpy as np
import matplotlib.pyplot as plt
import estimate_PI as ep

# Draw a square and inscribe a quadrant

# total sample count (the higher the better to approximate pi)
num_points = 100000

# function call
pi = ep.estimate_PI(num_points, seed=None)

# print the output
print(pi)
