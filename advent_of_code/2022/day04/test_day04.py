# source: https://realpython.com/python-advent-of-code/#part-1-solution-using-templates

import pathlib
import os
import pytest
import day04 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    return aoc.parse(os.path.join(PUZZLE_DIR, 'example.txt'))


@pytest.fixture
def example2():
    return aoc.parse(os.path.join(PUZZLE_DIR, 'example.txt'))


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [[2, 4, 6, 8],
                        [2, 3, 4, 5],
                        [5, 7, 7, 9],
                        [2, 8, 3, 7],
                        [6, 6, 4, 6],
                        [2, 6, 4, 8]]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == 2


def test_parse_example2(example1):
    """Test that input is parsed properly."""
    assert example1 == [[2, 4, 6, 8],
                        [2, 3, 4, 5],
                        [5, 7, 7, 9],
                        [2, 8, 3, 7],
                        [6, 6, 4, 6],
                        [2, 6, 4, 8]]


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc.part2(example1) == 4


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc.part2(example2) == 0
