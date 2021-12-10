from collections import deque, Counter
from dataclasses import dataclass
from pathlib import Path
from typing import List
import re

FILE_DIR = Path(__file__).parent
POINTS = { 
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

POINTS2 = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

LEFTS = ["(", "[", "{", "<"]
RIGHTS = [")", "]", "}", ">"]

PAIRS = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
}



def score_points(index: int, s: str) -> int:
    return POINTS[s[index]]

def find_corrupt(s: str) -> int:
    "returns the points of the index that the corruption occurs in, or False if no corruption found"
    stack = []
    for ii, char in enumerate(s):
        if char in PAIRS.values():
            stack.append(char)
        else:
            try:
                left = stack.pop()
                if PAIRS[char] != left:
                    #corresponding left character is wrong
                    raise ValueError
            # can no longer pop off meaning no corresponding left char
            except ValueError:
                return score_points(ii, s)
    return False

def finish_line(s: str) -> int:
    "returns points for line finished"
    stack = []
    for ii, char in enumerate(s):
        if char in PAIRS.values():
            stack.append(char)
        else:
            # don't have to worry about checking because we know they made it to the end
            left = stack.pop()
    results = []
    
    for char in stack[::-1]:
        for k, v in PAIRS.items():
            if char == v:
                results.append(k)
    points = 0
    for c in results:
        points *= 5
        points += POINTS2[c]
    return points



if __name__ == "__main__":

    test_data = [
        "[({(<(())[]>[[{[]{<()<>>",
        "[(()[<>])]({[<{<<[]>>(",
        "{([(<{}[<>[]}>{[]{[(<()>",
        "(((({<>}<{<{<>}{[]{[]{}",
        "[[<[([]))<([[{}[[()]]]",
       "[{[{({}]{}}([{[{{{}}([]",
        "{<[[]]>}<{[{[{[]{()[[[]",
        "[<(<(<(<{}))><([]([]()",
        "<{([([[(<>()){}]>(<<{{",
        "<{([{{}}[<[[[<>{}]]]>[]]"
    ]

    test_outputs = [x for x in test_data]
    print(sum([find_corrupt(x) for x in test_outputs]))
    print(sum([finish_line(x) for x in test_data if not find_corrupt(x)]))


    DATA = (FILE_DIR / "input.txt").read_text().strip()
    data = [x for x in DATA.split("\n")]
    # sol 1
    print(len(list(filter(lambda x: x!= False, [find_corrupt(x) for x in data]))))
    print(sum([find_corrupt(x) for x in data]))

    # sol 2
    sol2 = [finish_line(x) for x in data if not find_corrupt(x)]
    sol2 = sorted(sol2)
    print(sol2[len(sol2)//2])

