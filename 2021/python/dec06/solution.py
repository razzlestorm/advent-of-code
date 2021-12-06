from collections import defaultdict
import copy
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path
from typing import List, NamedTuple

FILE_DIR = Path(__file__).parent

@dataclass
class LanternFish:
    timer: int

    def spawn(self):
        if self.timer < 0:
            l = LanternFish(8)
            self.timer = 6
            return l
        return self

def countdown(fish: List[LanternFish], day: int, cache: dict) -> List[LanternFish]:
    if day == 1:
        for f in fish:
            new_f = f.spawn()
            if new_f is not f:
                fish.append(new_f)
            f.timer -= 1
        cache[1] = fish

    if day not in cache:
        new_list = countdown(fish, day-1, cache)
        for f in new_list:
            f.timer -= 1
        for f in new_list:
            new_f = f.spawn()
            if new_f is not f:
                new_list.append(new_f)
        cache[day] = new_list

    return cache[day]

    # we just actually need the counts though, so...
    # https://www.reddit.com/r/adventofcode/comments/r9z49j/comment/hnfaisu/?utm_source=share&utm_medium=web2x&context=3
def countdown2(fish: List[int]) -> int:
    # counts of initial fish timers 0-8
    fish = [fish.count(i) for i in range(9)]
    for _ in range(256):
        # pop the ones who have "counted down" to 0
        num = fish.pop(0)
        # then add that number to the number in the 6th spot 
        fish[6] += num
        # move those fish to the end and continue iterating
        fish.append(num)
    return sum(fish)


if __name__ == "__main__":
    test_data = [3,4,3,1,2]
    test_data = [LanternFish(ii) for ii in test_data]
    DATA = (FILE_DIR / "input.txt").read_text().strip()
    data = [LanternFish(int(x)) for x in DATA.split(',')]
    sol2_data = [int(x) for x in DATA.split(',')]
    # test working
    c = {}
    print(len(countdown(test_data, 80, c)))
    sol = {}
    #sol1
    print(len(countdown(data, 80, sol)))
    #sol2
    print(countdown2(sol2_data))
