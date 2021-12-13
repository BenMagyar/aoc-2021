def prepare(input):
    points, folds = [], []
    for line in input:
        if line.startswith('fold'):
            direction, value = str.split(line, '=')
            if direction == 'fold along x':
                folds.append((int(value), None))
            else:
                folds.append((None, int(value)))
        else:
            x, y = str.split(line, ',')
            points.append((int(x), int(y)))
    return (points, folds)

def transpose(point, fold):
    x, y = point
    tx, ty = fold
    dx = max(x - tx, 0) if tx is not None else 0
    dy = max(y - ty, 0) if ty is not None else 0
    return (tx - dx if dx > 0 else x, ty - dy if dy > 0 else y)
    
def part_one(input):
    points, folds = input
    return len(set([transpose(pt, folds[0]) for pt in points]))

def part_two(input):
    points, folds = input
    for fold in folds:
        points = [transpose(pt, fold) for pt in points]
    points = set(points)
    
    max_x = max([x for x, _ in points])
    max_y = max([y for _, y in points])
    
    for cy in range(max_y + 1):
        for cx in range(max_x + 1):
            print('#' if (cx, cy) in points else ' ', end='')
        print('')
    
def test(input):
    input = prepare(input)
    assert part_one(input) == 17

def answer(input):
    input = prepare(input)
    print(part_one(input))
    print(part_two(input))
