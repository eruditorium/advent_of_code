# source: https://realpython.com/python-advent-of-code/#part-1-solution-using-templates

import pathlib
import os
import pytest
import day01 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    return aoc.parse(os.path.join(PUZZLE_DIR, 'example.txt'))


@pytest.fixture
def example2():
    return aoc.parse2(os.path.join(PUZZLE_DIR, 'example2.txt'))


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [['1', '2'], ['3', '8'], ['1', '2', '3', '4', '5'], ['7']]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == 142


def test_parse_example2(example2):
    """Test that input is parsed properly."""
    assert example2 == [['two', '1', 'nine'],
                        ['eight', 'two', 'three'],
                        ['one', '2', 'three'],
                        ['two', 'one', '3', 'four'],
                        ['4', 'nine', 'eight', 'seven', '2'],
                        ['one', 'eight', '2', '3', '4'],
                        ['7', 'six']]


@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc.part2(example1) == 281


def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc.part2(example2) == 281
