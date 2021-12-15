from collections import defaultdict, Counter
from pathlib import Path
from typing import List

FILE_DIR = Path(__file__).parent

class GNode:
    def __init__(self, val, edges=None):
        self.val = val
        self.edges = edges
        if not self.edges:
            self.edges = []
    def __repr__(self):
        return str(self.val)

def create_graph(l: List[str]) -> List[List[GNode]]:
    matrix = []
    diagonals = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for line in l:
        row = []
        for char in line:
            row.append(GNode(int(char)))
        
        matrix.append(row)
    for j in range(len(matrix)):
        for k in range(len(matrix[0])):
            for dj in [-1, 0, 1]:
                for dk in [-1, 0, 1]:
                    if (dj == 0 and dk == 0) or (dj, dk) in diagonals:
                        continue
                    y_cell = j+dj
                    x_cell = k+dk
                    # checking that they aren't out of bounds
                    if (y_cell >= 0 and x_cell >= 0) and (y_cell < len(matrix) and x_cell < len(matrix[0])):
                        if matrix[y_cell][x_cell] not in matrix[j][k].edges:
                            matrix[j][k].edges.append(matrix[y_cell][x_cell])
    return matrix

def upgrade_map(matrix):
    # a few steps: 
    # extend rows to be the original * 5 + increasing vals each time
    # append rows to start at prev_row+1 * 5
    # run over everything and do the rule of 10 -> 1


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


def get_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node
    
    while node != start_node:
        path.append(node)
        node = previous_nodes[node]
 
    # Add the start node manually
    path.append(start_node)
    return shortest_path[target_node]

def solve_one(data: List[str]) -> int:
    prev_nodes, shortest_path = dijkstra(data, data[0][0])
    return get_result(prev_nodes, shortest_path, data[0][0], data[-1][-1])


def solve_two(data: List[str]) -> int:
    pass


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

    test_map = create_graph(test_data)
    print("Test1: ", solve_one(test_map)) 
    print("Test2: ", solve_two(test_map))  

    DATA = (FILE_DIR / "input.txt").read_text().strip()
    data = [x for x in DATA.split("\n")]
    data_map = create_graph(data)

    print("Sol1:", solve_one(data_map)) 
    print("Sol2:", solve_two(data_map)) 
