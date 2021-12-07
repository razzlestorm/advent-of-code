from collections import Counter, defaultdict
import copy
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path
from typing import List, NamedTuple
from statistics import median, mean
from math import floor

FILE_DIR = Path(__file__).parent


# some sort of math with the mode and the median?
"""
The median works for part 1 because of the optimality property: it is the value with the lowest absolute distance to the data.

Unfortunately, this does not work for part 2, because the "distances" (measured in fuel consumption) are no longer linear: if you double the distance, you need more than double the fuel.

In fact, the distances are the triangle numbers, which are defined by n × (n+1) / 2. Because of the n2 in there, we know that the arithmetic mean has the lowest total distance to the data.
"""

def find_fuel_cost(crabs: List[int], center: int) -> int:
    totals = []
    for c in crabs:
        # gaussian way added to original solution
        fuel_cost = abs(c - center)
        fuel_cost = fuel_cost*(fuel_cost+1)/2
        totals.append(fuel_cost)
    return totals

def brute_force(data):
    fuel_costs = [sum(find_fuel_cost(data, ii)) for ii in range(min(data), max(data)+1)]
    return min(fuel_costs)

def gauss_sum(n: int) -> int:
    n = n*(n+1)/2
    return n

if __name__ == "__main__":
    test_data = [16,1,2,0,4,2,7,1,2,14]
    center = int(median(test_data))
    test_sol = sum([abs(x - center) for x in test_data])
    mean_num = floor(mean(test_data))
    test_sol2 = sum([gauss_sum(abs(x - mean_num)) for x in test_data])
    print(test_sol)
    # note that the gauss_sum method doesn't work for the test data
    print(test_sol2)

    DATA = (FILE_DIR / "input.txt").read_text().strip()
    data = [int(x) for x in DATA.split(',')]



    #optimal sol1
    pos = int(median(data))
    print(sum([abs(x - pos) for x in data]))
    #optimal sol2
    pos = floor(mean(data))       
    print(sum([gauss_sum(abs(x - pos)) for x in data]))


    #improved original solution 2
    print(brute_force(data))