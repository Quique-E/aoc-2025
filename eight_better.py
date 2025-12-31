from tqdm import tqdm
from operator import itemgetter

input = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""

input = input.split("\n")

with open("eight_input.txt") as f:
    input = f.read().splitlines()

input = [[int(j) for j in i.split(",")] for i in input]

def compare_lists(list1, list2):
    for val in list1:
        if val in list2:
            return True
    return False

def recursively_consolidate(list_of_lists):
    found = False
    for i in list_of_lists:
        for j in list_of_lists:
            if i == j:
                continue
            if compare_lists(i, j):
                found = True
                # the new list we will add to LoL
                new_list = i + j
                nlt = [tuple(item) for item in new_list]
                slt = set(nlt)
                new_list = [list(item) for item in slt]
                
                # create copy and remove
                new_list_of_lists = list_of_lists.copy()
                new_list_of_lists.remove(i)
                new_list_of_lists.remove(j)

                new_list_of_lists.append(new_list)

    if found == False:
        return list_of_lists
    else:
        return recursively_consolidate(new_list_of_lists)

# create a matrix for faster distance lookup
matrix = dict()
for i in input:
    for j in input:
        if i == j:
            continue
        
        # only store pairs once, in one direction
        i_key = str(j) + str(i)
        if i_key in matrix:
            continue

        key = str(i) + str(j)
        matrix[key] = (((i[0] - j[0])**2) + ((i[1] - j[1])**2) + ((i[2] - j[2])**2)) ** 0.5

sorted_matrix = {k: v for k, v in sorted(matrix.items(), key=itemgetter(1))}

target = 1000
circuits = list()
seen_pairs = set()
connections = 0

pbar = tqdm(total=target)

# go from shortest to longest until we meet target
for d_pair in sorted_matrix:

    if connections >= target:
        break

    shortest_distance = [[int(j.strip()) for j in i.replace("[", "").replace("]", "").split(",")] for i in d_pair.split("][")]

    # append first directly
    if len(circuits) == 0:
        circuits.append([shortest_distance[0], shortest_distance[1]])

    # for the rest, look to see if either side is already there
    else:
        to_add = dict()
        
        # iterate over circuits
        for i, j in enumerate(circuits):

            # if any in the distance pair are found in circuits, store info
            if shortest_distance[0] in j:
                to_add = {
                    "found_loc": shortest_distance[0],
                    "new_loc": shortest_distance[1],
                    "pos_in_circuits": i,
                    "curr_circuit": j
                }
            elif shortest_distance[1] in j:
                to_add = {
                    "found_loc": shortest_distance[1],
                    "new_loc": shortest_distance[0],
                    "pos_in_circuits": i,
                    "curr_circuit": j
                }
        
        # if no matches are found, just append pair to list
        if to_add == dict():
            circuits.append([shortest_distance[0], shortest_distance[1]])

        # expand existing circuit if possible
        else:
            new_circuit = to_add["curr_circuit"]
            if to_add["new_loc"] not in new_circuit:
                new_circuit.append(to_add["new_loc"])
            if to_add["found_loc"] not in new_circuit:
                new_circuit.append(to_add["found_loc"])
            
            circuits.pop(to_add["pos_in_circuits"])
            circuits.insert(0, new_circuit)
            
            # consolidate
            circuits = recursively_consolidate(circuits)

    seen_pairs.add(frozenset((tuple(shortest_distance[0]), tuple(shortest_distance[1]))))

    connections += 1
    pbar.update(1)

pbar.close()

circuits.sort(reverse=True, key=lambda x: len(x))

mult_res = 1
for i in range(0, 3):
    print(f"factor {i} is {len(circuits[i])}")
    mult_res *= len(circuits[i])

print(mult_res)