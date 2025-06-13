"""
Welcome fellaz, this is the place where i put all of the necessary code. for easy acces and reusable code.

to use all of this code, just import pdpcore on yall python code. and then thou can use the function in this module.
"""

def multiply_matrix(A, B):
    if len(A[0]) != len(B):
        print("Invalid matrix dimension")
        return None

    result = [[0 for i in range(len(B[0]))] for j in range(len(A))]

    for i in range(len(A)):             # each row in A
        for j in range(len(B[0])):      # each column in B
            for k in range(len(B)):     # each element in the row of A and column of B
                result[i][j] += A[i][k] * B[k][j]

    return result



def gauss_eliminate(A, b):
    n = len(A)
    # Forward Elimination
    for i in range(n):
        # Find row with the largest absolute pivot in column i
        max_row = max(range(i, n), key=lambda r: abs(A[r][i]))
        
        # Swap current row with max_row
        A[i], A[max_row] = A[max_row], A[i]
        b[i], b[max_row] = b[max_row], b[i]

        # Check for singularity
        if abs(A[i][i]) < 1e-12:
            print("Matrix is singular or nearly singular.")
            return None

        for j in range(i+1, n):
            ratio = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] = A[j][k] - ratio * A[i][k]
            b[j] = b[j] - ratio * b[i]

    # Back Substitution
    x = [0 for i in range(n)]
    for i in range(n-1, -1, -1):
        sum_ax = sum(A[i][j] * x[j] for j in range(i+1, n))
        x[i] = (b[i] - sum_ax) / A[i][i]

    return x


def gauss_seidel(A, b, x_init=None, max_iter=25, tol=1e-6):
    n = len(A)

    if x_init is None:
        x_init = [0.0 for _ in range(n)]

    x = x_init[:] # create the entirely new list copy
    
    for it in range(max_iter):
        x_old = x[:]
        
        for i in range(n):
            sum_ax = 0
            for j in range(n):
                if j != i:
                    sum_ax += A[i][j] * x[j]
            x[i] = (b[i] - sum_ax) / A[i][i]
        
        # Compute the error to check convergence
        error = max(abs(x[i] - x_old[i]) for i in range(n))
        if error < tol:
            print(f"Converged after {it+1} iterations.")
            break
    
    return x


