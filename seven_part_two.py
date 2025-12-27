import re

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
move row by row down
count the number of beams in each column
add new ones
"""

beams_per_column = {i: 0 for i in range(0, w)}
for i in range(1, h):
    # start is a special case
    if "S" in input[i - 1]:
        beams_per_column[input[i - 1].index("S")] += 1

    if "^" in input[i]:
        splitters = re.finditer("\\^", input[i])

        # if there is a splitter in the column
        for splitter in splitters:
            if beams_per_column[splitter.start()] > 0:
                # add however many beams arrived in each of surrounding columns
                beams_per_column[splitter.start() - 1] += beams_per_column[splitter.start()]
                beams_per_column[splitter.start() + 1] += beams_per_column[splitter.start()]
                # subtract one from the column
                beams_per_column[splitter.start()] = 0

total = 0
for i in beams_per_column:
    total += beams_per_column[i]

print(total)

