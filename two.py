input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

with open("two_input.txt") as f:
    input = f.readlines()[0]

ids = input.split(",")

def check(x):
    val = str(x)

    # If the length is an odd number there is no way for the id to be invalid
    if len(val) % 2 != 0:
        return False
    
    midpoint = int(len(val) / 2)
    part1 = val[0:midpoint]
    part2 = val[midpoint:]

    if part1 == part2:
        print(f"Invalid ID found: {val}")
        return True
    else:
        return False


invalid_sum = 0

for i in ids:
    vals = i.split("-")
    start, end = int(vals[0]), int(vals[1]) + 1    

    for j in range(start, end):
        result = check(j)

        if result:
            invalid_sum += int(j)

print(invalid_sum)