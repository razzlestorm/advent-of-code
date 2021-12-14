from collections import defaultdict, Counter
from pathlib import Path
from typing import List

FILE_DIR = Path(__file__).parent

def define_rules(strings: List[str]) -> dict:
    return {row.split("->")[0].strip(): row.split("->")[1].strip() for row in strings}


def apply_rule(s1: str, s2: str, rule: str):
    return s1 + rule + s2

def run_step(template: str, rules: dict) -> str:
    output = ""
    ii = 0
    jj = 1
    while jj < len(template) - 1 :
        pair = template[ii] + template[jj]
        output += apply_rule(pair[0], pair[1], rules[pair])[:2]
        ii += 1
        jj += 1
    pair = template[ii] + template[jj]
    output += apply_rule(pair[0], pair[1], rules[pair])
    return output

def solve_one(data: List[str]) -> int:
    template = data[0]
    rules = define_rules(data[1:])
    pairs = defaultdict(int)
    # neat way to iterate over each pair in string
    for i, j in zip(template, template[1:]):
        pairs[i+j] += 1

    chars = defaultdict(int)
    for c in template:
        chars[c] += 1
    
    for _ in range(10):
        for (a, b), c in pairs.copy().items():
            x = rules[a+b]
            # remove count of original pair
            pairs[a+b] -= c
            # increate count of replacement pairs
            pairs[a+x] += c
            pairs[x+b] += c
            # increase count of new character
            chars[x] += c

    return max(chars.values()) - min(chars.values())


def solve_two(data: List[str]) -> int:
    template = data[0]
    rules = define_rules(data[1:])
    pairs = defaultdict(int)
    # neat way to iterate over each pair in string
    for i, j in zip(template, template[1:]):
        pairs[i+j] += 1

    chars = defaultdict(int)
    for c in template:
        chars[c] += 1
    
    for _ in range(40):
        for (a, b), c in pairs.copy().items():
            x = rules[a+b]
            # remove count of original pair
            pairs[a+b] -= c
            # increate count of replacement pairs
            pairs[a+x] += c
            pairs[x+b] += c
            # increase count of new character
            chars[x] += c

    return max(chars.values()) - min(chars.values())

if __name__ == "__main__":

    test_data = [
        "NNCB",
        "CH -> B",
        "HH -> N",
        "CB -> H",
        "NH -> C",
        "HB -> C",
        "HC -> B",
        "HN -> C",
        "NN -> C",
        "BH -> H",
        "NC -> B",
        "NB -> B",
        "BN -> B",
        "BB -> N",
        "BC -> B",
        "CC -> N",
        "CN -> C"
    ]

    print("Test1: ", solve_one(test_data))  # 1588
    print("Test2: ", solve_two(test_data))  # 2188189693529

    DATA = (FILE_DIR / "input.txt").read_text().strip()
    data = [x for x in DATA.split("\n") if x]

    print("Sol1:", solve_one(data))  # 3048
    print("Sol2:", solve_two(data))  # 3288891573057
