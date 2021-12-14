"""
from pathlib import Path
from collections import defaultdict
from typing import List

FILE_DIR = Path(__file__).parent

if __name__ == "__main__":

    DATA = (FILE_DIR / "input.txt").read_text().strip()
    lines = [x.strip() for x in DATA.split("\n")]
    divide = lines.index("")
    dots = set(tuple(map(int, line.split(",")))
            for line in lines[: divide])
    print(len(dots))

    for instruction in lines[divide + 1 :]:
        axis, position = instruction.split()[2].split("=")
        position = int(position)
        update = set()
        for x, y in dots:
            if axis == "x" and x > position:
                update.add((2 * position - x, y))
            elif axis == "y" and y > position:
                update.add((x, 2 * position - y))
            else:
                update.add((x, y))
        dots = update

    xmin = min(x for x, y in dots)
    xmax = max(x for x, y in dots)
    ymin = min(y for x, y in dots)
    ymax = max(y for x, y in dots)
    for y in range(ymin, ymax + 1):
        print("".join("#" if (x, y) in dots else "."
                    for x in range(xmin, xmax + 1)))
    print(len(dots))
"""
## Blatantly stolen from: https://www.reddit.com/r/adventofcode/comments/rf7onx/comment/hodsguh/?utm_source=share&utm_medium=web2x&context=3

import sys

L = open(sys.argv[1]).read().splitlines()
P = [tuple(map(int,p.split(','))) for p in L if ',' in p]
F = [('y' in p,int(p[13:])) for p in L[len(P)+1:]]
m = lambda n,Y: min([v+1 for y,v in n if Y^y] or [1e4])

def f(P,F):
    b = lambda n,f: abs((n//f)%2*(f-2)-n%f)
    return set((b(x,m(F,1)),b(y,m(F,0))) for x,y in P)

N=f(P,F)
print("Part 1: {:d}".format(len(f(P,F[:1]))))
print("Part 2: \n{:s}".format('\n'.join(''.join(" #"[(x,y) in N] for x in range(m(F,1))) for y in range(m(F,0)))))