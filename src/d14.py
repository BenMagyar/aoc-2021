from copy import deepcopy

def prepare(input):
    template = input.pop(0)
    rules = []
    for line in input:
        pair, inserted = str.split(line, " -> ")
        rules.append((pair, inserted))
    return template, dict(rules)     

def polymerize(input, steps=5):
    template, rules = input

    pair_counts = {}
    for pair in rules:
        pair_counts[pair] = template.count(pair)
    
    for _ in range(steps):
        next = deepcopy(pair_counts)
        for pair, value in pair_counts.items():
            if value > 0:
                middle = rules[pair]
                next[pair] -= value
                next[pair[0] + middle] += value
                next[middle + pair[1]] += value
        pair_counts = next

    counts = {}
    for pair in pair_counts:
        counts[pair[0]] = counts.get(pair[0], 0) + pair_counts[pair]
    counts[template[-1]] += 1

    return max(counts.values()) - min(counts.values())

def test(input):
    input = prepare(input)
    assert polymerize(input, 10) == 1588
    assert polymerize(input, 40) == 2188189693529


def answer(input):
    input = prepare(input)
    print(polymerize(input, 10))
    print(polymerize(input, 40))
