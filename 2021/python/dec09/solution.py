from collections import deque, Counter
from dataclasses import dataclass
from pathlib import Path
from typing import List
import argparse

FILE_DIR = Path(__file__).parent

@dataclass()
class Coords:
    y: int
    x: int

def check_neighbors(matrix: List[str]) -> tuple:
    """
    Tuple is a List[ints] and a list of coordinates of low_points
    """
    coords = []
    lows = []
    diagonals = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            cell = matrix[y][x]
            neighbors = []
            for yy in [-1, 0, 1]:
                for xx in [-1, 0, 1]:
                    if (yy == 0 and xx == 0) or (yy, xx) in diagonals:
                        continue
                    y_cell = y+yy
                    x_cell = x+xx

                    if (y_cell >= 0 and x_cell >= 0) and (y_cell < len(matrix) and x_cell < len(matrix[y])):
                        neighbors.append(matrix[y + yy][x + xx])
            if all([int(cell) < int(ii) for ii in neighbors]):
                coords.append((y, x))
                lows.append(int(cell))
    return [l+1 for l in lows], coords              

def bfs(matrix: List[str], coords: tuple[int]):
    q = deque()
    visited = set()
    visited.add(coords)
    q.appendleft(coords)
    while q:
        cur_node = q.pop()
        cur_node = Coords(cur_node[0], cur_node[1])

        diagonals = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        for yy in [-1, 0, 1]:
            for xx in [-1, 0, 1]:
                if (yy == 0 and xx == 0) or (yy, xx) in diagonals:
                    continue
                y_cell = cur_node.y+yy
                x_cell = cur_node.x+xx
                if (y_cell >= 0 and x_cell >= 0) and (y_cell < len(matrix) and x_cell < len(matrix[0])):
                    if matrix[cur_node.y + yy][cur_node.x + xx] != "9":
                        if (cur_node.y+yy, cur_node.x+xx) not in visited:
                            visited.add((cur_node.y+yy, cur_node.x+xx))
                            q.appendleft((cur_node.y+yy, cur_node.x+xx))
    return visited

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')

    args = parser.parse_args()

    breakpoint()
    print(args.accumulate(args.integers))

    test_data = [
        "2199943210",
        "3987894921",
        "9856789892",
        "8767896789",
        "9899965678",
    ]

    test_outputs = [x for x in test_data]
    test_lows, test_coords = check_neighbors(test_outputs)
    print(sum(test_lows))
    test_basins = []
    for c in test_coords:
        test_basins.append(bfs(test_data, c))
    test_basins.sort(key=len, reverse=True)
    print(test_basins)



    DATA = (FILE_DIR / "input.txt").read_text().strip()
    data = [x for x in DATA.split("\n")]
    # sol 1
    lows, coords = check_neighbors(data)
    print(coords[0])
    print("Number of coords:", len(coords))
    print(sum(lows))

    # sol 2
    basins = []
    for c in coords:
        basins.append(bfs(data, c))
    basins.sort(key=len, reverse=True)
    print(len(basins[0]) * len(basins[1]) * len(basins[2]))


