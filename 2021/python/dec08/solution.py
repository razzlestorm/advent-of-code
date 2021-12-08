from collections import Counter, defaultdict
import copy
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path
from typing import List, NamedTuple
from statistics import median, mean
from math import floor

FILE_DIR = Path(__file__).parent


@dataclass()
class Display:
    segment: list
    output: list

# Mapping of how many unique letters used to make a digit, where k:v = digit: no. of letters
DIGITS = {
    0: 6,
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6
}

def get_outputs(data: List[str]) -> List[str]:
    results = []
    for row in data:
        o = row.split("|")[1]
        out = [x.strip() for x in o.split()]
        results.append(out)
    return results

def create_row_lists(data: List[str]) -> Display:
    results = []
    for row in data:
        r = row.split("|")
        s, o = r
        d = Display([x.strip() for x in s.split()], [x.strip() for x in o.split()])
        results.append(d)
    return results

def is_unique_digit(s: str) -> bool:
    checklist = [DIGITS[1], DIGITS[4], DIGITS[7], DIGITS[8]]
    c = Counter(s)
    if len(c) in checklist:
        return True
    return False

def convert_output(mapping: dict, s: List[str]) -> int:
    """
    uses the mapping to convert the output series of strings to a number
    """
    result = ""
    for output in s:
        d = Counter(output)
        for k, v in mapping.items():
            if d == v:
                result += str(k)
    result = int(result)
    return result

def map_positions(row: Display) -> dict:
    NUMBER_MAP = {0: None, 1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None}
    combined = row.segment + row.output
    for s in combined:
        # find the 1, 4, 7, 8 to get basic mapping of segments
        if len(s) == DIGITS[1]:
            NUMBER_MAP[1] = Counter(s)
        elif len(s) == DIGITS[4]:
            NUMBER_MAP[4] = Counter(s)
        elif len(s) == DIGITS[7]:
            NUMBER_MAP[7] = Counter(s)
        elif len(s) == DIGITS[8]:
            NUMBER_MAP[8] = Counter(s)

    checklist = [DIGITS[1], DIGITS[4], DIGITS[7], DIGITS[8]]
    #then we do another pass and populate the rest of the dict       
    for s in combined:
        if len(s) in checklist:
            continue
        c = Counter(s)
        if len(s) == DIGITS[9]:
            # could be 0, 6, 9
            if len(c - NUMBER_MAP[4]) == 2:
                NUMBER_MAP[9] = c
            elif len((c - NUMBER_MAP[7])) == 3:
                NUMBER_MAP[0] = c
            else:
                NUMBER_MAP[6] = c
        else:
            # 2, 3, 5
            if len((NUMBER_MAP[8] - c) & NUMBER_MAP[1]) == 0:
                NUMBER_MAP[3] = c
            elif len((NUMBER_MAP[8] - NUMBER_MAP[4]) - c) == 0:
                NUMBER_MAP[2] = c
            else:
                NUMBER_MAP[5] = c
    return NUMBER_MAP
            
        

if __name__ == "__main__":
    test_data = [
        "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
        "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
        "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
        "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
        "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
        "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
        "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
        "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
        "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
        "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce",
    ]

    test_outputs = get_outputs(test_data)
    counts = 0
    for l in test_outputs:
        counts += sum([is_unique_digit(s) for s in l])
    print(counts)
    DATA = (FILE_DIR / "input.txt").read_text().strip()
    data = get_outputs([x for x in DATA.split("\n")])
    counts = 0
    for l in data:
        counts += sum([is_unique_digit(s) for s in l])
    #sol1
    print(counts)

    data2 = create_row_lists([x for x in DATA.split("\n")])
    mappings = []
    for d in data2:
        mappings.append(map_positions(d))
    #sol2
    total = sum([convert_output(mappings[ii], data2[ii].output) for ii in range(len(data2))])
    print(total)







