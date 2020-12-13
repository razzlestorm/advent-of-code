from typing import NamedTuple, List, Tuple
from collections import defaultdict
import functools
import itertools
import math


def get_depart_times(max_time: int, busses: List[int]) -> dict:
    schedules = defaultdict(list)
    for bus in busses:
        time = 0
        while time <= max_time:
            time += bus
            schedules[bus].append(time)
    return schedules

def calculate_next_bus(max_time: int, schedules: dict) -> Tuple:
    min = 500
    min_bus = None
    for k in schedules.keys():
        if schedules[k][-1] - max_time < min:
            min = schedules[k][-1] - max_time
            min_bus = k
    return (min_bus, min)


def create_offsets(base_routes: List[int]) -> List[int]:
    bus_tuple = [(ii, int(bus)) for ii, bus in enumerate(base_routes) if bus != 'x']
    offsets = []
    for time, bus in bus_tuple:
        offsets.append((time % bus, bus))
    return offsets


def lcm(*nums):
    return functools.reduce(lambda n, lcm: lcm * n // math.gcd(lcm, n), nums)

def iterate_lcms(offset_routes):
    #breakpoint()
    busses = offset_routes
    start = 0
    stepp = 1
    found = 0
    while found < len(busses):
        # itertools steps by the lcm of the last found matches
        for t in itertools.count(start, stepp):
            # checking for the number in the routes where t+offset % bus == 0
            matches = [bus for offset, bus in busses if (t + offset) % bus == 0]
            # keeping track of how many we've found, then updating stepp when we find another
            if len(matches) > found:
                start = t
                # Get least common multiple of matches
                stepp = lcm(*matches)
                found = len(matches)
                break
    return start



def calculate_times(offset_routes: List[Tuple]) -> int:
    candidate = 0
    increment = 1
    for time_after, bus in offset_routes:
        while True:
            if candidate % bus == (bus-time_after if time_after > 0 else 0):
                break
            candidate += increment
            increment *= bus
    return candidate

'''
ALTERNATIVE SOLUTION: STUDY
# chinese remainder from https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
from functools import reduce
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1
'''

with open('input.txt') as f:
    ts, busses = f.read().split('\n')
ts = int(ts)
busses = busses.split(',')
available = [int(bus) for bus in busses if bus != 'x']

schedules = get_depart_times(ts, available)

#sol 1
a, b = calculate_next_bus(ts, schedules)
print(a*b)

# sol 2
offsets = create_offsets(busses)
print(iterate_lcms(offsets))
