import os
import re
import heapq
import math
from collections import Counter
from operator import itemgetter
from concurrent.futures import ProcessPoolExecutor, as_completed
from tqdm import tqdm

input="""[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""

input = input.split("\n")

#with open("ten_input.txt") as f:
#    input = f.read().splitlines()

machines = list()
for i in input:
    s = re.findall("\\] (.*) \\{", i)
    buttons = s[0].split(" ")
    buttons = [[int(j) for j in i.replace("(", "").replace(")", "").split(",")] for i in buttons]

    j = re.findall("\\{(.*)\\}", i)
    joltages = [int(i) for i in j[0].split(",")]
    
    machines.append({
        "buttons": tuple(buttons),
        "joltages": joltages
    })


# return new_state, button_pushed
# multipush here?
def get_neighbors(pos, buttons):
    for button in buttons:
        new_state = pos[:]
        for item in button:
            new_state[item] += 1
        yield new_state, button

def a_star(start_position, goal, buttons, sorted_counts):
    open_list = [(0, start_position)]
    closed_set = {}
    g_score = {str(start_position): 0}

    while open_list:
        #print(len(open_list))
        _, current = heapq.heappop(open_list)
        #print(f"current: {current}, goal: {goal}")

        if current == goal:
            directions = list()
            while str(current) in closed_set:
                parent, direction = closed_set[str(current)]
                directions.append(direction)
                current = parent
            return directions[::-1]

        for neighbor, direction in get_neighbors(current, buttons):
            # do not add to list if any is higher than goal
            comparison = [a - b for a, b in zip(goal, current)]
            if any(i < 0 for i in comparison):
                continue

            tentative_g = g_score[str(current)] + 1
            if tentative_g < g_score.get(str(neighbor), float('inf')):
                closed_set[str(neighbor)] = (current, direction)
                g_score[str(neighbor)] = tentative_g

                # apply fixed score for the top three in sorted_counts
                if list(sorted_counts.keys())[0] in direction:
                    f_score = max(math.floor((tentative_g + heuristic(neighbor, goal)) / 1000), 1)
                elif list(sorted_counts.keys())[1] in direction:
                    f_score = max(math.floor((tentative_g + heuristic(neighbor, goal)) / 100), 2)
                elif list(sorted_counts.keys())[2] in direction:
                    f_score = max(math.floor((tentative_g + heuristic(neighbor, goal)) / 10), 3)
                else:
                    f_score = tentative_g + heuristic(neighbor, goal)

                heapq.heappush(open_list, (f_score, neighbor))
    return None

# trying to be relatively aggresive in chasing highest values
def heuristic(list1, list2):
    comparison = [a - b for a, b in zip(list2, list1)]
    return math.floor((abs(sum(comparison) / len(comparison)) ** 2) * 100)


def flatten_list(nested_list):
    flat_list = list()
    for row in nested_list:
        flat_list.extend(row)
    return flat_list


def solve_one(machine):
    state = [0] * len(machine["joltages"])
    goal = machine["joltages"]
    flat_list = flatten_list(machine["buttons"])
    counts = dict(Counter(flat_list))
    sorted_counts = {k: v for k, v in sorted(counts.items(), key=itemgetter(1))}
    least_affected = list(sorted_counts.keys())[0]
    res = a_star(state, goal, machine["buttons"], sorted_counts)
    
    return (len(res), state, goal, res)

if __name__ == "__main__":
    fewest_presses_sum = 0
    # max_workers = os.cpu_count()
    with ProcessPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(solve_one, m) for m in machines]
        for fut in tqdm(as_completed(futures), total=len(futures)):
            presses, state, goal, res = fut.result()
            #print(f"The shortest path from {state} to {goal} is {res}")
            fewest_presses_sum += presses
    print(fewest_presses_sum)


