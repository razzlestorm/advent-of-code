# - Zero
# - One
# - Many / More complex
# - Boundary behavior
# - Interface definition
# - Exceptional behavior
# - Simple scenarios

#!/bin/python3
import os
import random
import re
import sys


from typing import List
from math import sqrt
#
# Complete the 'findRestaurants' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY allLocations
#  2. INTEGER numRestaurants
#

def get_distance(x: int, y: int) -> float:
    square = abs((x**2 + y**2))
    return sqrt(square)

def findRestaurants(allLocations: List[list], numRestaurants: int) -> List[tuple]:
    """
    Takes in a list of restaurant coordinates, then outputs the N-closest restaurants, 
    in order of closest -> farthest distance.
    """
    # Distance from customer to location is sqrt(x^2 + y^2)
    # if there are ties, return any locations as long as you're returning N locations
    results = [None] * 
    all_locations_dict = {ii: get_distance(x[0], x[1]) for ii, x in enumerate(allLocations)}
    # sort by closest distance
    sorted_locations = sorted(all_locations_dict.items(), key=lambda x: x[1], reverse=False)
    restaurant_indexes = list(sorted_locations)[:numRestaurants]
    return [allLocations[ii[0]] for ii in restaurant_indexes]



def is_decreasing(days: List[int]) -> bool:
    for ii in range(1, len(days)):
        if days[ii] > days[ii-1]:
            return False
    return True

def is_increasing(days: List[int]) -> bool:
    for ii in range(1, len(days)):
        if days[ii] <= days[ii-1]:
            return False
    return True

def predictDays(day: List[int], k: int) -> List[int]:
    results = []
    N = len(day)
    for ii in range(k, N-k):
        breakpoint()
        if is_decreasing(day[ii-k:ii]) and is_increasing(day[ii+1:ii+k+1]):
            results.append(ii-k+1)
    return results


if __name__ == "__main__":
    test = [[3, 6], [2, 4], [5, 3], [2, 7], [1, 8], [-7, 9]]
    nums = 3
    print(findRestaurants(test, nums))
    print(predictDays([5, 1, 0, 1, 0, 1], 1))

