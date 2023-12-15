# day15.py
from collections import defaultdict
from functools import lru_cache
import copy
from itertools import count


def parse(puzzle_input):
    """Parse input."""
    with open(puzzle_input) as f:
        return [line for line in f.read().split(',')]


def hex_ascii(line):
    v = 0
    for c in line:
        v = ((v + ord(c)) * 17) % 256

    return v


def part1(input):
    """Solve part 1."""
    return [sum(hex_ascii(line) for line in input)]


def part2(input):
    """Solve part 2."""
    boxes = [{} for _ in range(256)]
    for line in input:
        if '-' in line:
            box = line[:-1]
            box_hash = hex_ascii(line[:-1])
            boxes[box_hash].pop(box, -1)
        else:
            box, lens = line.split('=')
            box_hash = hex_ascii(box)
            boxes[box_hash][box] = int(lens)

    result = 0
    for box_no, box in enumerate(boxes):
        for slot, lens in enumerate(box):
            result += (1 + box_no) * (slot + 1) * box[lens]

    return result


if __name__ == "__main__":
    path = ('input.txt')
    input = parse(path)
    print(input)

    # answer:
    print('part 1:', part1(input))

    # answer:
    print('part 2:', part2(input))
