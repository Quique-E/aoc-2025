input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

with open("two_input.txt") as f:
    input = f.readlines()[0]

ids = input.split(",")

# for any given string of length > 1
# find all divisors of its length
# for each divisor, split the string in that number of substrings
# compare substrings and if they are all the same, return true
# make sure to stop function execution as soon as one true case is found

def get_divisors(x):
    for i in range(1, int(x / 2) + 1):
        if x % i == 0:
            yield i
    yield x

def check(x):
    val = str(x)
    length = len(str(x))

    divisors = get_divisors(length)

    for divisor in divisors:
        # avoiding the last case, where divisor equals length 
        if divisor == length:
            return False
        
        segments_count = int(length / divisor)
        segments = list()

        # divide x in segments_count segments
        start_point = 0
        for i in range(0, segments_count):
            segments.append(val[start_point:(divisor + start_point)])
            start_point += divisor
        
        # if all segments are the same we've met the invalid id condition
        if len(set(segments)) == 1:
            return True
    
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