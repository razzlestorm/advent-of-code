from collections import Counter, defaultdict
import copy
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path
from typing import List, NamedTuple
from statistics import median, stdev

FILE_DIR = Path(__file__).parent


# some sort of math with the mode and the median?
# 



if __name__ == "__main__":
    test_data = [16,1,2,0,4,2,7,1,2,14]
    mode = Counter(test_data).most_common(1)[0][0]
    sol = sum([abs(ii-mode) for ii in test_data])
    print(sol)
    print(mode)
    print(min(test_data))
    print(median(test_data))
    print(max(test_data))
    print(stdev(test_data))
    DATA = (FILE_DIR / "input.txt").read_text().strip()
    data = [int(x) for x in DATA.split(',')]
    print(len(data))
    mode = Counter(data).most_common(5)
    print(mode)
    print(min(data))
    m = median(data)
    print(max(data))
    print(stdev(data))
    print(sum([abs(ii-m) for ii in data]))
    # test working
