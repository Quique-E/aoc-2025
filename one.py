with open("one_input.txt") as f:
    rotations = f.readlines() 

pos = 50
times_at_zero = 0

for i in rotations:
    sign = -1 if i[0] == "L" else 1
    mov = int(i[1:])

    pos = (pos + (mov * sign)) % 100

    if pos == 0:
        times_at_zero += 1

print(times_at_zero)
