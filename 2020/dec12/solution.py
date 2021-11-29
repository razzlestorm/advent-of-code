from typing import NamedTuple

class Direction(NamedTuple):
    direction: str
    distance: int


with open('input.txt') as f:
    instructions = [Direction(line[0], int(line[1:])) for line in f.read().split('\n')]

# sol1: 2277
print(instructions)
