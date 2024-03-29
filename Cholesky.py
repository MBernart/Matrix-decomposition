"""Cholesky decomposition"""
from math import sqrt
def cholesky(matrix):
    """
    Lt * L = matrix
    :param matrix: matrix to decompose
    :return: (tuple of lists) L, Lt
    """
    # Matrix L with unknown quantities
    L = [[0 for _ in range(len(matrix))] for _ in range(len(matrix))]
    for i in range(len(matrix)):
        L[i][i] = 1
    # Matrix Lt with unknown quantities
    Lt = [[0 for _ in range(len(matrix))] for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if j == i:
                stemp = 0
                for k in range(i):
                    stemp += L[i][k] ** 2
                L[i][i] = sqrt(matrix[i][i] - stemp)
            if j > i:
                stemp = 0
                for k in range(i):
                    stemp += L[j][k] * L[i][k]
                L[j][i] = (matrix[j][i] - stemp) / L[i][i]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            Lt[i][j] = L[j][i]
    return L, Lt
