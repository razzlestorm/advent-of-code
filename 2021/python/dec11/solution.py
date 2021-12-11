from pathlib import Path
from dataclasses import dataclass, field
from typing import List

FILE_DIR = Path(__file__).parent


@dataclass()
class Octopus:
    energy: int
    position: tuple
    flashed: bool = False
    neighbors: list = field(default_factory=list)

    def __repr__(self):
        return f"{self.energy}"


def create_map(data: List[str]):
    seamap = []
    for jj in range(len(data)):
        row = []
        for kk in range(len(data[0])):
            i = int(data[jj][kk])
            row.append(Octopus(i, (jj, kk)))
        seamap.append(row)
    for y in range(len(seamap)):
        for x in range(len(seamap[0])):
            for yy in [-1, 0, 1]:
                for xx in [-1, 0, 1]:
                    if (yy == 0 and xx == 0):
                        continue
                    y_cell = y+yy
                    x_cell = x+xx
                    if (y_cell >= 0 and x_cell >= 0) and (y_cell < len(seamap) and x_cell < len(seamap[y])):
                        if seamap[y + yy][x + xx] not in seamap[y][x].neighbors:
                            seamap[y][x].neighbors.append(seamap[y + yy][x + xx])
    return seamap


def check_energy(o: Octopus) -> bool:
    if o.energy > 9 and not o.flashed:
        return True
    return False


def run_step(data):
    for row in range(len(data)):
        for col in range(len(data[0])):
            data[row][col].energy += 1
            data[row][col].flashed = False
    return data


def run_flashes(data: List[Octopus], counter: int):
    """returns matrix and counter of flashes
    """
    for row in data:
        for octopus in row:
            if check_energy(octopus):
                counter += 1
                # reset after flash
                octopus.energy = 0
                octopus.flashed = True
                # transmit energy to neighbors
                for o in octopus.neighbors:
                    if not o.flashed:
                        o.energy += 1
                # rerun everything
                return run_flashes(data, counter)
    return data, counter


def cccombo_solver(data: List[list], steps: int) -> int:
    seamap = create_map(data)
    counter = 0
    for ii in range(steps):
        seamap = run_step(seamap)
        seamap, counter = run_flashes(seamap, counter)
        if all([o.flashed for row in seamap for o in row]):
            return ii
    return counter


if __name__ == "__main__":

    test_data = [
        "5483143223",
        "2745854711",
        "5264556173",
        "6141336146",
        "6357385478",
        "4167524645",
        "2176841721",
        "6882881134",
        "4846848554",
        "5283751526"
    ]

    print("Test1: ", cccombo_solver(test_data, 100))  # 1656
    print("Test2: ", cccombo_solver(test_data, 1000))  # 194

    DATA = (FILE_DIR / "input.txt").read_text().strip()
    data = [x for x in DATA.split("\n")]
    print("Sol1:", cccombo_solver(data, 100))  # 1647
    print("Sol2:", cccombo_solver(data, 1000))  # 348
