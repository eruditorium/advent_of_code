# source https://realpython.com/python-advent-of-code/#part-1-solution-using-templates

SCORE = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
ELVES = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors'}
ME = {'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}
ME_REV = {'Rock': 'X', 'Paper': 'Y', 'Scissors': 'Z'}
WIN = {'Rock': 'Paper', 'Paper': 'Scissors', 'Scissors': 'Rock'}
LOOSE = {'Rock': 'Scissors', 'Paper': 'Rock', 'Scissors': 'Paper'}


def parse(puzzle_input):
    """Parse input."""
    with open(puzzle_input) as f:
        return [line.split() for line in f.readlines()]


def part1(input):
    """Solve part 1."""
    score = 0
    for elv, me in input:
        score += SCORE[ME[me]]
        if ELVES[elv] == ME[me]:
            score += 3
        if WIN[ELVES[elv]] == ME[me]:
            score += 6

    return score


def part2(input):
    """Solve part 2."""
    input_new = []
    for elv, me in input:
        if me == 'X':
            input_new.append([elv, ME_REV[LOOSE[ELVES[elv]]]])
        elif me == 'Y':
            input_new.append([elv, ME_REV[ELVES[elv]]])
        else:
            input_new.append([elv, ME_REV[WIN[ELVES[elv]]]])

    return part1(input_new)


if __name__ == "__main__":
    path = 'input.txt'
    input = parse(path)
    print(input)

    # answer 11603
    print(part1(input))

    # answer 12725
    print(part2(input))
