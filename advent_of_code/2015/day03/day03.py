# day03.py

def parse(puzzle_input):
    """Parse input."""
    with open(puzzle_input) as f:
        return [list(input) for input in f.read().split('\n')]


def part1(input):
    """Solve part 1."""
    location = 0 + 0j
    visited = {location}

    for instruction in input:
        if instruction == '^':
            location += 1j
        elif instruction == 'V':
            location -= 1j
        elif instruction == '>':
            location += 1
        else:
            location -= 1
        visited.add(location)
    return len(visited)


def part2(input):
    """Solve part 2."""
    return 0


if __name__ == "__main__":
    path = 'input.txt'
    input = parse(path)
    print(input)

    # answer: 2592
    print('part 1:', part1(input))

    # answer: 2360
    print('part 2:', part2(input))
