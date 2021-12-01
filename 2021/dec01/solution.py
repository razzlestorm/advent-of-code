from pathlib import Path
from typing import List

FILE_DIR = Path(__file__).parent

def solve1(input_list: List) -> int:
    incs = 0
    jj = 0
    kk = 1
    while kk < len(input_list):
        if input_list[jj] < input_list[kk]:
            incs += 1
        jj += 1
        kk += 1
    return incs

def solve2(input_list: List) -> int:
    # implement sliding window of 3 nums
    incs = 0
    jj = 0
    kk = 3
    while kk < len(input_list):
        if sum(input_list[jj:kk]) < sum(input_list[jj+1:kk+1]):
            incs += 1
        jj += 1
        kk += 1
    return incs

if __name__ == "__main__":
    DATA = (FILE_DIR / "input.txt").read_text().strip()
    data = [int(x) for x in DATA.split('\n')]
    print(solve1(data))
    print(solve2(data))