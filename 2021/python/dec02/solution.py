from dataclasses import dataclass, field
from pathlib import Path
from typing import List, NamedTuple

FILE_DIR = Path(__file__).parent


class Vector(NamedTuple):
    direction: str
    speed: int

class SubParser:
    def __init__(self, data):
        self.data = data
        self.vectors = self.get_vectors()
        self.position = self.follow_route()
        self.position2 = self.follow_route2()


    def get_vectors(self):
        vectors = []
        for pair in self.data:
            result = pair.split(" ")
            vectors.append(Vector(result[0], int(result[1])))
        return vectors

    def follow_route(self):
        x, y = (0, 0)
        for vect in self.vectors:
            if vect.direction == "forward":
                x += vect.speed
            if vect.direction == "up":
                y -= vect.speed
            if vect.direction == "down":
                y += vect.speed
        return x, y

    def follow_route2(self):
        x, y = (0, 0)
        aim = 0
        for vect in self.vectors:
            if vect.direction == "forward":
                x += vect.speed
                y += vect.speed * aim
            if vect.direction == "up":
                aim -= vect.speed
            if vect.direction == "down":
                aim += vect.speed
        return x, y


if __name__ == "__main__":
    DATA = (FILE_DIR / "input.txt").read_text().strip()
    data = [x for x in DATA.split('\n')]
    sub = SubParser(data)
    # solution 1
    print(sub.position[0] * sub.position[1])
    print(sub.position2[0] * sub.position2[1])