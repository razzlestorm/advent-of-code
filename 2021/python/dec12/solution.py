from pathlib import Path
from collections import defaultdict
from typing import List

FILE_DIR = Path(__file__).parent


def create_map(l: List[str]) -> dict:
    neighbors = defaultdict(list) 
    for line in l:
        a, b = line.strip().split('-')
        neighbors[a] += [b]
        neighbors[b] += [a]
    return neighbors

DATA = (FILE_DIR / "input.txt").read_text().strip()
data = [x for x in DATA.split("\n")]
neighbors = create_map(data)

def count(part: int, seen=[], cave='start'):
    if cave == 'end': 
        return 1
    if cave in seen:
        if cave == 'start': 
            return 0
        if cave.islower():
            if part == 1: 
                return 0
            else: 
                part = 1

    return sum(count(part, seen+[cave], n)
                for n in neighbors[cave])


if __name__ == "__main__":
    # blatantly stolen from https://www.reddit.com/r/adventofcode/comments/rehj2r/comment/ho7x83o/?utm_source=share&utm_medium=web2x&context=3

    print(count(part=1))
    print(count(part=2))