from itertools import combinations
from typing import List


def check_values(nums: List[int]) -> int:
    left = 0
    right = 25
    while right < len(nums):
        window = nums[left:right]
        sums = [sum(pair) for pair in combinations(window, 2)]
        if nums[right] not in sums:
            return nums[right]
        left += 1
        right += 1

def check_values2(nums: List[int], target: int) -> int:
    # two pointers gradually expanding, brute forcing over everything
    for ii in range(len(nums)):
        for jj in range(ii+2, len(nums)):
            rang = nums[ii:jj]
            if sum(rang) == target:
                return min(rang)+max(rang)


with open('input.txt') as f:
    nums = [int(line) for line in f.read().split('\n')]
# sol1: 217430975
print(check_values(nums))

#sol 2: 28509180
print(check_values2(nums, check_values(nums)))
