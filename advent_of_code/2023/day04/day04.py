# day04.py

import regex as re
import math as m


def parse(puzzle_input):
    """Parse input."""
    with open(puzzle_input) as f:
        return [[row for row in line.split(':')] for line in f.read().split('\n')]


def part1(input):
    """Solve part 1."""
    count = 0
    for game, card in input:
        set1, set2 = [set(map(int, nums.split())) for nums in card.split('|')]
        common_numbers = set1 & set2
        if len(common_numbers) >= 1:
            count += 2 ** (len(common_numbers) - 1)
    return count


def part2(input):
    """Solve part 2."""
    games = {i: 1 for i in range(1, len(input) + 1)}

    for game, card in input:
        set1, set2 = [set(map(int, nums.split())) for nums in card.split('|')]
        game_no = int(game.split()[1])
        common_numbers = set1 & set2
        if len(common_numbers) >= 0:
            for i in range(game_no + 1, game_no + 1 + len(common_numbers)):
                games[i] += games[game_no]

    return sum(games.values())


if __name__ == "__main__":
    path = 'input.txt'
    input = parse(path)
    print(input)

    # answer: 557705
    print('part 1:', part1(input))

    # answer: 84266818
    print('part 2:', part2(input))
