input = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""

input = input.split("\n")

with open("seven_input.txt") as f:
    input = f.read().splitlines()

w = len(input[0])
h = len(input)

"""
find S
keep track of active beams (in a set?)
count every split
move down once per setep and active beam
"""

# start at S
cur = (0, input[0].index("S"))
# store active beams' last position, start with one block below S
active_beams = [(1, cur[1])]

split_count = 0
while active_beams:
    this_beam = active_beams.pop(0)
    next_pos = (this_beam[0] + 1, this_beam[1])

    # handle last row
    if next_pos[0] >= h:
        continue
    # if we find a splitter, create two beams
    elif input[next_pos[0]][next_pos[1]] == "^":
        split_count += 1

        #print(f"Split at {next_pos}")
        
        # add the two new beams as long as not out of index
        if this_beam[1] - 1 >= 0:
            active_beams.append((this_beam[0] + 1, this_beam[1] - 1))
        if this_beam[1] + 1 < w:
            active_beams.append((this_beam[0] + 1, this_beam[1] + 1))
    # else continue downward
    else:
        active_beams.append(next_pos)
    
    # ensure no repeats in active beams while maintaining left to right order
    active_beams = list(set(active_beams))
    active_beams = sorted(active_beams)
    #print(f"Active beams: {active_beams}")

print(split_count)