from typing import NamedTuple, List, Tuple, Dict
from collections import defaultdict
import re


class Bag(NamedTuple):
    name: str
    slots: Dict[str, int]

def create_bag(rowtuple: str) -> Bag:
    name = re.sub(r"bags?$", "", rowtuple[0].strip()).strip()
    if rowtuple[2].strip().startswith("no"):
        return Bag(name, {})
    outdict = {re.sub(r"bags?$", "", bag[1:]).strip(): \
               int(bag[0]) for bag in \
               [b.strip() for b in rowtuple[2].replace(".", "").split(",")]}
    return Bag(name, outdict)


def create_map(bags: List[Bag]) -> dict:
    output = defaultdict(list)
    for bag in bags:
        for k in bag.slots:
            output[k].append(bag.name)
    return output

def check_map(bags: List[Bag], name: str) -> List[str]:
    # essentially bfs logic
    map = create_map(bags)
    checked = set()
    names = [name]

    while len(names) > 0:
        to_check = names.pop()
        for bag in map.get(to_check, []):
            if bag not in checked:
                checked.add(bag)
                names.append(bag)
    return list(checked)

# All credit to Joel Grus
# TODO: Refactor everything/come up with own solution.
def num_bags_inside(
    bags: List[Bag],
    color: str
) -> int:
    by_color = {bag.name: bag for bag in bags}

    num_bags = 0
    stack: List[Tuple[str, int]] = [(color, 1)]
    while stack:
        next_color, multiplier = stack.pop()
        bag = by_color[next_color]
        for child, count in bag.slots.items():
            num_bags += multiplier * count
            stack.append((child, count * multiplier))
    return num_bags


with open('input.txt') as f:
    tuple_list = [group.partition("contain") for group in f.read().split('\n')]
    bag_list = [create_bag(bag) for bag in tuple_list]


shiny_gold_list = check_map(bag_list, "shiny gold")
print(shiny_gold_list)
print(len(shiny_gold_list))
print(num_bags_inside(bag_list, "shiny gold"))
