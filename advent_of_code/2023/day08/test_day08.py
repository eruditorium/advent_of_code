# source: https://realpython.com/python-advent-of-code/#part-1-solution-using-templates

import pathlib
import os
import pytest
import day06 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    return aoc.parse(os.path.join(PUZZLE_DIR, 'example.txt'))


@pytest.fixture
def example2():
    return aoc.parse2(os.path.join(PUZZLE_DIR, 'example2.txt'))


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [['Card 1', ' 41 48 83 86 17 | 83 86  6 31 17  9 48 53'],
                        ['Card 2', ' 13 32 20 16 61 | 61 30 68 82 17 32 24 19'],
                        ['Card 3', '  1 21 53 59 44 | 69 82 63 72 16 21 14  1'],
                        ['Card 4', ' 41 92 73 84 69 | 59 84 76 51 58  5 54 83'],
                        ['Card 5', ' 87 83 26 28 32 | 88 30 70 12 93 22 82 36'],
                        ['Card 6', ' 31 18 13 56 72 | 74 77 10 23 35 67 36 11']]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == 13


@pytest.mark.skip(reason="Not implemented")
def test_parse_example2(example2):
    """Test that input is parsed properly."""
    assert example2 == [['Card 1', ' 41 48 83 86 17 | 83 86  6 31 17  9 48 53'],
                        ['Card 2', ' 13 32 20 16 61 | 61 30 68 82 17 32 24 19'],
                        ['Card 3', '  1 21 53 59 44 | 69 82 63 72 16 21 14  1'],
                        ['Card 4', ' 41 92 73 84 69 | 59 84 76 51 58  5 54 83'],
                        ['Card 5', ' 87 83 26 28 32 | 88 30 70 12 93 22 82 36'],
                        ['Card 6', ' 31 18 13 56 72 | 74 77 10 23 35 67 36 11']]


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc.part2(example1) == 30


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc.part2(example2) == 0
