from copy import deepcopy

def prepare(input):
    return [
        [int(octo) for octo in row]
        for row in input
    ]

def pp(input):
    for row in input:
        print("".join(map(str, row)))

def neighbors(input, x, y):
    return [
        (x, y)
        for x, y in [
            (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1),
            (x - 1, y - 1), (x - 1, y + 1), (x + 1, y + 1), (x + 1, y - 1)
        ]
        if x >= 0 and x < len(input[0]) and y >= 0 and y < len(input)
    ]

def flash(input, x, y, flashed):
    if input[y][x] > 9 and (x, y) not in flashed:
        flashed.add((x, y))
        for nx, ny in neighbors(input, x, y):
            input[ny][nx] += 1
            input, flashed =  flash(input, nx, ny, flashed)
    return input, flashed
    
def octo_step(input, steps=100):
    total, finding_sync = 0, steps is False
    for step in range(steps if not finding_sync else 100000):
        flashed = set()
        for x in range(len(input[0])):
            for y in range(len(input)):
                input[y][x] += 1
        for x in range(len(input[0])):
            for y in range(len(input)):
                input, flashed = flash(input, x, y, flashed)
        for x, y in flashed:
            input[y][x] = 0
        total += len(flashed)
        if finding_sync and len(flashed) == len(input) * len(input[0]):
            return step + 1
    return total
    
def test(input):
    input = prepare(input)
    assert octo_step(deepcopy(input)) == 1656
    assert octo_step(input, False) == 195

def answer(input):
    input = prepare(input)
    print(octo_step(deepcopy(input)))
    print(octo_step(input, False))
    
