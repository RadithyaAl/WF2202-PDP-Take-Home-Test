"""
general equation
(dT/dt) = k(d**T/dx**2)
"""

# koefficient constants
import pdpcore

k = 0.835
rod_length = 10
dx = 2
dt = 0.1
time_limit = 2

# adjusting
x_intervals = round(rod_length/dx)
dx = rod_length/x_intervals
x_node_count = x_intervals + 1

y_node_count = int(time_limit/dt) + 1
lamb = (k*dt)/(dx**2)

U = [[0 for i in range(x_node_count)] for j in range(y_node_count)]

# define initial condition
for t in range(y_node_count):
    U[t][0] = 100 #left boundary
    U[t][-1] = 50 #right boundary

# interior node counts
N = x_node_count - 2 

A = [[0.0 for i in range(N)] for i in range(N)]
for i in range(N):
    A[i][i] = 1 + 2*lamb
    if i > 0:
        A[i][i-1] = -lamb
    if i < N-1:
        A[i][i+1] = -lamb

for i in range(len(A)):
    print(A[i])

#time stepping
for t in range(y_node_count - 1):
    b = [U[t][i+1] for i in range(N)]
    b[0] += lamb * U[t][0]      #left boundary
    b[-1] += lamb * U[t][-1]    #right boundary
    print(b)

    A_copy = [row[:] for row in A]

    u_next = pdpcore.gauss_eliminate(A_copy, b)

    for i in range(N):
        U[t+1][i+1] = u_next[i]

for i in range(len(U)):
    print(U[i])
