# day11.py

import math as m
import re
import itertools


def parse(puzzle_input):
    """Parse input."""
    with open(puzzle_input) as f:
        return [line.strip() for line in f.readlines()]


def transpose(input):
    """Transpose input"""
    return list(map(''.join, zip(*input)))


def universe_expansion(input):
    """Expanse the universe"""

    new_universe = []
    for row_no, row in enumerate(input):
        new_universe.append(row)
        if '#' in row: continue
        new_universe.append(row)

    universe = transpose(new_universe)
    new_universe = []
    for col_no, col in enumerate(universe):
        new_universe.append(col)
        if '#' in col: continue
        new_universe.append(col)

    return transpose(new_universe)


def empty_rows_and_cols(input):
    """Expanse the universe"""
    empty_rows = []
    empty_columns = []
    for row_no, row in enumerate(input):
        if '#' in row: continue
        empty_rows.append(row_no)

    universe = transpose(input)
    for col_no, col in enumerate(universe):
        if '#' in col: continue
        empty_columns.append(col_no)

    return (set(empty_rows), set(empty_columns))


def search_galaxies(input):
    """Search for Galaxies"""
    galaxies = set()
    for row_no, row in enumerate(input):
        for col_no, col in enumerate(row):
            if col == '#':
                galaxies.add((row_no, col_no))

    return galaxies


def get_distances(galaxies):
    """Calculate distances between all galaxies"""
    distances = []
    for (x, y), (x2, y2) in itertools.combinations(galaxies, 2):
        distances.append(abs(x2 - x) + abs(y2 - y))

    return sum(distances)


def part1(input):
    """Solve part 1."""
    input = universe_expansion(input)
    galaxies = search_galaxies(input)
    distance_sum = get_distances(galaxies)

    return distance_sum


def get_distances_part2(galaxies, empty_rows, empty_columns):
    """Get distance between galaxies for part 2"""
    expand_row = expand_column = 1000000

    distances = []
    galaxies = list(galaxies)
    """ cleaner solution inspired by seligman and kwshi on github"""
    for (x, y), (x2, y2) in itertools.combinations(galaxies, 2):
        x, x2 = min(x, x2), max(x, x2)
        y, y2 = min(y, y2), max(y, y2)

        distance = (x2 - x) + len(empty_rows & set(range(x, x2 + 1))) * (expand_column - 1)
        distance += (y2 - y) + len(empty_columns & set(range(y, y2 + 1))) * (expand_row - 1)
        distances.append(distance)

    return sum(distances)


def part2(input):
    """Solve part 2."""
    galaxies = search_galaxies(input)
    empty_rows, empty_columns = empty_rows_and_cols(input)

    distance_sum = get_distances_part2(galaxies, empty_rows, empty_columns)

    return distance_sum


if __name__ == "__main__":
    path = 'input.txt'
    input = parse(path)
    # print(input)

    # answer: 9418609
    print('part 1:', part1(input))

    # answer: 593821230983
    print('part 2:', part2(input))
