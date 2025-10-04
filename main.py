import numpy as np
import matplotlib.pyplot as plt
import powerCurve as pc

# This script computes and plots the power curve of a wind turbine

# options (0 = linear, 1 = cubic)
interpFlag = 1

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


print(f"Power at U_rated = {P_rated/1e6:.1f} MW")

# call for the power curve function
P = pc.powerCurve(P_rated, U, U_rated, U_cin, U_cout, interpFlag)

# power curve chart
plt.figure(figsize=(8, 5))
plt.plot(U, P / 1e6, label="Power Curve", color="blue")  # converti in MW
plt.xlabel("Wind speed [m/s]")
plt.ylabel("Power [MW]")
plt.title("Wind Turbine Power Curve")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
