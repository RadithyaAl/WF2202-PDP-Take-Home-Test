import pdpcore
"""


okay, let say that we have list A, x, and b

okay, let the matrix is in form of Ax = b, then 

A[i]*x[i] = b[i]

let us pick the first value of the matrix, as the variable to be  found

A[i][i]*b[i] = the rest of the equations. 

and store all the equation in a list. but how to do that?




# Example system:
# 4x + y + z = 7
# x + 3y + z = -8
# x + y + 5z = 6

A = [
    [10, -2, -1, -1],
    [-2, 10, -1, -1],
    [-1, -1, 10, -2],
    [-1, -1, -2, 10]
]

b = [3, 15, 27, -9]

# Initial guess for x, y, z
x = [0 for i in range(len(A))]


result = pdpcore.gauss_seidel(A, b, x)

print(result)
okay. it works dude

"""



"""
implicit solution for heat conduction equation

assume that the wall is a long rod, then,
Ts ==============Ti================Ts
length = 10 cm
initial temperature = 0 C (uniform)
Ts1 = 100 C
Ts2 = 50 C
k = 0.835 ft/hr
basic equation = (dT/dt) = k(d**T/dx**2)

let say the partition is dx= 2 and dt=0.1

the matrix is U = [[100, 0, 0, 0, 50],
                   [X1T1, X2T1, X3T1, X4T1,],
                    ......... ]
"""
"""
# coefficient constants
k = 0.835
rod_length = 10
dx = 2
dt = 0.1
time_limit = 0.5

# --- Adjust dx if it doesn't fit rod_length exactly ---
x_intervals = round(rod_length / dx)
dx = rod_length / x_intervals   # recomputed dx to fit exactly
x_node_count = x_intervals + 1  # total nodes = intervals + 1

# Continue as usual
y_node_count = int(time_limit / dt) + 1
lamb = (k * dt) / (dx ** 2)

U = [[0 for i in range(x_node_count)] for j in range(y_node_count)]
"""
"""# define the initial condition
for t in range(y_node_count):
    U[t][0] = 100.0  # Left boundary
    U[t][-1] = 50.0  # Right boundary
"""


"""
okay now that the matrices for both space and time is defined. next is perform the operation using implicit method.
implicit method equation is 
-lambda*U[i+1][j-1] + (1+2*lambda)*U[i+1][j] - lambda*U[i+1][j+1] = U[i][j]
i = time
j = spatial
which an be stored as linear equations and solve for U[i][j]
"""
"""

# Interior node count
N = x_node_count - 2

# create linear equations
A = [[0.0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    A[i][i] = 1 + 2 * lamb
    if i > 0:
        A[i][i - 1] = -lamb
    if i < N - 1:
        A[i][i + 1] = -lamb

for i in range(len(A)):
    print(A[i])"""

"""
okay that the linear equations is solved. """

"""# Time-stepping loop
for t in range(y_node_count - 1):
    # Build right-hand side vector b using previous time step and boundaries
    b = [U[t][i + 1] for i in range(N)]
    b[0] += lamb * U[t + 1][0]      # left boundary
    b[-1] += lamb * U[t + 1][-1]    # right boundary
    print(b)

    # Deep copy of A to avoid modifying original
    A_copy = [row[:] for row in A]

    # Solve system using your Gaussian elimination function
    u_next = pdpcore.gauss_eliminate(A_copy, b)

    # Store solution in U
    for i in range(N):
        U[t + 1][i + 1] = u_next[i]

# Print final result (formatted)
for i in range(len(U)):
    print(U[i])"""
"""
k = 0.1
rod_length = 1
dx = 0.05
dt = 0.005
time_limit = 1
# adjusting
x_intervals = round(rod_length/dx)
dx = rod_length/x_intervals
x_node_count = x_intervals + 1

t_node_count = int(time_limit/dt) + 1
lamb = (k*dt)/(dx**2)

T = [[100 for i in range(x_node_count)] for j in range(t_node_count)]

# define initial condition
for t in range(t_node_count):
    T[t][0] = 300 #left boundary
    T[t][-1] = 300 #right boundary"""
"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Example 2D matrix (you can replace this with your own)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Get matrix dimensions
rows = len(matrix)
cols = len(matrix[0])

# Create X, Y, Z for surface plot
X = [[j for j in range(cols)] for i in range(rows)]
Y = [[i for j in range(cols)] for i in range(rows)]
Z = matrix  # Z is already the value matrix

# Create the figure and 3D axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
ax.plot_surface(X, Y, Z, cmap='viridis')

# Set axis labels
ax.set_xlabel('X (column index)')
ax.set_ylabel('Y (row index)')
ax.set_zlabel('Z (value)')

plt.show()

"""

NIM = 13123136 # nim > 8 digit
NIM = str(NIM)
I = 1500
L = 200
E = int(NIM[3:8])
M = int(NIM[4:8])


print( E,M)


