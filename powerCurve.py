def nonVectorized(P_rated, U, U_rated, U_cin, U_cout, interpFlag):
    """This function computes the power curve of a wind turbine"""

    import numpy as np
    import matplotlib.pyplot as plt

    # check for the interpFlag type
    if interpFlag == 0:

        # linear interpolation
        g = (U - U_cin) / (U_rated - U_cin)

    else:

        # cubic interpolation
        g = U**3 / U_rated**3

    # initialize the power array
    P = np.zeros(len(U))

    # compute the power curve
    for i in range(len(U)):
        if U[i] < U_cin:
            P[i] = 0
        elif U[i] < U_rated:
            P[i] = g[i] * P_rated
        elif U[i] >= U_rated and U[i] < U_cout:
            P[i] = P_rated
        else:
            P[i] = 0

    return P


def vectorized(P_rated, U, U_rated, U_cin, U_cout, interpFlag):
    """This function computed the power curve using the vectorization"""

    import numpy as np
    import matplotlib.pyplot as plt

    # check for the interpFlag type
    if interpFlag == 0:

        # linear interpolation
        g = (U - U_cin) / (U_rated - U_cin)

    else:

        # cubic interpolation
        g = U**3 / U_rated**3

    # initialize the power array
    P = np.zeros(len(U))

    # compute the power curve
    P = np.where(
        U < U_cin,
        0,
        np.where(U < U_rated, g * P_rated, np.where(U < U_cout, P_rated, 0)),
    )

    return P
