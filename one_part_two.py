rotations = [
    "L68",
    "L30",
    "R48",
    "L5",
    "R60",
    "L55",
    "L1",
    "L99",
    "R14",
    "L82",
    "R18",
    "R150"
]

with open("one_input.txt") as f:
    rotations = f.readlines() 

pos = 50
zero_passes = 0

for i in rotations:
    sign = -1 if i[0] == "L" else 1
    mov = int(i[1:])
    
    # dist to zero from zero is 100, not 0
    if pos == 0:
        dist_zero = 100
    else:
        dist_zero = pos if sign == -1 else (100 - pos)
    
    print("prev pos: " + str(pos))
    print("movement direction: " + i[0])
    print("distance to zero: " + str(dist_zero))
    print("mov: " + str(mov))

    # zero passes equals 1 if mov is equal or larger than applicable dist to zero + (mov_remainder / 100)

    if mov >= dist_zero:
        zero_passes += 1
        mov_remainder = mov - dist_zero
        print(f"Added one zero pass. Mov remainder is {mov_remainder}")

        zero_passes += mov_remainder // 100
        
        print(f"Added {mov_remainder // 100} from remainder passes")
    
    pos = (pos + (mov * sign)) % 100

    print("new pos: " + str(pos))
    print(f"Total zero passes so far: {zero_passes}")
    print("\n")

print(zero_passes)
