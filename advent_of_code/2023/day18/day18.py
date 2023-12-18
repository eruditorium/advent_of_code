# day18.py

import time


def parse(puzzle_input):
    """Parse input."""
    with open(puzzle_input) as f:
        return [line.strip().split(' ') for line in f]


def part1(input):
    """Solve part 1."""
    position = (0, 0)
    sum_x = 0
    sum_y = 0
    sum_len = 0

    DIR = {"U": (1, 0), "D": (-1, 0), "R": (0, 1), "L": (0, -1)}

    for line in input:
        d, n, _ = line

        cur_len = int(n)
        cur_dir = DIR[d]

        next_position = (position[0] + cur_len * cur_dir[0], position[1] + cur_len * cur_dir[1])

        sum_x += position[0] * next_position[1]
        sum_y += position[1] * next_position[0]
        sum_len += cur_len
        position = next_position

    return (abs(sum_x - sum_y) / 2) + sum_len / 2 + 1


def part2(input):
    """Solve part 2."""
    position = (0, 0)
    sum_x = 0
    sum_y = 0
    sum_len = 0
    DIR = {'3': (1, 0), '1': (-1, 0), '0': (0, 1), '2': (0, -1)}

    for line in input:
        _, _, rgb = line

        cur_len = int(rgb[2:7], 16)
        cur_dir = DIR[rgb[-2]]

        next_position = (position[0] + cur_len * cur_dir[0], position[1] + cur_len * cur_dir[1])

        sum_x += position[0] * next_position[1]
        sum_y += position[1] * next_position[0]
        sum_len += cur_len
        position = next_position

    return (abs(sum_x - sum_y) / 2) + sum_len / 2 + 1


if __name__ == "__main__":
    time_start = time.perf_counter()
    path = 'input.txt'
    input = parse(path)
    # print(input)

    # answer: 67891
    print('part 1:', part1(input))
    print(f'Solved in {time.perf_counter() - time_start:.5f} seconds')

    time_start = time.perf_counter()

    # answer: 94116351948493
    print('part 2:', part2(input))
    print(f'Solved in {time.perf_counter() - time_start:.5f} seconds')
