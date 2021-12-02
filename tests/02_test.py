from src.io import read_example
from src.d02 import *

input = prepare(read_example('02'))

def test_part_one():
    assert find_distance(input) == 150

def test_part_two():
    assert find_distance_with_aim(input) == 900
