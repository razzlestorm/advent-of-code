from typing import List
from collections import Counter, defaultdict

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

### Didn't get this working
def count_arrangements(adapters: List[int]) -> int:
    # add the outlet to list:
    sorted_adapters = sorted(adapters)
    # add our final device to sorted list
    sorted_adapters.append(sorted_adapters[-1] + 3)
    #breakpoint()
    combinations = defaultdict(int, {0: 1})
    for a in sorted_adapters:
        combinations[a] = combinations[a - 1] + combinations[a - 2] + combinations[a - 3]
    return combinations[sorted_adapters[-1]]


with open('input.txt') as f:
    adapters = [int(line) for line in f.read().split('\n')]


counter = Counter({1: 0, 2: 0, 3: 0})
sol1 = count_differences(adapters, counter)
print(sol1)
print(sol1[1] * sol1[3])

sol2 = count_arrangements(adapters)
print(sol2)

####
xs = adapters
xs.append(0)
xs = sorted(xs)
xs.append(max(xs)+3)
n1 = 0
n3 = 0
for i in range(len(xs)-1):
    d = xs[i+1]-xs[i]
    if d==1:
        n1 += 1
    elif d==3:
        n3 += 1

# dynamic programming
# Blatantly stolen from jonathan paulson
DP = {}
# dp(i) = the number of ways to complete the adapter chain given
#         that you are currently at adapter xs[i]
def dp(i):
    if i==len(xs)-1:
        return 1
    if i in DP:
        return DP[i]
    ans = 0
    for j in range(i+1, len(xs)):
        if xs[j]-xs[i]<=3:
            # one way to get from i to the end is to first step to j
            # the number of paths from i that *start* by stepping to xs[j] is just DP[j]
            # So dp(i) = \sum_{valid j} dp(j)
            ans += dp(j)
    DP[i] = ans
    return ans

print('dpsol1: ', n1*n3)
print('dpsol2: ', dp(0))
