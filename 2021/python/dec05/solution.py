from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, NamedTuple

FILE_DIR = Path(__file__).parent

class Point(NamedTuple):
    x: int
    y: int

@dataclass
class Vent:
    start: Point
    end: Point

    def is_straight_line(self) -> bool:
        return self.start.x == self.end.x or self.start.y == self.end.y

    def get_straight_range(self) -> List[Point]:
        if self.is_straight_line():
            straight_range = []
            if self.start.x == self.end.x:
                for ii in range(min(self.start.y, self.end.y), max(self.start.y, self.end.y)+1):
                    straight_range.append(Point(self.start.x, ii))
            else:
                for ii in range(min(self.start.x, self.end.x), max(self.start.x, self.end.x)+1):
                    straight_range.append(Point(ii, self.start.y))
        return straight_range

    def get_diagonal_range(self) -> List[Point]:
        d_range = []
        dx = 1 if self.end.x > self.start.x else -1
        dy = 1 if self.end.y > self.start.y else -1
        d_range.append(self.start)
        x = self.start.x
        y = self.start.y
        while x != self.end.x or y != self.end.y:
            x += dx
            y += dy
            d_range.append(Point(x, y))
        return d_range


def create_lines(data: List[str]) -> List[Vent]:
    result = []
    for row in data:
        start, end = row.split("->")
        start_points = start.split(",")
        s = Point(int(start_points[0]), int(start_points[1]))
        end_points = end.split(",")
        e = Point(int(end_points[0]), int(end_points[1]))
        result.append(Vent(s, e))
    return result


def check_overlapping(data: List[List]) -> (dict, int):
    overlaps = defaultdict(int)
    for l in data:
        for point in l:
            overlaps[point] += 1
    overlapping = len([k for k, v in overlaps.items() if v > 1])
    return overlaps, overlapping

if __name__ == "__main__":
    DATA = (FILE_DIR / "input.txt").read_text().strip()
    data = [x for x in DATA.split('\n')]
    vents = create_lines(data)
    lines = [v for v in vents if v.is_straight_line()]
    straight_ranges = [l.get_straight_range() for l in lines]
    overlap_dict, overlaps = check_overlapping(straight_ranges)
    #sol 1 4655
    print(overlaps)
    diag_lines = [v for v in vents if not v.is_straight_line()]
    diag_ranges = [l.get_diagonal_range() for l in diag_lines]
    all_ranges = straight_ranges + diag_ranges
    overlap_dict2, overlaps2 = check_overlapping(all_ranges)
    #sol 2 20500
    print(overlaps2)
