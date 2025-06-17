import problem4
import problem4rk4
import matplotlib.pyplot as plt

NIM = 13123031
rk2x, rk2y, rk2z = problem4.RK2_distributor()
rk4x, rk4y, rk4z = problem4rk4.RK4_distributor()

print("rk2x | rk2y | rk2z")
for i in range(len(rk2x)):
    print(f"{rk2x[i]} | {rk2y[i]} | {rk2z[i]}")
print("rk4x | rk4y | rk4z")
for i in range(len(rk4x)):
    print(f"{rk4x[i]} | {rk4y[i]} | {rk4z[i]}")
# Plotting
plt.figure(figsize=(10, 6))
plt.plot(rk2x, rk2y, marker='o', label='RK2', linestyle='--')
plt.plot(rk4x, rk4y, marker='s', label='RK4', linestyle='-')

plt.title(f"Beam Deflection: RK2 vs RK4 (NIM :{NIM})")
plt.xlabel("x (mm)")
plt.ylabel("Deflection y (mm)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()