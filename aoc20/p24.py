from __future__ import annotations

import re
from dataclasses import dataclass, field
from enum import Enum
from typing import Iterator

from aoc20 import utils

Coords = tuple[int, int]


class Dir(Enum):
    W = 1
    E = 2
    NW = 3
    NE = 4
    SW = 5
    SE = 6

    @staticmethod
    def from_string(s: str) -> Dir:
        return Dir[s.upper()]


Path = list[Dir]


@dataclass
class Floor:
    black: set[Coords] = field(default_factory=set)

    @staticmethod
    def from_paths(paths: list[Path]) -> Floor:
        floor = Floor()
        for path in paths:
            floor.flip(path_to_coords(path))
        return floor

    def flip(self, coords: Coords) -> None:
        if coords in self.black:
            self.black.remove(coords)
        else:
            self.black.add(coords)

    def copy(self) -> Floor:
        return Floor(self.black.copy())

    @staticmethod
    def neighboring_coords(coords: Coords) -> set[Coords]:
        x1, y1 = coords
        return {(x1 + x2, y1 + y2) for x2, y2 in ALL_DIR_COORDS}

    def neighbors(self, coords: Coords) -> list[bool]:
        return [self[c] for c in self.neighboring_coords(coords)]

    def count_black_neighbors(self, coords: Coords) -> int:
        return sum(1 for n in self.neighbors(coords) if n)

    def __getitem__(self, item: Coords) -> bool:
        return item in self.black

    def __iter__(self) -> Iterator[Coords]:
        possible = set()
        possible |= self.black
        for coords in self.black:
            possible |= self.neighboring_coords(coords)
        return iter(possible)


def path_to_coords(path: Path) -> Coords:
    x, y = 0, 0
    for d in path:
        if d == Dir.W:
            x -= 1
        elif d == Dir.E:
            x += 1
        elif d == Dir.NW:
            y -= 1
        elif d == Dir.NE:
            x += 1
            y -= 1
        elif d == Dir.SW:
            x -= 1
            y += 1
        elif d == Dir.SE:
            y += 1
        else:
            raise ValueError(f"Unknown direction: {d}")
    return x, y


ALL_DIR_COORDS = [path_to_coords([d]) for d in Dir]


def simulate_living_art(paths: list[Path], days: int = 100) -> int:
    floor = Floor.from_paths(paths)
    for _ in range(days):
        new = floor.copy()
        for coords in floor:
            n = floor.count_black_neighbors(coords)
            if floor[coords] and (n == 0 or n > 2) or not floor[coords] and n == 2:
                new.flip(coords)
        floor = new
    return len(floor.black)


def count_black_tiles(paths: list[Path]) -> int:
    return len(Floor.from_paths(paths).black)


def parse_input(lines: list[str]) -> list[Path]:
    res = []
    for line in lines:
        res.append([Dir.from_string(s) for s in re.findall(r"(se|ne|sw|nw|e|w)", line)])
    return res


def main() -> None:
    paths = parse_input(utils.read_input_lines(__file__))
    print(count_black_tiles(paths))
    print(simulate_living_art(paths))


if __name__ == "__main__":
    main()
