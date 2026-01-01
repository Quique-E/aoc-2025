import numpy as np
from operator import itemgetter

input = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""

input = input.split("\n")

with open("nine_input.txt") as f:
    input = f.read().splitlines()

input = [[int(j) for j in i.split(",")] for i in input]

matrix = dict()

for i in input:
    for j in input:
        if i == j:
            continue

        key = str(i) + str(j)
        res = np.array(i) - np.array(j) + np.array([1, 1])
        res = res[0] * res[1]

        matrix[key] = res

sorted_matrix = {k: v for k, v in sorted(matrix.items(), reverse=True, key=itemgetter(1))}

for i in sorted_matrix:
    print(sorted_matrix[i])
    break