from copy import deepcopy

def c(x, y):
    return f"{x},{y}"

def prepare(input):
    lines, touched = [], {}
    for line in input:
        p1, p2 = str.split(line, "->")
        x1, y1 = str.split(p1, ',')
        x2, y2 = str.split(p2, ',')
        lines.append(list(map(int, [x1, y1, x2, y2])))
    return (lines, touched)
    
def count_overlaps(input, with_diagnols=False):
    lines, touched = deepcopy(input)
    for  x1, y1, x2, y2 in lines:
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                touched[c(x1, y)] = touched.get(c(x1, y), 0) + 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                touched[c(x, y1)] = touched.get(c(x, y1), 0) + 1
        elif with_diagnols:
            x, y = x1, y1
            step_x = int(int(x2 - x1) / int(abs(x2 - x1)))
            step_y = int(int(y2 - y1)  / int(abs(y2 - y1)))
            while (x != x2 + step_x):
                touched[c(x, y)] = touched.get(c(x, y), 0) + 1
                x += step_x
                y += step_y
    return len(list(filter(lambda v: v >= 2, touched.values())))
 
def test(input):
    input = prepare(input)
    assert count_overlaps(input) == 5
    assert count_overlaps(input, True) == 12

def answer(input):
    input = prepare(input)
    print(count_overlaps(input))
    print(count_overlaps(input, True))
