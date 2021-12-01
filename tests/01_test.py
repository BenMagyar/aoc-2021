from os import read
from src.io import read_example
from src.d01 import count_window_increases, prepare, count_increases

example = read_example('01')
input = prepare(example)

def test_part_one():
    assert count_increases(input) == 7

def test_part_two():
    assert count_window_increases(input) == 5
