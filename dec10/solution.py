from typing import List
from collections import Counter

def count_differences(adapters: List, counter: Counter) -> Counter:
    pointer = 0
    # add the outlet to list:
    adapters.append(0)
    sorted_adapters = sorted(adapters)
    # add our final device to sorted list
    sorted_adapters.append(sorted_adapters[-1] + 3)
    while pointer < len(sorted_adapters)-1:
        diff = sorted_adapters[pointer+1] - sorted_adapters[pointer]
        counter[diff] += 1
        pointer += 1
    return counter


with open('input.txt') as f:
    adapters = [int(line) for line in f.read().split('\n')]


counter = Counter({1: 0, 2: 0, 3: 0})
sol1 = count_differences(adapters, counter)
print(sol1)
print(sol1[1] * sol1[3])
