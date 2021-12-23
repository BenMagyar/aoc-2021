import copy
import re

def prepare(input):
    directions = []
    for line in input:
        mode = line[0:2] == 'on'
        matches = re.findall(r'[\d\-]+\.\.[\d\-]+', line)
        ranges = [list(map(int, str.split(match, '..'))) for match in matches]
        directions.append([mode] + ranges)
    return directions

def part_one(input):
    cubes = set()
    for set_on, xr, yr, zr in input:
        if any([abs(v) > 50 for v in sum([xr, yr, zr], [])]):
            continue
        for x in range(xr[0], xr[1] + 1):
            for y in range(yr[0], yr[1] + 1):
                for z in range(zr[0], zr[1] + 1):
                    if set_on:
                        cubes.add((x, y, z))
                    elif (x, y, z) in cubes:
                        cubes.remove((x, y, z))
    return (len(cubes))

def range_intersect(range_a, range_b):
    if range_b[0] > range_a[1] or range_a[0] > range_b[1]:
        return None
    
    return (max(range_a[0], range_b[0]), min(range_a[1], range_b[1]))
    

def intersect(a, b):
    _, x_range_a, y_range_a, z_range_a = a
    set_on, x_range_b, y_range_b, z_range_b = b

    x_overlap = range_intersect(x_range_a, x_range_b)
    y_overlap = range_intersect(y_range_a, y_range_b)
    z_overlap = range_intersect(z_range_a, z_range_b)

    if any([overlap is None for overlap in [x_overlap, y_overlap, z_overlap]]):
        return None
    
    return [set_on, x_overlap, y_overlap, z_overlap]

def volume(cuboid):
    _, xr, yr, zr = cuboid
    return (xr[1] - xr[0] + 1) * (yr[1] - yr[0] + 1) * (zr[1] - zr[0] + 1)

def count_cubes(input):
    complete, cubes = [], 0
    for input_cuboid in reversed(input):
        set_on, xr, yr, zr = input_cuboid
        recount = []
        if set_on:
            for cuboid in complete:
                overlap = intersect(input_cuboid, cuboid)
                if overlap is not None:
                    recount_cuboid = overlap
                    recount_cuboid[0] = True
                    recount.append(recount_cuboid) 
            cubes += volume(input_cuboid)
            cubes -= count_cubes(recount)
        complete.append(input_cuboid)
    return cubes
    
def part_two(input):
    return count_cubes(input)

def test(input):
    input = prepare(input)
    assert part_two(input) == 2758514936282235

def answer(input):
    input = prepare(input)
    print(part_one(input))
    print(part_two(input))
