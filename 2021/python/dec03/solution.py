import copy
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, NamedTuple

FILE_DIR = Path(__file__).parent


def get_gamma(text: List[str]) -> List[int]:
    gamma = [0] * len(text[0])
    for line in text:
        for ii, char in enumerate(line):
            if bool(int(char)):
                gamma[ii] += 1
            else:
                gamma[ii] -= 1
    return gamma

def convert_gamma(nums: List[str]) -> int:
    gamma = nums[:]
    ii = 0
    for ii, num in enumerate(nums):
        if num <= 0:
            gamma[ii] = '0'
        else:
            gamma[ii] = '1'
    gamma = "".join(gamma)
    return gamma

def get_board(matrices: List[num]) -> str:

    remaining = copy.deepcopy(matrices)
    ii = 0 
    while len(remaining) > 1:
        most = 0
        for n in remaining:
            if bool(int(n[ii])):
                most += 1
            else:
                most -= 1
        if common:
            if most >= 0:
                most = "1"
            else:
                most = "0"
            remaining = [n for n in remaining if n[ii] == most]
        else:
            if most < 0:
                most = "1"
            else:
                most = "0"
            remaining = [n for n in remaining if n[ii] == most]
        ii += 1
    return remaining[0]


if __name__ == "__main__":
    DATA = (FILE_DIR / "input.txt").read_text().strip()
    data = [x for x in DATA.split('\n\n')]
    breakpoint()