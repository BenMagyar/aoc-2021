from math import floor
from copy import deepcopy

def prepare(input):
    cavern = {}
    for y in range(len(input)):
        for x in range(len(input[0])):
            cavern[(x, y)] = int(input[y][x])
    return (cavern, (len(input[0]) - 1, len(input) - 1))

def neighbors(end, x, y):
    max_x, max_y = end
    return [
        (x, y) for x, y in
        [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        if x >= 0 and x <= max_x and y >= 0 and y <= max_y
    ]

def extra_cost(cost, node, end):
    x, y = node
    max_x, max_y = end
    value = (cost + floor(x / max_x) + floor(y / max_y)) % 9
    return value if value != 0 else 9 
    
def find_path(input):
    cavern, end = input
    queue = set(cavern.keys())
    eligible = set([(0, 0)])

    risk, previous =  {}, {}
    for node in queue:
        risk[node] = float('inf')
    risk[(0, 0)] = cavern[(0, 0)] = 0

    while len(queue) > 0:
        current = None
        for node in eligible:
            if current is None or risk[node] < risk[current]:
                current = node

        queue.remove(current)
        eligible.remove(current)
        
        if current == end:
            return risk[current]
        
        x, y = current
        for neighbor in neighbors(end, x, y):
            if neighbor in queue:
                node_risk = risk[current] + cavern[neighbor]
                if neighbor not in risk or node_risk < risk[neighbor]:
                    eligible.add(neighbor)
                    risk[neighbor] = node_risk
                    previous[neighbor] = current

def part_one(input):
    return find_path(input)

def part_two(input):
    cavern, end = input
    size = end[0] + 1
    original_cavern = list(cavern.keys())
    
    for x_mult in range(5):
        for y_mult in range(5):
            if x_mult == 0 and y_mult == 0:
                continue
            for x, y in original_cavern:
                new_x = x + size * x_mult
                new_y = y + size * y_mult
                value = (cavern[(x, y)] + x_mult + y_mult) % 9
                value = value if value != 0 else 9
                cavern[(new_x, new_y)] = value

    max_x = max([x for x, _ in cavern])
    max_y = max([y for _, y in cavern])

    return find_path((cavern, (max_x, max_y)))
    
def test(input):
    input = prepare(input)
    assert part_one(deepcopy(input)) == 40
    assert part_two(input) == 315

def answer(input):
    input = prepare(input)
    print(part_one(deepcopy(input)))
    print(part_two(input))
