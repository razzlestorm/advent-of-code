from collections import Counter, defaultdict
import copy
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path
from typing import List, NamedTuple
from statistics import median, stdev
from math import floor

FILE_DIR = Path(__file__).parent


# some sort of math with the mode and the median?

def find_fuel_cost(crabs: List[int], center: int) -> int:
    total = 0
    for c in crabs:
        fuel_cost = 1
        for ii in range(min(c, int(center)), max(c, int(center))):
            total += fuel_cost
            fuel_cost += 1
    return total

def brute_force(data):
    min_cost = 100000000
    for ii in range(min(data), max(data)+1):
        print(ii)
        cost = find_fuel_cost(data, ii)
        if cost < min_cost:
            min_cost = cost
    return min_cost


if __name__ == "__main__":
    test_data = [16,1,2,0,4,2,7,1,2,14]
    mode = Counter(test_data).most_common(1)[0][0]
    sol = sum([abs(ii-median(test_data)) for ii in test_data])
    sol2 = brute_force(test_data)
    print(sol)
    print(sol2)
    print(mode)
    print(min(test_data))
    print(median(test_data))
    print(max(test_data))
    print(stdev(test_data))
    DATA = (FILE_DIR / "input.txt").read_text().strip()
    data = [int(x) for x in DATA.split(',')]
    print(len(data))
    mode = Counter(data).most_common(5)
    print(mode)
    print(min(data))
    m = median(data)
    print(max(data))
    s = stdev(data)
    print(sum([abs(ii-m) for ii in data]))
    # test working
    print(sum([abs(ii-floor(s)) for ii in data]))
    # not 92676748
    print(brute_force(data))

