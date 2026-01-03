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

# now find the largest square with only red and green tiles

# make an adjacency matrix
# traverse from lowest [i][j] corner of largest area to highest [i][j] corner of largest area and back
# if you can make it with all [i][j] inside, continue
# else discard and move to the next one

# build adjacency matrix
def create_adjacency_matrix(coords):
    n = len(coords)
    adj = np.zeros((n, n), dtype=int)

    for i in range(n):
        next_i = (i + 1) % n
        adj[i][next_i] = 1
        adj[next_i][i] = 1
    
    return adj

def traverse_a_to_b(coords, adj, start_idx, end_idx):
    n = len(coords)
    coords = np.array(coords)

    # clockwise
    if start_idx <= end_idx:
        path_indices = list(range(start_idx, end_idx + 1))
    # counterclockwise
    else:
        path_indices = list(range(start_idx, n)) + list(range(0, end_idx + 1))
    
    # get traversed coords
    path_coords = coords[path_indices]

    return path_coords

def path_intersects_interior(path_coords, lower_x, upper_x, lower_y, upper_y):
    for j in range(len(path_coords)):
        # check points strictly inside
        if path_coords[j][0] > lower_x and path_coords[j][0] < upper_x and path_coords[j][1] > lower_y and path_coords[j][1] < upper_y:
            return True
        
        # check edges that pass inside
        # if horizontal, get x of edge and both terminus of edge
        #   if both terminus are within bounds (inclusive) and x of edge within bounds (exclusive), reject
        # if vertical, get y of edge and both terminus of edge
        #   if both terminus are within bounds (inclusive) and y of edge within bounds (exclusive), reject
        if j > 0:
            node_a = path_coords[j - 1]
            node_b = path_coords[j]
            direction = "vertical" if (node_b - node_a)[0] == 0 else "horizontal"

            if direction == "horizontal":
                term1 = np.min([node_a[0], node_b[0]])
                term2 = np.max([node_a[0], node_b[0]])
                y_pos = node_a[1]

                #print(f"Horizontal line with termini at: {term1}, {term2}, at y: {y_pos}")
                if min([term1, term2]) < upper_x and max([term1, term2]) > lower_x and y_pos > lower_y and y_pos < upper_y:
                    #print("Hor rejected due to edge clause ")
                    return True
            else:
                term1 = np.min([node_a[1], node_b[1]])
                term2 = np.max([node_a[1], node_b[1]])
                x_pos = node_a[0]

                if min([term1, term2]) < upper_y and max([term1, term2]) > lower_y and x_pos > lower_x and x_pos < upper_x:
                    #print("Ver rejected due to edge clause")
                    return True
    
    return False   


adj_matrix = create_adjacency_matrix(input)

# starting from largest box, check a to b and b to a
for i in sorted_matrix:
    print(f"Checking square {i} with area {sorted_matrix[i]}")

    # get coords to check
    a, b = [[int(k.strip()) for k in j.replace("[", "").replace("]", "").split(",")] for j in i.split("][")]

    # get the index of these coords in input
    a_idx = input.index(a)
    b_idx = input.index(b)

    # get corner mins and maxs to check traversed road later
    lower_x, lower_y = np.array([a, b]).min(axis=0)
    upper_x, upper_y = np.array([a, b]).max(axis=0)

    # traverse from a to b
    path_coords = traverse_a_to_b(input, adj_matrix, a_idx, b_idx)

    # check a to b path
    rejected = path_intersects_interior(path_coords, lower_x, upper_x, lower_y, upper_y)
    
    if rejected:
            continue

    # traverse from b to a
    path_coords = traverse_a_to_b(input, adj_matrix, b_idx, a_idx)
    
    # check b to a path
    rejected = path_intersects_interior(path_coords, lower_x, upper_x, lower_y, upper_y)
    
    if rejected:
            continue

    break
