CORD_MAP = { 'forward': ('x', 1), 'up': ('y', -1), 'down': ('y', 1) }
    
def prepare(lines):
    directions = []
    for line in lines:
        step, value = str.split(line, ' ')
        axis, direction = CORD_MAP[step]
        directions.append({'x' : 0, 'y': 0, axis: direction * int(value)})
    return directions

def find_distance(directions):
    x, y = 0, 0
    for direction in directions:
        x += direction['x']
        y += direction['y']
    return x * y

def find_distance_with_aim(directions):
    x, y, aim = 0, 0, 0
    for direction in directions:
        aim += direction['y']
        x += direction['x']
        y += direction['x'] * aim
    return x * y

def test(input):
    input = prepare(input)
    assert find_distance(input) == 150
    assert find_distance_with_aim(input) == 900

def answer(input):
    input = prepare(input)
    print(find_distance(input))
    print(find_distance_with_aim(input))
