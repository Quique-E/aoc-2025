import re


input = """0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2"""

with open("twelve_input.txt") as f:
    input = f.read()

shapes = re.findall(r"([\#\.]{3}\n[\#\.]{3}\n[\#\.]{3})", input)

shapes_with_areas = [[i, i.count("#")] for i in shapes]

region_strings = re.findall(r"([0-9]{1,2}x[0-9]{1,2}.*)\b", input)

regions = list()
for s in region_strings:
    area = re.findall(r"([0-9]{1,2}x[0-9]{1,2})", s)
    area = area[0].split("x")
    w = int(area[0])
    h = int(area[1])

    targets = s.split(" ")
    targets = [int(i) for i in targets if len(i) < 3]
    
    regions.append({
        "w": w,
        "h": h,
        "targets": targets
    })

"""
get how many regions can fit their targets
you can discard regions that are smaller than the total footprint of their shapes
then recursively fit shapes?
"""

excluded = 0
for region in regions:
    area = region["w"] * region["h"]

    total_shape_area = 0
    for i in range(0, len(region["targets"])):
        target = region["targets"][i]
        shape_area = shapes_with_areas[i][1]

        total_shape_area += shape_area * target 

    #print(area)
    #print(f"total shape area: {total_shape_area}")

    if total_shape_area > area:
        #print(f"region: {region} excluded due to total area")
        excluded += 1

print(f"regions excluded due to total area: {excluded}")
print(f"regions remaining: {len(regions) - excluded}")

