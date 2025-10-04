import numpy as np
import matplotlib.pyplot as plt
import powerCurve as pc
import time

# This script computes and plots the power curve of a wind turbine

# options (0 = linear, 1 = cubic)
interpFlag = 0

# fluid properties
rho = 1.225  # Kg/m^3

# turbine properties
D = 90
Cp = 0.40
P_rated = 3e6

# wind properties
U = np.linspace(0, 30, 1000)
U_rated = 11
U_cin = 3
U_cout = 25

if interpFlag not in (0, 1):
    raise ValueError("interpFlag must be 0 (linear) or 1 (cubic)")

# addition of python time module to measure the execution time of the (NON-VECTORIZED) \
# power curve function
# Note: time.time() was giving inconsistent results on my PC, so I used time.perf_counter()
timeStart = time.perf_counter()
P1 = pc.nonVectorized(P_rated, U, U_rated, U_cin, U_cout, interpFlag)
timeEnd = time.perf_counter()
dt1 = timeEnd - timeStart
print(f"The execution time is{dt1:.10f} seconds")

# addition of python time module to measure the execution time of the (VECTORIZED) \
# power curve function
# Note: time.time() was giving inconsistent results on my PC, so I used time.perf_counter()
timeStart = time.perf_counter()
P2 = pc.vectorized(P_rated, U, U_rated, U_cin, U_cout, interpFlag)
timeEnd = time.perf_counter()
dt2 = timeEnd - timeStart
print(f"The execution time is{dt2:.10f} seconds")

# power curve chart
plt.figure(figsize=(8, 5))

plt.subplot(2, 1, 1)
plt.plot(U, P1 / 1e6, label="Power Curve", color="blue")
plt.xlabel("Wind speed [m/s]")
plt.ylabel("Power [MW]")
plt.title("Power Curve (built without vectorization)")
plt.grid(True)
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(U, P2 / 1e6, label="Power Curve", color="blue")
plt.xlabel("Wind speed [m/s]")
plt.ylabel("Power [MW]")
plt.title("Power Curve (built with vectorization)")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
