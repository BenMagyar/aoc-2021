from src.io import read_input
from src.d01 import *

input = prepare(read_input('01'))
print(count_increases(input))
print(count_window_increases(input))
