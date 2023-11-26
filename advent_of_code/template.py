# template

def parse(puzzle_input):
    """Parse input."""
    with open(puzzle_input) as f:
        return [int(line) for line in f.read().split()]


def part1(input):
    """Solve part 1."""


def part2(input):
    """Solve part 2."""


if __name__ == "__main__":
    path = 'path'
    numbers = parse(path)

    # answer:
    print(part1(numbers))

    # answer:
    print(part2(numbers))
