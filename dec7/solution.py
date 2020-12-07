from typing import NamedTuple, List, Tuple, Dict


class Bag(NamedTuple):
    name: str
    slots: Dict[str, int]

def create_bag(rowtuple: str) -> Bag:
    name = rowtuple[0].strip()
    if rowtuple[2].strip().startswith("no"):
        return Bag(name, {})
    outdict = {bag[1:].strip(): int(bag[0]) for bag in [b.strip() for b in rowtuple[2].replace(".", "").split(",")]}
    return Bag(name, outdict)


with open('input.txt') as f:
    tuple_list = [group.partition("contain") for group in f.read().split('\n')]
    bag_list = [create_bag(bag) for bag in tuple_list]

print(bag_list)
