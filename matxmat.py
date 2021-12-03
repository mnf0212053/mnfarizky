def mult_mtx(A, B):
    C = []
    D = []
    for j in range(0, len(B)):
        for i in range(0, len(B[0])):
            C.append(0)
        D.append(C)

    ans = 0

    for i in range(0, len(B)):
        for j in range(0, len(B[0])):
            ans = ans + A[i][j]*B[j][i]
        D[i][j] = ans
        ans = 0

    return D

A = [[2, 2], [2, 2]]
B = [[3, 0], [1, 0]]
print(mult_mtx(A, B))