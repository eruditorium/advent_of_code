# https://realpython.com/python-advent-of-code/#part-1-solution-using-templates

def parse(puzzle_input):
    """Parse input."""
    with open(puzzle_input) as f:
        return [sum(int(block) for block in line.split('\n')) for line in f.read().split('\n\n')]

def part1(input):
    """Solve part 1."""
    return max(input)

def part2(input):
    """Solve part 2."""
    return sum(sorted(input, reverse=True)[:3])


if __name__ == "__main__":
    path = 'input.txt'
    numbers = parse(path)
    #print(numbers)

    # answer 66306
    print(part1(numbers))

    # answer 195292
    print(part2(numbers))