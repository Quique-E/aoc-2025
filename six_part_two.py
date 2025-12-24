import re

input = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """

with open("six_input.txt") as f:
    input = f.read()

input = input.split("\n")

h = len(input)
w = len(input[0])

"""
now we have to go at the character level like so
    [0, -1]
    [1, -1]
    [2, -1]
    [3, -1]
ignoring blanks and only completing an operation when you find an operand
"""

# Loop over columns until you find an operand, then perform a sum, then continue
answer = 0
operand_found = False
factors = list()

for i in reversed(range(0, w)):
    this_factor = ""
    operand = ""
    res = 0
    for j in range(0, h):
        # Add input to the string that makes up this factor
        if j < h - 1 and input[j][i] != " " and input[j][i] != "":
            this_factor += input[j][i]

        # When at the end of a col and found a space, store factor
        elif j == h - 1 and input[j][i] == " " and this_factor != "":
            factors.append(this_factor.strip())
        # Store operand and set toggle to True when found
        elif j == h - 1 and input[j][i] != " ":
            factors.append(this_factor.strip())
            operand = input[j][i]
            operand_found = True
    
    if operand_found == True:
        operand_found = False
        #print(f"Factors are {factors} and the operand is {operand}")
        if operand == "*":
            res = 1
            for n in factors:
                res *= int(n)
        elif operand == "+":
            for n in factors:
                res += int(n)
        factors = list()
    
    #print(res)
    answer += res

print(answer)

