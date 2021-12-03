def prepare(input):
    rows = list(map(lambda l: list(map(int, list(l))), input))
    columns = [list(column) for column in zip(*rows)]
    return (rows, columns)

def bits_as_int(bits):
    return int(''.join(map(str, bits)), 2)

def bits_mode(elements, fallback=1):
    midpoint = len(elements) / 2
    actual = sum(elements)
    
    if (actual == midpoint):
        return fallback

    return 1 if actual > midpoint else 0
    
def gamma_and_epsilon(input):
    _, columns = input
    gamma, epsilon = [], []
    for column in columns:
        gamma_bit = bits_mode(column)
        gamma.append(gamma_bit)
        epsilon.append(int(not gamma_bit))
    return bits_as_int(gamma) * bits_as_int(epsilon)

def search(rows, find_criteria, pos=0):
    if len(rows) == 1:
        return bits_as_int(rows[0])

    columns = [list(column) for column in zip(*rows)]
    required = find_criteria(columns[pos])
    filtered = list(filter(lambda r: r[pos] == required, rows))

    return search(filtered, find_criteria, pos + 1)

def life_support_rating(input):
    rows, _ = input
    oxygen = search(rows, bits_mode)
    co2 = search(rows, lambda c: int(not bits_mode(c)))
    return oxygen * co2
    
def test(input):
    input = prepare(input)
    assert gamma_and_epsilon(input) == 198
    assert life_support_rating(input) == 230

def answer(input):
    input = prepare(input)
    print(gamma_and_epsilon(input))
    print(life_support_rating(input))
