import itertools
from typing import Iterator

from aoc20 import utils

Coords = tuple


class Space:
    def __init__(self, min_c: Coords, max_c: Coords) -> None:
        self.min_c = min_c
        self.max_c = max_c
        self.points: set[Coords] = set()

    def __getitem__(self, item: Coords) -> bool:
        return item in self.points

    def __setitem__(self, key: Coords, value: bool) -> None:
        if value:
            self.points.add(key)
        elif key in self.points:
            self.points.remove(key)

    def __iter__(self) -> Iterator[Coords]:
        ranges = [range(start, stop) for start, stop in zip(self.min_c, self.max_c)]
        return (x for x in itertools.product(*ranges))

    def __len__(self) -> int:
        return len(self.points)

    @staticmethod
    def neighbors(coords: Coords) -> list[Coords]:
        ranges = [range(coord - 1, coord + 2) for coord in coords]
        return [x for x in itertools.product(*ranges) if x != coords]

    def count_active(self, coords: Coords) -> int:
        return sum(1 for neighbor in self.neighbors(coords) if self[neighbor])

    def reshape(self, dims: int) -> "Space":
        diff = dims - len(self.min_c)
        new_min = *self.min_c, *([0] * diff)
        new_max = *self.max_c, *([1] * diff)
        space = Space(new_min, new_max)
        for coords in self:
            new_coords = *coords, *([0] * diff)
            space[new_coords] = self[coords]
        return space


def simulate(initial: Space, dims: int, cycles: int = 6) -> int:
    prev = space = initial.reshape(dims)
    for _ in range(cycles):
        min_c = tuple(x - 1 for x in prev.min_c)
        max_c = tuple(x + 1 for x in prev.max_c)
        space = Space(min_c, max_c)
        for coords in space:
            active = prev.count_active(coords)
            if prev[coords]:
                space[coords] = active == 2 or active == 3
            else:
                space[coords] = active == 3
        prev = space
    return len(space)


def parse_input(lines: list[str]) -> Space:
    table: list[list[bool]] = []
    for line in lines:
        table.append([c == "#" for c in line])
    space = Space((0, 0), (len(table), len(table[0])))
    for i, row in enumerate(table):
        for j, value in enumerate(row):
            space[(i, j)] = value
    return space


def main() -> None:
    initial = parse_input(utils.read_input_lines(__file__))
    print(simulate(initial, 3))
    print(simulate(initial, 4))


if __name__ == "__main__":
    main()
