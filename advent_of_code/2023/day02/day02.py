# day04.py

import regex as re


def parse(puzzle_input):
    """Parse input."""
    with open(puzzle_input) as f:
        return [[game for game in line.split(':')] for line in f.readlines()]


def part1(input):
    """Solve part 1."""
    score = 0
    RED = 12
    GREEN = 13
    BLUE = 14
    for game_id, game in input:
        game_id = int(game_id.replace('Game ', ''))
        possible = True
        for take in game.split(';'):

            red = sum(list(map(int, re.findall(r'(\d+)(?= red)', take))))
            green = sum(list(map(int, re.findall(r'(\d+)(?= green)', take))))
            blue = sum(list(map(int, re.findall(r'(\d+)(?= blue)', take))))

            if red > RED or green > GREEN or blue > BLUE:
                possible = False

        if possible:
            score += game_id

    return score


def part2(input):
    """Solve part 2."""
    power = 0

    for game_id, game in input:
        max_red = max_green = max_blue = 0

        for take in game.split(';'):
            red = sum(list(map(int, re.findall(r'(\d+)(?= red)', take))))
            green = sum(list(map(int, re.findall(r'(\d+)(?= green)', take))))
            blue = sum(list(map(int, re.findall(r'(\d+)(?= blue)', take))))

            max_red = max(max_red, red)
            max_green = max(max_green, green)
            max_blue = max(max_blue, blue)

        power += max_red * max_green * max_blue

    return power


if __name__ == "__main__":
    path = 'input.txt'
    input = parse(path)

    # answer:
    print('part 1:', part1(input))

    # answer:
    print('part 2:', part2(input))
