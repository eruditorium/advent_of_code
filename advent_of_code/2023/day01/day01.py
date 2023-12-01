# day04.py

import regex as re


def parse(puzzle_input):
    """Parse input."""
    with open(puzzle_input) as f:
        return [list(map(str, re.findall('\d', line))) for line in f.readlines()]


def parse2(puzzle_input):
    """Parse input 2."""

    # tipp from reddit with overlapped = True
    with open(puzzle_input) as f:
        with open(puzzle_input) as f:
            return [list(map(str, re.findall('\d|one|two|three|four|five|six|seven|eight|nine', line, overlapped=True)))
                    for line in
                    f.readlines()]


def part1(input):
    """Solve part 1."""
    sum = 0
    for line in input:
        value = str(line[0] + line[-1])
        sum += int(value)

    return sum


def part2(input):
    """Solve part 2."""
    DIGITS = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
              'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'zero': 0}
    total_sum = 0
    for line in input:
        for key, value in DIGITS.items():
            line = [string.replace(key, str(value)) for string in line]

        value = str(line[0] + line[-1])
        total_sum += int(value)
    return total_sum


def part22(input):
    """Solve part 2."""
    DIGITS = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
              'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    total_sum = 0
    for line in input:
        digits = []
        for i, c in enumerate(line):
            if c.isdigit():
                digits.append(c)
            for key, value in DIGITS.items():
                if line[i:].startswith(key):
                    digits.append(str(value))
        total_sum += int(str(digits[0]) + (digits[-1]))

    return total_sum


if __name__ == "__main__":
    path = 'input.txt'
    input = parse(path)
    input2 = parse2(path)

    # answer:
    print('part 1:', part1(input))

    # answer:
    print('part 2:', part2(input2))
