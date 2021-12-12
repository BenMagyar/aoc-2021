def prepare(input):
    adjacency = {}
    for line in input:
        start, end = str.split(line, '-')
        adjacency[start] = adjacency.get(start, []) + [end]
        adjacency[end] = adjacency.get(end, []) + [start]
    return adjacency
    
def find_paths(input, current, current_path, paths, ended, revisit=False):
    if current == 'end':
        ended.add(current_path)
        return (paths, ended)

    for neighbor in input[current]:
        path = current_path + neighbor
        
        is_revisit = neighbor.islower() and neighbor in current_path
        next_revisit = revisit

        if is_revisit \
            and type(revisit) is not bool \
            and neighbor not in ['start', 'end'] \
            and revisit is None:
                next_revisit = neighbor
                is_revisit = False
            
        if (path not in paths and not is_revisit):
            paths.add(path)
            paths, ended = find_paths(input, neighbor, path, paths, ended, next_revisit)

    return (paths, ended)

def part_one(input):
    _, ended = find_paths(input, 'start', ('start'), set(), set())
    return len(ended)

def part_two(input):
    _, ended = find_paths(input, 'start', ('start'), set(), set(), None)
    return len(ended)
    
def test(input):
    input = prepare(input)
    assert part_one(input) == 10
    assert part_two(input) == 36

def answer(input):
    input = prepare(input)
    print(part_one(input))
    print(part_two(input))
