from typing import List, NamedTuple
from collections import defaultdict


class Address(NamedTuple):
    mem_add: str
    stored: List

    def sum_self(self):
        return sum(int(x, 2) for x in self.stored)

def apply_mask2(mask: str, instruction: str) -> List:
    pass

def apply_mask(mask: str, instruction: str) -> str:
    output = ''
    for ii, let in enumerate(mask):
        if let == 'X':
            output += instruction[ii]
        else:
            output += mask[ii]
    return output

def generate_dict(instructions: List[str], mask_applier) -> dict:
    memory = {}
    for line in instructions:
        if line.startswith('mask'):
            mask = line.split('=')[1].strip()
        if line.startswith('mem'):
            inst = line.split("=")
            value = format(int(inst[1].strip()), '036b')
            memory[inst[0].strip()[4:-1]] = mask_applier(mask, value)
    return memory

def sum_values(memory: dict) -> int:
    return sum([int(x, 2) for x in memory.values()])

def sum_values2(memory: dict) -> int:
    total = 0
    for li in memory.values():
        total += sum([int(x, 2) for x in l])
    return total

# create 36 places for every value of key in mem dict:

# every time mask appears, update the method to translate.

with open('input.txt') as f:
    instructions = [line for line in f.read().split('\n')]

# sol1
mem = generate_dict(instructions, apply_mask)
print(sum_values(mem))

#sol2
#mem2 = generate_dict(instructions, apply_mask2)
