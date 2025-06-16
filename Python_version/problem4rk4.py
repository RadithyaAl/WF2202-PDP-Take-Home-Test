import matplotlib.pyplot as plt

NIM = 13123031 # nim > 8 digit
NIM = str(NIM)
I = 1500 
L = 200
E = int(NIM[3:8])
M = -int(NIM[4:8]) # M is negative because the moment is clockwise
coeff = M / (E*I)

# system of equation
def f1(x, y, z):
    return z
def f2(x, y, z):
    return (coeff)*(1+z**2)**(3/2)

# Initial conditions
x = 0
y = 0      # y(0)
z = 0      # z(0)
h = 20
x_end = L

x_values = [x]
y_values = [y]
z_values = [z]

n_steps = int((x_end - x) / h)

# Runge-Kutta 4th order loop
for i in range(n_steps):
    x = x_values[i]
    y1 = y_values[i]
    y2 = z_values[i]

    # Compute RK4 coefficients
    k1_1 = h * f1(x, y1, y2)
    k1_2 = h * f2(x, y1, y2)

    k2_1 = h * f1(x + h/2, y1 + k1_1/2, y2 + k1_2/2)
    k2_2 = h * f2(x + h/2, y1 + k1_1/2, y2 + k1_2/2)

    k3_1 = h * f1(x + h/2, y1 + k2_1/2, y2 + k2_2/2)
    k3_2 = h * f2(x + h/2, y1 + k2_1/2, y2 + k2_2/2)

    k4_1 = h * f1(x + h, y1 + k3_1, y2 + k3_2)
    k4_2 = h * f2(x + h, y1 + k3_1, y2 + k3_2)
    """
    y1_values[i+1] = y1 + (k1_1 + 2*k2_1 + 2*k3_1 + k4_1) / 6
    y2_values[i+1] = y2 + (k1_2 + 2*k2_2 + 2*k3_2 + k4_2) / 6
    """
    # Update y and z
    y = y + (k1_1 + 2*k2_1 + 2*k3_1 + k4_1) / 6
    z = z + (k1_2 + 2*k2_2 + 2*k3_2 + k4_2) / 6
    x = x + h

    x_values.append(x)
    y_values.append(y)
    z_values.append(z)

def RK4_distributor():
    return x_values, y_values, z_values

"""plt.title(f"beam deflection (NIM : {NIM})")
plt.plot(x_values, y_values, marker='o')
plt.xlabel("x(mm)")
plt.ylabel("y(mm)")
plt.grid(True)
plt.show()"""