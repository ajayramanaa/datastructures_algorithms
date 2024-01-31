import numpy as np


def square_matrix(size, *elements):
    return np.array(elements).reshape(size, size)


def comp_diag_sum(arr):
    left_diag_sum = right_diag_sum = 0
    n = len(arr)
    print(n)
    for i in range(n):
        left_diag_sum += arr[i][i]
        right_diag_sum += arr[i][n-1-i]
        print(arr[i][n-1-i])
    return abs(left_diag_sum-right_diag_sum)


result = square_matrix(3, [2, 5, 7, 9, 4, 6, 23, 56, 80])
print(result)

abs_def = comp_diag_sum(result)
print(abs_def)
