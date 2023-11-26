# day03.py

def parse(puzzle_input):
    """Parse input."""
    with open(puzzle_input) as f:
        return [line.strip() for line in f.readlines()]


def part1(input):
    """Solve part 1."""
    score = 0
    for line in input:
        a = set(line[:len(line) // 2])
        b = set(line[len(line) // 2:])
        for char in a.intersection(b):
            if char.isupper():
                score += ord(char) - 65 + 27
            else:
                score += ord(char) - 96

    return score


def part2(input):
    """Solve part 2."""
    score = 0
    for a, b, c in zip(*[iter(input)] * 3):
        for char in set(a).intersection(set(b), set(c)):
            if char.isupper():
                score += ord(char) - 65 + 27
            else:
                score += ord(char) - 96

    return score


if __name__ == "__main__":
    path = 'input.txt'
    input = parse(path)

    # answer: 8176
    print('part 1:', part1(input))

    # answer: 2689
    print('part 2:', part2(input))
