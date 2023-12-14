# day13.py

import time


def parse(puzzle_input):
    """Parse input."""
    with open(puzzle_input) as f:
        return [line.split('\n') for line in f.read().split('\n\n')]


def mirror_axis(puzzle):
    for row in range(1, len(puzzle)):
        above, below = reversed(puzzle[:row]), puzzle[row:]
        # diff = 0
        # for a, b in zip(above, below):
        #     for c1, c2 in zip(a, b):
        #         if c1 != c2: diff += 1
        # if diff == 0: return row
        # shorter
        if all((a == b) for a, b in zip(above, below)): return row

    return 0


def mirror_axis2(puzzle):
    for row in range(1, len(puzzle)):
        above, below = reversed(puzzle[:row]), puzzle[row:]
        diff = 0
        for a, b in zip(above, below):
            for c1, c2 in zip(a, b):
                if c1 != c2: diff += 1
        if diff == 1: return row
        # shorter:
        # if sum((c1 != c2) for a, b in zip(above, below) for c1, c2 in zip(a,b)) == 1: return row

    return 0


def part1(input):
    """Solve part 1."""
    count = 0
    for puzzle in input:
        count += mirror_axis(puzzle) * 100 + mirror_axis(list(zip(*puzzle)))

    return count


def part2(input):
    """Solve part 2."""
    count = 0
    for puzzle in input:
        count += mirror_axis2(puzzle) * 100 + mirror_axis2(list(zip(*puzzle)))

    return count


if __name__ == "__main__":
    path = 'input.txt'
    input = parse(path)
    # print(input)

    time_start = time.perf_counter()

    # answer: 34911
    print('part 1:', part1(input))
    print(f'Solved in {time.perf_counter() - time_start:.5f} Sec.')

    time_start = time.perf_counter()
    # answer: 33183
    print('part 2:', part2(input))
    print(f'Solved in {time.perf_counter() - time_start:.5f} Sec.')
