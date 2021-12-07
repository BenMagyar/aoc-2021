def prepare(input):
    return list(map(int, str.split(input[0], ',')))

def part_one(crabs):
    best = -1
    for position in crabs:
        fuel = sum([abs(position - crab) for crab in crabs])
        best = fuel if fuel < best or best == -1 else best
    return best

def part_two(crabs):
    best = -1
    for position in range(min(crabs), max(crabs)):
        fuel = sum([
            int((abs(position - crab) * (abs(position - crab) + 1) / int(2)))
            for crab in crabs
        ])
        best = fuel if fuel < best or best == -1 else best
    return best
    
def test(input):
    input = prepare(input)
    assert part_one(input) == 37
    assert part_two(input) == 168

def answer(input):
    input = prepare(input)
    print(part_one(input))
    print(part_two(input))
