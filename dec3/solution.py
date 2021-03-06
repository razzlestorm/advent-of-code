from typing import List, Tuple
import math

with open('input.txt') as f:
    input_list = [line.strip() for line in f]

# example line in input_list: '....#...............#.#..###.##'
# Each row is 31 spaces in width, the columns are 323 high.
# print(len(input_list[0])) <- width
# print(len(input_list)) <- height

SLOPE = (3, 1)

def traverse_map(input_list: List, slope: Tuple) -> int:
    count = 0
    width, height = len(input_list[0]), len(input_list)
    x, y = (0, 0)

    while y < height:
        try:
            # % by width because we're repeating, not just reaching a side and staying
            if input_list[y][x % width] == '#':
                count += 1
            x += slope[0]
            y += slope[1]
        except IndexError:
            return count
    return count

a = traverse_map(input_list, (1, 1))
b = traverse_map(input_list, (3, 1))
c = traverse_map(input_list, (5, 1))
d = traverse_map(input_list, (7, 1))
e = traverse_map(input_list, (1, 2))

answer = math.prod([a, b, c, d, e])

print(traverse_map(input_list, (3,1)))
print(answer)
