import re
from collections import deque

input="""aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out"""

input = input.split("\n")

with open("eleven_input.txt") as f:
    input = f.read().splitlines()

# create adjacency matrix
def create_adjacency_matrix(input_list):
    n = len(input_list)
    adj = dict()

    for i in input_list:
        r = re.findall("([a-z]{3})", i)
        origin = r[0]
        outputs = r[1:]

        adj[origin] = outputs
    
    return adj

adj = create_adjacency_matrix(input)

# recursively traverse all paths
def find_all_paths(graph, start, goal, path=None):
    if path is None:
        path = [start]
    
    if start == goal:
        return [path]
    
    paths = []
    for neighbor in graph[start]:
        if neighbor not in path:
            paths.extend(find_all_paths(graph, neighbor, goal, path + [neighbor]))
    return paths



paths = find_all_paths(adj, "you", "out")
print(len(paths))
#print(paths)