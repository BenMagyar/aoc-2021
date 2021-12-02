def prepare(lines):
    return list(map(lambda l: int(l), lines))

def count_increases(depths):
    count = 0
    for i in range(1, len(depths)):
        count += (depths[i] > depths[i-1])
    return count

def count_window_increases(depths):
    window = lambda i: sum(depths[i-1:i+2])
    count = 0
    for i in range(2, len(depths) - 1):
        count += (window(i) > window(i-1))
    return count

def test(input):
    input = prepare(input)
    assert count_increases(input) == 7
    assert count_window_increases(input) == 5

def answer(input):
    input = prepare(input)
    print(count_increases(input))
    print(count_window_increases(input))
