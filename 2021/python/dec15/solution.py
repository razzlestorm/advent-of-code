from collections import defaultdict, Counter
import heapq
from pathlib import Path
from typing import List

FILE_DIR = Path(__file__).parent

# Credit to Joel Grus for sol 2 https://www.youtube.com/watch?v=tCrpuMS60TE&list=PLeDtc0GP5IClHtOISluA2UIXY7VK_Yewf&index=14
def reset_val(x: int) -> int:
    while x > 9:
        x -= 9
    return x

def expand_map(matrix):
    nr = len(matrix)
    nc = len(matrix[0])

    new_matrix = [[0 for _ in range(nc * 5)] for _ in range(nr * 5)]

    for i in range(5):
        for j in range(5):
            for r in range(nr):
                for c in range(nc):
                    new_value = reset_val(int(matrix[r][c]) + i + j)
                    new_matrix[r + i * nr][c + j * nc] = new_value
    
    return new_matrix

"""
# Leaving commented so I can compare the two easily
def dijkstra(matrix, start):
    unvisited_nodes = [node for line in matrix for node in line] 
    shortest_path = {}
    previous_nodes = {}
    max_value = 1000
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    shortest_path[start] = 0
    while unvisited_nodes:
        cur_min = None
        for node in unvisited_nodes:
            if not cur_min:
                cur_min = node
            elif shortest_path[node] < shortest_path[cur_min]:
                cur_min = node
        neighbors = cur_min.edges
        for neighbor in neighbors:
            tentative_value = shortest_path[cur_min] + neighbor.val
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                previous_nodes[neighbor] = cur_min
        unvisited_nodes.remove(cur_min)

    return previous_nodes, shortest_path
"""
# Upgraded pathfinding, credit to: https://github.com/Peter200lx/advent-of-code/blob/master/2021/day15.py
def pathfinder(matrix):
    heap = []
    heapq.heappush(heap, (0, (0, 0)))
    coord_cost = {}
    finish = (len(matrix[-1]) - 1, len(matrix) - 1)
    get_func = lambda m, x, y: m[y][x]

    while heap:
        risk_so_far, cur_coord = heapq.heappop(heap)
        if coord_cost.get(cur_coord, 99999999) <= risk_so_far:
            continue
        if cur_coord == finish:
            return risk_so_far
        coord_cost[cur_coord] = risk_so_far
        for dx, dy in ((-1, 0), (0, -1), (0, 1), (1, 0)):
            new_x, new_y = cur_coord[0] + dx, cur_coord[1] + dy
            if 0 <= new_x <= finish[0] and 0 <= new_y <= finish[1]:
                other_risk = risk_so_far + get_func(matrix, new_x, new_y)
                if coord_cost.get((new_x, new_y), 99999999) <= other_risk:
                    continue
                heapq.heappush(heap, (other_risk, (new_x, new_y)))


def solve_one(data: List[str]) -> int:
    return pathfinder(data)


# Do better than dijkstra, just do a bfs or something
def solve_two(data: List[str]) -> int:
    data = expand_map(data)
    return pathfinder(data)



if __name__ == "__main__":

    test_data = [
        "1163751742",
        "1381373672",
        "2136511328",
        "3694931569",
        "7463417111",
        "1319128137",
        "1359912421",
        "3125421639",
        "1293138521",
        "2311944581",
    ]

    print("Test1: ", solve_one([[int(n) for n in line] for line in test_data])) 
    print("Test2: ", solve_two([[int(n) for n in line] for line in test_data]))  

    DATA = (FILE_DIR / "input.txt").read_text().strip()
    data = [x for x in DATA.split("\n")]
    data_map = [[int(n) for n in line] for line in data]

    print("Sol1:", solve_one(data_map))
    print("Sol2:", solve_two(data_map)) 
