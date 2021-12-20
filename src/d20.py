from copy import deepcopy

SQUARE = [
    (-1, -1), (0, -1), (1, -1),
    (-1, 0),  (0, 0),  (1, 0),
    (-1, 1),  (0, 1),  (1, 1)
]

def prepare(input):
    enhancement = input.pop(0)
    lights = set([
        (x, y)
        for y in range(len(input))
        for x in range(len(input[y]))
        if input[y][x] == '#'
    ])
    return (enhancement, lights)
    
def enhance(input, steps=2):
    enhancement, lights = input

    borders = ('.', enhancement[0])
    for step in range(steps):
        output = set()

        min_x = min([ x for x, _ in lights])
        max_x = max([ x for x, _ in lights])
        min_y = min([ y for _, y in lights])
        max_y = max([ y for _, y in lights])

        for y in range(min_y - 1, max_y + 2):
            for x in range(min_x - 1, max_x + 2):
                index = []
                for ox, oy in SQUARE:
                    px, py, pv = (x + ox, y + oy, '0')
                    if (px, py) in lights:
                        pv = '1'
                    elif px < min_x or px > max_x or py < min_y or py > max_y:
                        pv = '1' if borders[step % 2] == '#' else '0'
                    index.append(pv)
                index = int(''.join(index), 2)
                if enhancement[index] == '#':
                    output.add((x, y))
        lights = output
    
    return lights

def pp(lights, min_x, max_x, min_y, max_y, borders, step):
    for y in range(min_y - 5, max_y + 5):
        for x in range(min_x - 5, max_x + 5):
            if (x, y) in lights:
                print('#', end='')
            elif x < min_x or x > max_x or y < min_y or y > max_y:
                print('#' if borders[(step - 1) % 2] == '#' else ' ', end='')
            else:
                print(' ', end='')
        print('')
    
def part_one(input):
    return len(enhance(input))

def part_two(input):
    return len(enhance(input, 50))
    
def test(input):
    input = prepare(input)
    assert part_one(deepcopy(input)) == 35
    assert part_two(deepcopy(input)) == 3351

def answer(input):
    input = prepare(input)
    print(part_one(deepcopy(input)))
    print(part_two(deepcopy(input)))
