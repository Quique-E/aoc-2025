input = """3-5
10-14
16-20
12-18
182552303297392-189779897282507
184887351194217-187190465789699

1
5
8
11
17
32"""

with open("five_input.txt") as f:
    input = f.read()

valid_ranges = input.split("\n\n")[0].split("\n")
valid_ranges = sorted([(int(i.split("-")[0]), int(i.split("-")[1])) for i in valid_ranges])

# either identify continuous ranges and get their size
# or get size of smallest to largest then subtract whitespace
# or try to form ever increasing contiguous ranges until you can't

final_ranges = list()

# we are going to check every valid range for presence in a continuous range
while valid_ranges:
    this_range = valid_ranges.pop(0)

    # check this_range to see if the end of it overlaps with any other range
    # if it does:
    #   make new, larger overlapping range
    #   pop the range you just found out of valid_ranges
    #   add the overlapping range to the first position of valid_ranges
    #   restart loop
    # if you go through all and there are no overlaps, add range to final_ranges

    new_range = tuple()

    for i in range(0, len(valid_ranges)):
        
        # handle subsequent ranges strictly smaller than the one we are checking
        if this_range[0] <= valid_ranges[i][0] and this_range[1] >= valid_ranges[i][1]:
            new_range = this_range
            valid_ranges.pop(i)
            # reinsert this range to keep checking
            valid_ranges.insert(0, this_range)
            break

        # if the end of this range is within another range, we have a match
        # the minus one at the end is intended to catch contiguous ranges and consolidate further
        if this_range[1] <= valid_ranges[i][1] and this_range[1] >= (valid_ranges[i][0] - 1):
            new_range = (this_range[0], valid_ranges[i][1])
            valid_ranges.pop(i)
            valid_ranges.insert(0, new_range)
            break
    
    if new_range == tuple():
        final_ranges.append(this_range)


# now get the size of all the final ranges added together
total_ids = 0
for i in final_ranges:
    # adding 1 because inclusive at both ends
    range_size = i[1] - i[0] + 1
    #print(f"Range {i} has a size of {range_size}")
    total_ids += range_size

print(total_ids)
