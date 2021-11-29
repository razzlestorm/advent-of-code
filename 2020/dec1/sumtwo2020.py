from typing import List
import itertools
import math

with open('input.txt') as f:
    input_list = [int(line.strip()) for line in f]

def dict_builder_2020(input: List[int]) -> dict:
    '''Builds a dict where k:v = 2020-n:n'''
    num_dict = {}
    for num in input:
        num_dict[2020-num] = num
    return num_dict

num_dict = dict_builder_2020(input_list)

def find_product(input: List) -> int:
    for num in input:
        # If num is present in dict keys, means that there is
        # already another number that adds up with it to 2020.
        if num in num_dict:
            print((num, num_dict[num]))
            return num * num_dict[num]


# This currently doesn't output what I'd expect it to.
def sum_dict_builder(input: List[int]) -> dict:
    '''
    Builds a dict with every number summed with all other numbers,
    where k:v = sum:num
    '''
    sum_dict = {}
    for ii, num in enumerate(input):
        for n in input[ii:]:
            sum_dict[num+n] = n
    return sum_dict

# sum_dict = sum_dict_builder(input_list)

# initial thought is this will be (O)n^2, which is not ideal
# Also note this doesn't return proper value
'''
def find_three_sum_product(input: List[int]) -> int:
    for k, v in sum_dict.items():
        if k+v in num_dict:
            print(k, 'and', v, 'and', num_dict[k+v])
            return k*v*num_dict[k+v]
'''

# BETTER SOLUTION BELOW:
def find_x_sum_product(input: List[int], x: int) -> int:
    possibles = itertools.combinations(input, x)
    for combo in possibles:
        if sum(combo) == 2020:
            print(combo)
            return math.prod(combo)

print(find_product(input_list))
print(find_x_sum_product(input_list, 2))
print(find_x_sum_product(input_list, 3))
