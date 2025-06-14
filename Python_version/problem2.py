import matplotlib.pyplot as plt

k = 0.1
rod_length = 1
dx = 0.05
dt = 0.005
time_limit = 10

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
    T[t][-1] = 300 #right boundary

# interior node counts
N = x_node_count - 2 

for t in range(t_node_count - 1):
    for i in range(N):
        T[t+1][i+1] = T[t][i+1] + lamb*(T[t][i+2] - 2*T[t][i+1] + T[t][i])

# what de helll kok jauh lebih gampang daripada implicit jir
for i in range(len(T)):
    print(T[i]) 

x = [i * dx for i in range(x_node_count)]

# Plot temperature profiles for each time step
for t in range(t_node_count):
    plt.plot(x, T[t], label=f't={round(t * dt, 2)}s')

plt.xlabel('Position')
plt.ylabel('Temperature')
plt.title('Temperature Profile Over Time (FTCS)')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.grid(True)
plt.tight_layout()
plt.show()