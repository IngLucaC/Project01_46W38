def estimate_PI(num_points, seed=None):
    """Estimate the value of PI using the Monte Carlo method"""

    import numpy as np

    # create random number generator
    rng = np.random.default_rng(seed)  # seed can be None or an integer

    # generate number of random points between 0 and 1
    x = rng.random(num_points)
    y = rng.random(num_points)
    d = np.sqrt(x**2 + y**2)

    # count the number of points inside the single quadrant
    count_in = np.sum(d <= 1)

    # calculate pi
    pi = 4 * count_in / num_points

    return pi
