# day14.py

from functools import lru_cache
import copy
from itertools import count


def parse(puzzle_input):
    """Parse input."""
    with open(puzzle_input) as f:
        return [[c for c in line.strip()] for line in f.readlines()]


def move_north(input):
    platform = list(list(c) for c in input)
    for row in range(0, len(platform)):
        for col in range(0, len(platform[0])):
            if platform[row][col] == "O":
                row_new, col_new = row, col
                while row_new > 0:
                    if platform[row_new - 1][col_new] == ".":
                        row_new -= 1
                    else:
                        break
                platform[row_new][col_new], platform[row][col] = platform[row][col], platform[row_new][col_new]

    return tuple(tuple(line) for line in platform)


def move_south(input):
    platform = list(list(c) for c in input)
    for row in range(len(platform) - 1, -1, -1):
        for col in range(0, len(platform[0])):
            if platform[row][col] == "O":
                row_new, col_new = row, col
                while row_new < len(platform) - 1:
                    if platform[row_new + 1][col_new] == ".":
                        row_new += 1
                    else:
                        break
                platform[row_new][col_new], platform[row][col] = platform[row][col], platform[row_new][col_new]

    return tuple(tuple(line) for line in platform)


def move_east(input):
    platform = list(list(c) for c in input)
    for row in range(0, len(platform)):
        for col in range(len(platform[0]) - 1, -1, -1):
            if platform[row][col] == "O":
                row_new, col_new = row, col
                while col_new < len(platform[0]) - 1:
                    if platform[row_new][col_new + 1] == ".":
                        col_new += 1
                    else:
                        break
                platform[row_new][col_new], platform[row][col] = platform[row][col], platform[row_new][col_new]

    return tuple(tuple(line) for line in platform)


def move_west(input):
    platform = list(list(c) for c in input)
    for row in range(0, len(platform)):
        for col in range(0, len(platform[0])):
            if platform[row][col] == "O":
                row_new, col_new = row, col
                while col_new > 0:
                    if platform[row_new][col_new - 1] == ".":
                        col_new -= 1
                    else:
                        break
                platform[row_new][col_new], platform[row][col] = platform[row][col], platform[row_new][col_new]

    return tuple(tuple(line) for line in platform)


def print_map(input):
    for row in input:
        print(row)


def cycle(input):
    input = move_north(input)
    # print('north:')
    # print_map(input)
    input = move_west(input)
    # print('west:')
    # print_map(input)
    input = move_south(input)
    # print('south:')
    # print_map(input)
    input = move_east(input)
    # print('east:')
    # print_map(input)

    return input


def get_load(input):
    count = 0
    for row in range(len(input)):
        for col in range(len(input[0])):
            if input[row][col] == "O":
                count += len(input) - row
    return count


def part1(input):
    """Solve part 1."""
    input = move_north(input)
    return get_load(input)


def part2(input):
    """Solve part 2."""
    seen = []
    start = 0

    for i in range(0, 10000):
        input = cycle(input)
        if input in seen:
            start = seen.index(input)
            break
        seen.append(input)

    result = (1000000000 - i) % (start - i) + i - 1
    return get_load(seen[result])


if __name__ == "__main__":
    path = ('input.txt')
    input = parse(path)
    # print(input)

    # answer:
    print('part 1:', part1(copy.deepcopy(input)))

    # answer:
    print('part 2:', part2(input))
