import re
from pulp import LpProblem, LpMinimize, LpVariable, LpInteger, lpSum, PULP_CBC_CMD

input="""[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""

input = input.split("\n")

with open("ten_input.txt") as f:
    input = f.read().splitlines()

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

# trying out integer linear programming
def solve(targets, buttons):
    prob = LpProblem("MinimButtons", LpMinimize)

    # one var per button with integer and lowbound constraints
    x = [LpVariable(f"x{i}", lowBound=0, cat=LpInteger) for i in range(len(buttons))]

    # minimization objective
    prob += lpSum(x)

    # configure buttons and add to problem
    for target_idx, target_value in enumerate(targets):
        prob += lpSum(x[button_idx] for button_idx, button in enumerate(buttons)
                        if target_idx in button) == target_value
    
    # solve without verbose output
    prob.solve(PULP_CBC_CMD(msg=False))

    if prob.status == 1:
        return [int(v.value()) for v in x]
    else:
        return None


fewest_presses_sum = 0
solutions = list()
for machine in machines:
    # all lights turned off
    state = [0] * len(machine["joltages"])
    goal = machine["joltages"]

    res = solve(machine["joltages"], machine["buttons"])
    solutions.append(res)
    fewest_presses_sum += sum(res)


print(fewest_presses_sum)

