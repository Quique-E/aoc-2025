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
        # avoid checking against itself and also doing [a][b] and [b][a] rectangles
        if i >= j:
            continue

        key = str(i) + str(j)
        w = abs(i[0] - j[0]) + 1
        h = abs(i[1] - j[1]) + 1
        res = w * h

        if res > 0:
            matrix[key] = res

sorted_matrix = {k: v for k, v in sorted(matrix.items(), reverse=True, key=itemgetter(1))}

for i in sorted_matrix:
    print(sorted_matrix[i])
    break