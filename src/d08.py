COUNT_MAP = { 2: 1, 3: 7, 4: 4, 7: 8, }
INTERSECTIONS = [
    [6, [[6, 1, 1], [9, 4, 4]]],
    [5, [[2, 2, 4], [3, 2, 1], [5, 5, 6]]],
]

def prepare(input):
    lines = []
    split = lambda l: str.split(l.strip(), ' ')
    for line in input:
        lines.append(list(map(split, str.split(line, '|'))))
    return lines    
    
def part_one(input):
    return sum([
        1 if len(digits) in COUNT_MAP else 0
        for _, output in input
        for digits in output
    ])

def part_two(input):
    encoded, total = {}, 0
    for signal, output in input:
        used = []
        for digit in signal:
           if len(digit) in COUNT_MAP:
               encoded[COUNT_MAP[len(digit)]] = list(digit)
               used.append(digit)
        for size, intersections in INTERSECTIONS:
            for intersection in intersections:
                for digit in signal:
                    target, overlap_size, source = intersection
                    if len(digit) == size:
                        overlap = [l for l in encoded[source] if l in digit]
                        if len(overlap) == overlap_size:
                            encoded[target] = list(digit)
                            used.append(digit)
        encoded[0] = list([d for d in signal if d not in used][0])

        digits = []
        for digit in output:
            for key, value in encoded.items():
                if (len(value) == len(digit)):
                    if (len(value) == len([d for d in digit if d in value])):
                        digits.append(str(key))
        total += int("".join(digits))

    return total
    
def test(input):
    input = prepare(input)
    assert part_one(input) == 26
    assert part_two(input) == 61229

def answer(input):
    input = prepare(input)
    print(part_one(input))
    print(part_two(input))
