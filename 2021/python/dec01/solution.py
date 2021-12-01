from dataclasses import dataclass, field
from pathlib import Path
from typing import List

FILE_DIR = Path(__file__).parent


@dataclass
class WindowSolver:
    window_size: int = 1
    data: list[int] = field(default_factory=list)
   
    def count_increments(self) -> int:
        incs = 0
        ii = 0
        jj = self.window_size
        while jj < len(self.data):
            if sum(self.data[ii:jj]) < sum(self.data[ii+1:jj+1]):
                incs += 1
            ii += 1
            jj += 1
        return incs

if __name__ == "__main__":
    DATA = (FILE_DIR / "input.txt").read_text().strip()
    data = [int(x) for x in DATA.split('\n')]
    sol1 = WindowSolver(1, data)
    sol2 = WindowSolver(3, data)
    print(sol1.count_increments())
    print(sol2.count_increments())

    """
    # Added for some fun list comprehension
    def sliding_window_sums(input_list: List[int], window_size: int = 3) -> List[int]:
        return sum([
            (sum(input_list[i - window_size : i])) < (sum(input_list[i - window_size+1 : i+1]))
            for i in range(window_size, len(input_list) + 1)
        ])
    print(sliding_window(data, 1))
    print(sliding_window(data, 3))
    """