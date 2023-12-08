# day08.py

import math as m


def parse(puzzle_input):
    """Parse input."""
    with open(puzzle_input) as f:
        return [line.strip().split('\n') for line in f.readlines()]


def part1(input):
    """Solve part 1."""
    instructions = str(input.pop(0)).strip('[\']')
    _ = input.pop(0)
    map_dict = dict()
    for item in input:
        key, values_str = str(item).split('=')
        key = key.strip(' [\']() ')
        left, right = values_str.strip(' [\']() ').split(',')
        map_dict[key] = tuple([left.strip(), right.strip()])

    print('part 1: ', find_solution('AAA', 'ZZZ', map_dict, instructions))

    keys_ending_with_A = [key for key in map_dict.keys() if key.endswith('A')]
    steps = []
    for starting in keys_ending_with_A:
        steps.append(find_solution(starting, 'Z', map_dict, instructions))

    print('part 2:', m.lcm(*steps))
    return 0


def find_solution(starting, ending, map_dict, instructions):
    pos = starting
    count = 0

    while not pos.endswith(ending):
        pos = map_dict[pos][0] if instructions[count % len(instructions)] == 'L' else map_dict[pos][1]
        count += 1

    return count


def part2(input):
    """Solve part 2."""
    return 0


if __name__ == "__main__":
    path = 'input.txt'
    input = parse(path)

    # answer:
    print('part 1:', part1(input))

    # answer:
    # print('part 2:', part2(input))
