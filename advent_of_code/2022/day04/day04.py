# day04.py

import re


def parse(puzzle_input):
    """Parse input."""
    with open(puzzle_input) as f:
        return [list(map(int, re.findall('\d+', line))) for line in f.readlines()]


def part1(input):
    """Solve part 1."""
    count = 0
    for a, b, c, d in input:
        if (a <= c and b >= d) or (a >= c and b <= d):
            count += 1
    return count


def part2(input):
    """Solve part 2."""
    count = 0
    for a, b, c, d in input:
        section1 = set(range(a, b + 1))
        section2 = set(range(c, d + 1))
        if section1.intersection(section2):
            count += 1
    return count


if __name__ == "__main__":
    path = 'input.txt'
    input = parse(path)

    # answer: 503
    print('part 1:', part1(input))

    # answer: 827
    print('part 2:', part2(input))
