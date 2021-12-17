import re

def prepare(input):
    matches = re.findall(r'[\d\-]+\.\.[\d\-]+', input[0])
    range = [str.split(match, '..') for match in matches]
    return list(map(int, range[0] + range[1]))

    
def find_velocities(input):
    x_min, x_max, y_min, y_max = input
    highest_y, velocities = 0, set()
    for xi in range(0, x_max + 1):
        for yi in range(y_min, 1000):
            x, y, t, peak = 0, 0, 0, 0
            while x < x_max and y > y_min:
                x += max(xi - t, 0)
                y += yi - t
                peak = max(y, peak)
                t += 1
                if x_min <= x and x <= x_max and y_min <= y and y <= y_max:
                    velocities.add((xi, yi))
                    if highest_y < peak:
                        highest_y = peak
                    break
    return highest_y, len(velocities)

def part_one(input):
    highest_y, _ = find_velocities(input)
    return highest_y

def part_two(input):
    _, count = find_velocities(input)
    return count
    
def test(input):
    input = prepare(input)
    assert part_one(input) == 45
    assert part_two(input) == 112 

def answer(input):
    input = prepare(input)
    print(part_one(input))
    print(part_two(input))
