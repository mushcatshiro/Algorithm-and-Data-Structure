"""
A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.
Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.
"""

import numpy as np
import random as r

def solutionWONumpy(col, row):
    matrix = []
    for i in range(row):
        _row = []
        for j in range(col):
            _row.append(r.randint(0, 15))
        matrix.append(_row)
    print(matrix)

    min_cost = 0

    for row in matrix:
        min_cost += min(row)

    print(min_cost)

# t O(n) or O(n^2) depending on if we care about python buildin func or not

solutionWONumpy(4, 5)


# with numpy
def solutionWNumpy(row, col):
    matrix = np.random.random([row, col])
    matrix = matrix*100
    matrix = matrix.astype(int)
    print(matrix)

    min_cost = 0

    for row in matrix:
        min_cost += min(row)

    print(min_cost)

# solutionWNumpy(4, 5)