# day01.py

import regex as re


def parse(puzzle_input):
    """Parse input."""
    with open(puzzle_input) as f:
        return f.read()


def parse2(puzzle_input):
    """Parse input 2."""


def part1(input):
    """Solve part 1."""
    floor = 0
    for letter in input:

        if letter == '(':
            floor += 1
        else:
            floor -= 1

    return floor


def part2(input):
    """Solve part 2."""
    floor = 0
    count = 1
    for letter in input:

        if letter == '(':
            floor += 1
        else:
            floor -= 1

        if floor == -1:
            return count

        count += 1


if __name__ == "__main__":
    path = 'input.txt'
    input = parse(path)
    print(input)
    # answer:
    print('part 1:', part1(input))

    # answer:
    print('part 2:', part2(input))
