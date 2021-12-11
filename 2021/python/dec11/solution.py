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
            neighbors = []
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
        # FLASH
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

    test_outputs = create_map(test_data)
    counter = 0
    # sol 1
    for ii in range(1, 11):
        test_outputs = run_step(test_outputs)
        test_outputs, counter = run_flashes(test_outputs, counter)
    print("Test: ", counter)


    DATA = (FILE_DIR / "input.txt").read_text().strip()
    data = [x for x in DATA.split("\n")]
    seamap1 = create_map(data)
    counter = 0
    # sol 1
    for _ in range(1, 101):
        seamap1 = run_step(seamap1)
        seamap1, counter = run_flashes(seamap1, counter)
    
    print("Sol1:", counter)

    seamap2 = create_map(data)
    counter = 0
    # sol 2
    for ii in range(1, 10000):
        seamap2 = run_step(seamap2)
        seamap2, counter = run_flashes(seamap2, counter)
        if all([o.flashed for row in seamap2 for o in row]):
            print("Sol2:", ii)
            break