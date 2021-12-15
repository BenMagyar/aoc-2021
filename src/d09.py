def prepare(input):
    return [[int(char) for char in row] for row in input]

def at(input, x, y):
    try:
        return input[y][x] if x >= 0 and y >= 0 else 10
    except IndexError:
        return 10

def neighbors(x, y, parent):
    return [
        (x + 1, y, parent),
        (x - 1, y, parent),
        (x, y + 1, parent),
        (x, y - 1, parent)
    ]

def is_low(input, x, y):
    value = at(input, x, y)
    return all([
        value < at(input, j, k)
        for j, k, _ in neighbors(x, y, value)
    ])
    
def part_one(input):
    return sum([
        input[y][x] + 1
        for y in range(0, len(input))
        for x in range(0, len(input[0]))
        if is_low(input, x, y)
    ])

def part_two(input):
    lows = ([
        (x, y)
        for y in range(0, len(input))
        for x in range(0, len(input[0]))
        if is_low(input, x, y)
    ])
    
    basins, visited = [], {}
    for x, y in lows:
        visited[(x, y)] = 1
        basin = 1
        queue = neighbors(x, y, at(input, x, y))
        while (len(queue) > 0):
            j, k, parent = queue.pop()
            value = at(input, j, k)
            if value < 9 and value > parent and (j, k) not in visited:
                visited[(j, k)] = 1
                basin += 1
                queue.extend([
                    (a, b, c)
                    for a, b, c in neighbors(j, k, value)
                    if (a, b) not in visited
                ])
        basins.append(basin)
    basins.sort(reverse=True)
    return basins[2] * basins[1] * basins[0]
            
    
def test(input):
    input = prepare(input)
    assert part_one(input) == 15
    assert part_two(input) == 1134

def answer(input):
    input = prepare(input)
    print(part_one(input))
    print(part_two(input))  
