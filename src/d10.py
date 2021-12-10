KEY = { '}': '{', ')': '(', '>': '<', ']': '[' }
PTS = {')': 3, ']': 57, '}': 1197, '>': 25137}
COMPLETE_PTS = { '(': 1, '[': 2, '{': 3, '<': 4 }

def prepare(input):
    return list(map(list, input))
    
def part_one(input):
    points = 0
    for line in input:
        opened = []
        for character in line:
            if character in ['[', '(', '{', '<']:
                opened.append(character)
            else:
                value = opened.pop() if len(opened) > 0 else None
                if value != KEY[character]:
                    points += PTS[character]
    return points

def part_two(input):
    scores = [] 
    for line in input:
        points = 0
        opened, is_valid = [], True
        for character in line:
            if character in ['[', '(', '{', '<']:
                opened.append(character)
            else:
                value = opened.pop() if len(opened) > 0 else None
                if value != KEY[character]:
                    is_valid = False
        if is_valid and len(opened) > 0:
            while len(opened) > 0:
                value = opened.pop()
                points = points * 5 + COMPLETE_PTS[value]
            scores.append(points)
    return sorted(scores)[int(len(scores) / int(2))]
    
def test(input):
    input = prepare(input)
    assert part_one(input) == 26397
    assert part_two(input) == 288957

def answer(input):
    input = prepare(input)
    print(part_one(input))
    print(part_two(input))
