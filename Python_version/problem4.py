import matplotlib.pyplot as plt

NIM = 13123031 # interchangeable with 13123031
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

for i in range(n_steps):
    x = x_values[-1]
    
    # k1
    k1_1 = h * f1(x, y, z)
    k1_2 = h * f2(x, y, z)

    # k2
    k2_1 = h * f1(x + h/2, y + k1_1/2, z + k1_2/2)
    k2_2 = h * f2(x + h/2, y + k1_1/2, z + k1_2/2)

    # Update y and z
    y = y + k2_1
    z = z + k2_2
    x = x + h

    x_values.append(x)
    y_values.append(y)
    z_values.append(z)

def RK2_distributor():
    return x_values, y_values, z_values

"""plt.title(f"beam deflection (NIM : {NIM})")
plt.plot(x_values, y_values, marker='o')
plt.xlabel("x(mm)")
plt.ylabel("y(mm)")
plt.grid(True)
plt.show()"""