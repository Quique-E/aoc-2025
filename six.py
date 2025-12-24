import re

input = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """

with open("six_input.txt") as f:
    input = f.read()

input = input.split("\n")

input = [re.split(r"\s{1,}", i.strip()) for i in input]

h = len(input)
w = len(input[0])

"""
you have to go
    [0, 0]
    [1, 0]
    [2, 0]
    [3, 0] <- operand
"""
answer = 0
for i in range(0, w):
    factors = list()
    operand = ""
    res = 0
    for j in range(0, h):
        
        if j < h - 1:
            factors.append(input[j][i])
        elif j == h - 1:
            operand = input[j][i]
        
    #print(f"Factors are {factors} and the operand is {operand}")
    if operand == "*":
        res = 1
        for n in factors:
            res *= int(n)
    elif operand == "+":
        for n in factors:
            res += int(n)
    
    #print(res)
    answer += res

print(answer)

