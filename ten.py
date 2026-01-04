import re
from collections import deque

input="""[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""

input = input.split("\n")

with open("ten_input.txt") as f:
    input = f.read().splitlines()

machines = list()
for i in input:
    s = re.findall("\\[([\\.\\#]*)\\]", i)
    lights = s[0]

    s = re.findall("\\] (.*) \\{", i)
    buttons = s[0].split(" ")
    buttons = [[int(j) for j in i.replace("(", "").replace(")", "").split(",")] for i in buttons]
    
    machines.append({
        "lights": lights,
        "buttons": tuple(buttons)
    })


# idea: use BFS to search for a "path" from 0 to the target state

# return new_state, button_pushed
def get_neighbors(pos, buttons):
    for button in buttons:
        new_state = pos[:]
        for item in button:
            new_state[item] = 1 if new_state[item] == 0 else 0
        yield new_state, button


def bfs(start_position, goal, buttons):
    queue = deque([(start_position, [])])
    visited = {str(start_position)}

    while queue:
        current, directions = queue.popleft()

        if current == goal:
            return directions

        for neighbor, direction in get_neighbors(current, buttons):
            if str(neighbor) not in visited:
                visited.add(str(neighbor))
                queue.append((neighbor, directions + [direction]))
    
    return None

fewest_presses_sum = 0
for machine in machines:
    # all lights turned off
    state = [0] * len(machine["lights"])
    goal = [0 if i == "." else 1 for i in machine["lights"]]
    
    res = bfs(state, goal, machine["buttons"])
    print(f"The shortest path from {state} to {goal} is {res}")
    fewest_presses_sum += len(res)

print(fewest_presses_sum)
