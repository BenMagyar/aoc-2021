RESET_AGE, NEW_AGE = 6, 8

def prepare(input):
    fish, pop = list(map(int, str.split(input[0], ','))), {}
    for lf in fish:
        pop[lf] = pop.get(lf, 0) + 1
    return (fish, pop)
    
def count_fish(input, days):
    _, pop = input
    for _ in range(days):        
        next = {}
        for day in pop:
            if day == 0:
                next[RESET_AGE] = next.get(RESET_AGE, 0) + pop[day]
                next[NEW_AGE] = next.get(NEW_AGE, 0) + pop[day]
            else:
                next[day-1] = next.get(day-1, 0) + pop[day]
        pop = next
    return sum(pop.values())
    
    
def test(input):
    input = prepare(input)
    assert count_fish(input, 80) == 5934

def answer(input):
    input = prepare(input)
    print(count_fish(input, 80))
    print(count_fish(input, 256))
