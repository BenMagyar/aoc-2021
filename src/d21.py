from copy import deepcopy

BOARD, DICE = range(1, 11), range(1, 101)

def prepare(input):
    return (int(input[0][-1]), int(input[1][-1]))

class Dice():
    def __init__(self, rolls=0):
        self.rolls = rolls
        self.total = 0
    
    def roll(self, times=3):
        values = [DICE[(self.rolls + i) % 100] for i in range(times)]
        self.rolls += times
        self.total += times
        self.rolls = self.rolls % 100
        return values
    
def part_one(input):
    dice = Dice()
    player, positions, scores = 0, [input[0] - 1, input[1] - 1], [0, 0]
    while not any([score >= 1000 for score in scores]):
        positions[player] = (positions[player] + sum(dice.roll())) % 10
        scores[player] += BOARD[positions[player]]
        player = (player + 1) % 2
    return min(scores) * (dice.total)

quantum_cache = {}
def play_quantum(pos1, pos2, score1, score2):
    if (pos1, pos2, score1, score2) in quantum_cache:
        return quantum_cache[(pos1, pos2, score1, score2)]

    if score2 >= 21:
        quantum_cache[(pos1, pos2, score1, score2)] = (0, 1)
        return (0, 1)

    w1, w2 = 0, 0
    for i in range(1,4):
        for j in range(1, 4):
            for k in range(1, 4):
                next_position = sum([pos1, i, j, k]) % 10
                next_score = score1 + BOARD[next_position]
                sub_w2, sub_w1 = play_quantum(pos2, next_position, score2, next_score)
                w1 += sub_w1
                w2 += sub_w2
    quantum_cache[(pos1, pos2, score1, score2)] = (w1, w2)
    return (w1, w2)

def part_two(input):
    w1, w2 = play_quantum(input[0] - 1, input[1] - 1, 0, 0)
    return max([w1, w2])

def test(input):
    input = prepare(input)
    assert part_one(input) == 739785
    assert part_two(input) == 444356092776315

def answer(input):
    input = prepare(input)
    print(part_one(input))
    print(part_two(input))
