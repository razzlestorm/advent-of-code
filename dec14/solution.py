from typing import List, NamedTuple
from collections import defaultdict


class Address(NamedTuple):
    mem_add: str
    stored: List

    def sum_self(self):
        # This should be working correctly
        return sum(int(x, 2) for x in self.stored)

def apply_mask2(mask: str, instruction: str, *args) -> List:
    # Checking for X, so we know how many strings we will need
    if 'X' in mask:
        output = Address(args[0], [''] * (2**mask.count('X')))
        cutoff = len(output.stored)//2
    else:
        output = Address(args, [''])
    for ii, let in enumerate(mask):
        if let == 'X':
            jj = 0
            kk = 0
            flip = False
            # inserts either '0' or '1' into each string, flipping with F frequency
            # where F = cutoff, then halving cutoff so we should have 2**X unique strings?
            while jj < len(output.stored):
                while kk < cutoff:
                    output.stored[jj] += str(int(flip))
                    kk += 1
                    jj += 1
                kk = 0
                flip = not flip
            cutoff //= 2
        else:
            # otherwise appending the value of the original instruction
            for x in range(len(output.stored)):
                output.stored[x] += instruction[ii]
    return output

def apply_mask(mask: str, instruction: str, *args) -> str:
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
            memory[inst[0].strip()[4:-1]] = mask_applier(mask, value, inst[0].strip()[4:-1])
    return memory

def sum_values(memory: dict) -> int:
    return sum([int(x, 2) for x in memory.values()])

with open('input.txt') as f:
    instructions = [line for line in f.read().split('\n')]

# sol1: answer is: 9628746976360
mem = generate_dict(instructions, apply_mask)
print('sol1: ', sum_values(mem))

#sol2: answer should be: 4_574_598_714_592, currently returning:  488_600_067_258_664
mem2 = generate_dict(instructions, apply_mask2)
print('sol2: ', sum([v.sum_self() for v in mem2.values()]))

'''
import collections
import math
import re
import sys

lines = instructions

def domask(arg, mask):
    arg |= int(mask.replace('X', '0'), 2)
    arg &= int(mask.replace('X', '1'), 2)
    return arg

def allmasks(pos, mask):
    if not mask:
        yield 0
    else:
        # (yes, I probably could have done the ifs *inside* the loop...)
        if mask[-1] == '0':
            for m in allmasks(pos // 2, mask[:-1]):
                yield 2*m + pos % 2
        if mask[-1] == '1':
            for m in allmasks(pos // 2, mask[:-1]):
                yield 2*m + 1
        if mask[-1] == 'X':
            for m in allmasks(pos // 2, mask[:-1]):
                yield 2*m + 0
                yield 2*m + 1


mask = None
mem = collections.defaultdict(int)
for line in lines:
    op, arg = line.split(' = ')
    if op == 'mask':
        mask = arg
    else:
        pos = int(op[4:-1])
        # part 1:
        # mem[pos] = domask(int(arg), mask)
        for m in allmasks(pos, mask):
            mem[m] = int(arg)

print(sum(mem.values()))
'''
