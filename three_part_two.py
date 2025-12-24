input = """987654321111111
811111111111119
234234234234278
818181911112111
1252442221213212222222222222211212142351224112221222212213421221422124234123226223512212112521243121
4332455583353542332343534334236431265333231336234534214333451233424122455344335342354255355244234332
2222232232225222322623262227221122322222322221161224223225422222222221127242222527172322224242322235
2231112222222222432322232222221222231222332222212222241232221224232233232222222221212121222222232122"""

#banks = input.split("\n")

with open("three_input.txt") as f:
    banks = f.read().splitlines()

# find max value by finding largest possible two number combination without reordering
# find max individual value, excluding last value, and record earliest index
# delete the whole string up to the position of the max value
# find max individual value remaining

# how to generalize for 12 digits:
# loop over 12 times
# each time only look at [0:-i] in sequence
# so you only look at the end digit in the last loop

def find_max(bank, exclude_n):

    if exclude_n > 0:
        vals = [int(i) for i in str(bank)[0:-exclude_n]]
    else:
        vals = [int(i) for i in str(bank)[0:]]

    vals = sorted(vals, reverse=True)

    max_val = vals[0]
    max_val_index = bank.index(str(max_val))

    return (max_val, max_val_index)

total = 0

for bank in banks:

    # top 12 digits starting with -12 ending with all
    tmp_bank = bank
    max_val_string = ""

    for i in reversed(range(0, 12)):
        
        (curr_num, curr_num_index) = find_max(tmp_bank, i)
        
        max_val_string += str(curr_num)

        tmp_bank = tmp_bank[curr_num_index + 1:]
    
    total += int(max_val_string)
    

print(total)

        