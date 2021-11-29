from typing import List, NamedTuple
from collections import defaultdict


def num_gen(input: List[int]):
    pass

with open('input.txt') as f:
    instructions = [int(num) for num in f.read().split(',')]

print(instructions)
