input = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

with open("five_input.txt") as f:
    input = f.read()

valid_ranges = input.split("\n\n")[0].split("\n")
available_ids = input.split("\n\n")[1].split("\n")

# loop through valid ids
# then through ranges
# when you find id in a range, stop
count = 0
for i in available_ids:
    found = False
    for r in valid_ranges:
        if found == True:
            continue

        range_start = int(r.split("-")[0])
        range_end = int(r.split("-")[1])

        if int(i) >= range_start and int(i) <= range_end:
            #print(f"id {i} is in range {range_start} to {range_end}")
            count += 1
            found = True
            continue

print(count)