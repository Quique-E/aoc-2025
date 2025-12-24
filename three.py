input = """987654321111111
811111111111119
234234234234278
818181911112111"""

banks = input.split("\n")

with open("three_input.txt") as f:
    banks = f.read().splitlines()

# find max value by finding largest possible two number combination without reordering
# find max individual value, excluding last value, and record earliest index
# delete the whole string up to the position of the max value
# find max individual value remaining

def find_max(bank, exclude_last):

    if exclude_last:
        vals = [int(i) for i in str(bank)[0:-1]]
    else:
        vals = [int(i) for i in str(bank)[0:]]

    vals = sorted(vals, reverse=True)

    max_val = vals[0]
    max_val_index = bank.index(str(max_val))

    return (max_val, max_val_index)

total = 0

for bank in banks:
    (first_num, first_num_index) = find_max(bank, True)

    new_bank = bank[first_num_index + 1:]

    (second_num, _) = find_max(new_bank, False)

    max_val = int(str(first_num) + str(second_num))

    total += max_val

print(total)

        