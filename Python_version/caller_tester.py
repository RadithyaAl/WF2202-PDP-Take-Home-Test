import pdpcore

b = [[1, 2], [2, 3]]
c = [[3, 2], [5, 7]]

asdf = pdpcore.multiply_matrix(b, c)

print(asdf)



import pdpcore

# Solve:
# 2x + 3y - z = 5
# 4x + y + 2z = 6
# -2x + 5y - 3z = -4

A = [
    [10, -2, -1, -1],
    [-2, 10, -1, -1],
    [-1, -1, 10, -2],
    [-1, -1, -2, 10]
]
b = [3, 15, 27, -9]

solution = pdpcore.gauss_eliminate(A, b)
print("Solution:", solution)
