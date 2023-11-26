# source: https://realpython.com/python-advent-of-code/#part-1-solution-using-templates

import pathlib
import os
import pytest
import day02 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    return aoc.parse(os.path.join(PUZZLE_DIR, 'example.txt'))


@pytest.fixture
def example2():
    return aoc.parse(os.path.join(PUZZLE_DIR, 'example.txt'))


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [['A', 'Y'], ['B', 'X'], ['C', 'Z']]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == 15


def test_parse_example2(example1):
    """Test that input is parsed properly."""
    assert example1 == [['A', 'Y'], ['B', 'X'], ['C', 'Z']]


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc.part2(example1) == 12


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc.part2(example2) == 0
