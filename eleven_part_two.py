import re
from collections import deque

input="""svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out"""

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

# add out as a special case so topo sort doesn't fail and we ensure out is last
adj["out"] = list()

# assume the graph is acyclical
# do a topological sort and then count paths
def topo_sort(graph):
    # kahn's algorithm
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1
    
    queue = deque([node for node, deg in in_degree.items() if deg == 0])
    order = list()

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return order

# given the topo sorted graph, start counting paths backwards
def count_paths_dag(graph, start, goal):
    topo_order = topo_sort(graph)
    
    count = {node: 0 for node in graph}
    count[goal] = 1

    for node in reversed(topo_order):
        for neighbor in graph[node]:
            count[node] += count[neighbor]

    return count[start]

# find paths from svr to out that visit both dac and fft
# i.e. paths
#   from svr to dac to fft to out
#   from svr to fft to dac to out
#   sum the count of both options

path_a = count_paths_dag(adj, "svr", "dac") * count_paths_dag(adj, "dac", "fft") * count_paths_dag(adj, "fft", "out")
print(path_a)

path_b = count_paths_dag(adj, "svr", "fft") * count_paths_dag(adj, "fft", "dac") * count_paths_dag(adj, "dac", "out")
print(path_b)
print(path_a + path_b)