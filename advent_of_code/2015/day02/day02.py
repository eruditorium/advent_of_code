# day02.py

import regex as re


def parse(puzzle_input):
    """Parse input."""
    with open(puzzle_input) as f:
        return [list(map(int, input.split('x'))) for input in f.read().split('\n')]


def part1(input):
    """Solve part 1."""
    area = 0
    for l, w, h in input:
        area += 2 * l * w + 2 * w * h + 2 * h * l + min([l, w, h]) * sorted([l, w, h])[1]
    return area


def part2(input):
    """Solve part 2."""
    length = 0
    for l, w, h in input:
        length += 2 * min([l, w, h]) + 2 * sorted([l, w, h])[1] + l * w * h
    return length


if __name__ == "__main__":
    path = 'input.txt'
    input = parse(path)
    print(input)

    # answer: 1586300
    print('part 1:', part1(input))

    # answer: 3737498
    print('part 2:', part2(input))
