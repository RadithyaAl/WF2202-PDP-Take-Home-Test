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
        # pivots
        if A[i][i] == 0:
            print(f"Zero pivot at row {i}, swapping with last row.")
            if A[-1][i] == 0:
                print("Still zero after swap, system might be singular.")
                return None
            A[i], A[-1] = A[-1], A[i]
            b[i], b[-1] = b[-1], b[i]

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

