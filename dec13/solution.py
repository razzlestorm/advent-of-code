from typing import NamedTuple, List, Tuple
from collections import defaultdict


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

with open('input.txt') as f:
    ts, busses = f.read().split('\n')
ts = int(ts)
busses = busses.split(',')
available = [int(bus) for bus in busses if bus != 'x']


schedules = get_depart_times(ts, available)

#sol 1
a, b = calculate_next_bus(ts, schedules)
print(a*b)
