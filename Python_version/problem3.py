import pdpcore

# 3 libraries below is necessary for plotting
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

NIM = 13123136 # interchangeable with 13123031
NIM = str(NIM)
up_bound = int(NIM[0:3])
down_bound = int(NIM[5:7])
left_bound = int(NIM[7])
right_bound = int(NIM[3:5])
interior_node = 3
node_counts_width =  interior_node + 2 # 3 interior + 2 boundary values per row and column
data = [[None for i in range(node_counts_width)] for i in range(node_counts_width)]

# apply the boundary values.
for i in range(len(data)):
    data[0][i] = up_bound
    data[-1][i] = down_bound
    data[i][0] = left_bound
    data[i][-1] = right_bound
    
for i in range(len(data)):
    print(data[i])
A = [[0 for i in range(interior_node**2)] for i in range(interior_node**2)]
b = [0 for i in range(interior_node**2)]

for j in range(1, node_counts_width - 1):     # skip boundary rows and column
    for i in range(1, node_counts_width - 1): 
        p = (j - 1) * interior_node + (i - 1) 
        A[p][p] = -4                           

        neighbors = [((j, i+1), 1),   # right
                     ((j, i-1), 1),   # left
                     ((j+1, i), 1),   # down
                     ((j-1, i), 1)]   # up

        for (nj, ni), coeff in neighbors:
            # check interior node
            if 1 <= nj < node_counts_width - 1 and 1 <= ni < node_counts_width - 1: 
                q = (nj - 1) * interior_node + (ni - 1)
                A[p][q] = coeff
            else:
                b[p] -= data[nj][ni]

result = pdpcore.gauss_seidel(A, b, tol=0.01)
index = 0
for j in range(1, node_counts_width - 1):
    for i in range(1, node_counts_width - 1):
        data[j][i] = result[index]
        index += 1
for i in range(len(A)):
    print(A[i])
print(b)
for i in range(len(data)):
    print(data[i])

Z = np.array(data)

# Generate X and Y grid from node indices
x = list(range(len(Z[0])))  # i-direction (columns)
y = list(range(len(Z)))     # j-direction (rows)
X, Y = np.meshgrid(x, y)

# Plotting
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Surface plot
surf = ax.plot_surface(X, Y, Z, cmap='inferno', edgecolor='k')

# Labels
ax.set_xlabel("X Node")
ax.set_ylabel("Y Node")
ax.set_zlabel("Temperature")
ax.set_title(f"Temperature Distribution (NIM : {NIM})")
ax.set_xticks(x)
ax.set_yticks(y)
fig.colorbar(surf, shrink=0.5, aspect=10)
plt.show()