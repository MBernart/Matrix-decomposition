"""Lu"""

def doolittle(matrix):
    """
    L * U = matrix
    :param matrix: Matrix to use Doolittle's algorithm on
    :return: (tuple of lists) matrix L and matrix U
    """
    # Matrix L with unknown quantities
    L = [[0 for _ in range(len(matrix))] for _ in range(len(matrix))]
    for i in range(len(matrix)):
        L[i][i] = 1
    # Matrix U with unknown quantities
    U = [[0 for _ in range(len(matrix))] for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            if j >= i:
                utemp = 0  # variable to temporary assign u[i][j] value
                for k in range(len(matrix)):
                    utemp += L[i][k] * U[k][j]
                U[i][j] = matrix[i][j] - utemp
            ltemp = 0  # variable to temporary assign l[i][j] value
            if j > i:
                for k in range(len(matrix)):
                    ltemp += L[j][k] * U[k][i]
                ltemp = matrix[j][i] - ltemp
                if U[i][i] != 0:
                    L[j][i] = (ltemp / U[i][i])
    return L, U