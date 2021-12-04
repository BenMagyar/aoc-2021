BOARD_SIZE = 5

def prepare(input: list[str]):
    draws = list(map(int, input.pop(0).split(',')))
    boards = [
        list(map(lambda l: list(map(int, l.split())), input[i:i+BOARD_SIZE]))
        for i in range(0, len(input), BOARD_SIZE)
    ]
    return (draws, boards)

def is_winner(mask):
    if mask is None:
        return False

    possible = [sum(row) for row in mask]
    possible.extend([sum(col) for col in zip(*mask)])
    return max(possible) == BOARD_SIZE

def play(input, exit_on_win):
    draws, boards = input
    masks = [
        [[0 for i in range(BOARD_SIZE)] for j in range(BOARD_SIZE)]
        for board in boards
    ]
    score = None
    for draw in draws:
        for i in range(len(boards)):
            for j in range(BOARD_SIZE):
                for k in range(BOARD_SIZE):
                    if boards[i][j][k] == draw:
                        if masks[i] is not None:
                            masks[i][j][k] = 1
            if is_winner(masks[i]):
                sum = 0
                for l in range(BOARD_SIZE):
                    for m in range(BOARD_SIZE):
                        if masks[i][l][m] == 0:
                            sum += boards[i][l][m]
                score = sum * draw
                if exit_on_win:
                    return score
                else:
                    masks[i] = None
    return score

def play_part_one(input):
    return play(input, True)

def play_part_two(input):
    return play(input, False)

def test(input):
    input = prepare(input)
    assert play_part_one(input) == 4512
    assert play_part_two(input) == 1924

def answer(input):
    input = prepare(input)
    print(play_part_one(input))
    print(play_part_two(input))
