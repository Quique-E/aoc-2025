input="""..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""


input = input.split("\n")

with open("four_input.txt") as f:
    input = f.read().splitlines()

w = len(input[0])
h = len(input)


"""
for every position [i, j]
adyacent cells are defined as
[i - 1, j - 1]  [i - 1, j]  [i - 1, j + 1]
[i,     j -1]   [i,     j]  [i,     j + 1]
[i + 1, j - 1]  [i + 1, j]  [i + 1, j + 1]
"""

# Return True if <4 adyacents are @
def check_adyacents(i, j):
    paper_count = 0

    for n in range(i - 1, i + 2):
        for m in range(j - 1, j + 2):
            
            # Skip the cell we are checking
            if n == i and m == j:
                continue

            # Skip out of range
            if n < 0 or m < 0 or n >= w or m >= h:
                continue

            #print(f"Adyacent in coordinates {(n, m)} is {input[n][m]}")

            # count paper
            if input[n][m] == "@":
                paper_count += 1

            #print(f"Total paper count so far for this cell is {paper_count}")
            
            # stop if at 4
            if paper_count > 3:
                #print(f"Finished checking due to hitting four papers\n")
                return False
    
    #print("Finished checking, did not find four papers\n")
    return True

# Loop until a new cycle does not yield any new movable rolls
count = 0
found = True

while found:
    movables = list()
    found_this_pass = 0

    for i in range(0, h):
        for j in range(0, w):

            # skip whatever is not a roll of paper
            if input[i][j] == ".":
                continue

            # whenever a cell is a roll of paper, evaluate adyacents
            #print(f"Checking {input[i][j]}, coords {(i, j)}")
            if check_adyacents(i, j):
                movables.append((i, j))
                found_this_pass +=1
    
    #print(f"Found {found_this_pass}")

    # stop loop when you don't find any
    if found_this_pass < 1:
        found = False

    count += found_this_pass

    # first make temp lists
    tmp_input = input
    for row in range(0, h):
        tmp_input[row] = list(input[row])

    # move rolls
    for i in movables:
        tmp_input[i[0]][i[1]] = "."

    # convert back to str
    for i in range(0, h):
        tmp_input[i] = "".join(tmp_input[i])
    
    input = tmp_input

print(count)

