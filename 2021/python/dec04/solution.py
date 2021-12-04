from pathlib import Path
from typing import List

FILE_DIR = Path(__file__).parent


def create_boards(boards: List[str]) -> List[str]:
    defined_boards = []
    for board in boards:
        b = board.split('\n')
        d_board = [db.split() for db in b]
        defined_boards.append(d_board)
    return defined_boards


def get_bingo_rankings(boards: List[str], numbers: List[str]):
    # have a pool of bingo numbers we slowly expand and check, return the first board
    # that we encounter with all the numbers on a single column or row. Rank boards in 
    # length of the pool of numbers to see which are first, which are last.
    ranking = {}
    # exhaustive approach, hopefully pays off for pt2?
    for ii, board in enumerate(boards):
        ni = 0
        nj = 5
        # then we search for where the first number is in any boards, and search along
        # rows and columns for the remaining numbers.
        while nj < len(numbers):
            pool = numbers[ni:nj]
            for row in board:
                if set(row).issubset(pool):
                    if ii not in ranking.values():
                        ranking[len(pool)] = ii
                    break
            t_board = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]
            for row in t_board:
                if set(row).issubset(pool):
                    if ii not in ranking.values():
                        ranking[len(pool)] = ii
                    break
            nj += 1
    return ranking

def get_unmarked_nums(checklist, board) -> List:
    nums = []
    for row in board:
        for num in row:
            if num not in checklist: 
                nums.append(num)
    return nums
    


if __name__ == "__main__":
    DATA = (FILE_DIR / "input.txt").read_text().strip()
    data = [x for x in DATA.split('\n\n')]
    numbers = data[0].split(",")
    boards = data[1:]
    d_boards = create_boards(boards)
    ranks = get_bingo_rankings(d_boards, numbers)
    fastest = d_boards[ranks[min(ranks.keys())]]
    slowest = d_boards[ranks[max(ranks.keys())]]
    marked1 = numbers[:min(ranks.keys())]
    marked2 = numbers[:max(ranks.keys())]
    sol_one = sum([int(x) for x in get_unmarked_nums(marked1, fastest)]) * int(marked1[-1]) 
    print(sol_one) #72770
    sol_two = sum([int(x) for x in get_unmarked_nums(marked2, slowest)]) * int(marked2[-1])
    print(sol_two) # 13912