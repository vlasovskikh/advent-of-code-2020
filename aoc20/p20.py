import collections
import itertools
import math
import re
from typing import Iterable

import numpy as np

from aoc20 import utils

MONSTER = "                  # \n#    ##    ##    ###\n #  #  #  #  #  #   "


def all_edges(tile: np.ndarray) -> Iterable[tuple]:
    edges = tile[0, :], tile[:, 0], tile[-1, :], tile[:, -1]
    for edge in edges:
        yield tuple(edge)
        yield tuple(edge[::-1])


def edges_to_north(tile: np.ndarray) -> Iterable[tuple[tuple, int, bool]]:
    yield tuple(tile[0, :]), 0, False
    yield tuple(tile[:, 0]), 3, True
    yield tuple(tile[-1, :]), 2, True
    yield tuple(tile[:, -1]), 1, False
    yield tuple(tile[0, :][::-1]), 0, True
    yield tuple(tile[:, 0][::-1]), 3, False
    yield tuple(tile[-1, :][::-1]), 2, False
    yield tuple(tile[:, -1][::-1]), 1, True


def tile_edges(tile: np.ndarray) -> list[tuple]:
    return [tuple(t) for t in [tile[0, :], tile[:, -1], tile[-1, :], tile[:, 0]]]


def find_corners(neighbors: dict[int, set[int]]) -> list[int]:
    return [id_ for id_, ns in neighbors.items() if len(ns) == 2]


def find_neighbors(tiles: dict[int, np.ndarray]) -> dict[int, set[int]]:
    matching: dict[tuple, list[int]] = collections.defaultdict(list)
    neighbors: dict[int, set[int]] = collections.defaultdict(set)
    for id_, tile in tiles.items():
        for edge in all_edges(tile):
            matching[edge].append(id_)
    for edge, ids in matching.items():
        if len(ids) == 2:
            id1, id2 = ids
            neighbors[id1].add(id2)
            neighbors[id2].add(id1)
        elif len(ids) >= 3:
            raise ValueError(f"Got {len(ids)} matches for edge {edge}: {ids!r}")
    return neighbors


def multiply_corners(tiles: dict[int, np.ndarray]) -> int:
    return math.prod(find_corners(find_neighbors(tiles)))


def fit_to_match(tile: np.ndarray, other: np.ndarray) -> tuple[np.ndarray, int, int]:
    other = other.copy()
    to_match = {
        0: (2, True, 1),
        1: (1, True, 0),
        2: (0, False, 0),
        3: (3, False, 0),
    }
    coords = {
        0: (-1, 0),
        1: (0, 1),
        2: (1, 0),
        3: (0, -1),
    }
    for i, edge in enumerate(tile_edges(tile)):
        for other_edge, rot, flip in edges_to_north(other):
            if edge == other_edge:
                other = np.rot90(other, rot)
                if flip:
                    other = np.flip(other, axis=1)
                rot, flip, axis = to_match[i]
                other = np.rot90(other, rot)
                if flip:
                    other = np.flip(other, axis=axis)
                x, y = coords[i]
                return other, x, y
    raise ValueError(f"No match found for tiles:\n{tile}\nand:\n{other}")


def trim_tile(tile: np.ndarray) -> np.ndarray:
    return tile[1:-1, 1:-1]


def restore_image(tiles: dict[int, np.ndarray]) -> np.ndarray:
    parts: dict[tuple[int, int], np.ndarray] = {}
    neighbors = find_neighbors(tiles)
    corners = find_corners(neighbors)
    c = corners[0]
    queue: list[tuple[int, np.ndarray, int, int]] = [(c, tiles[c], 0, 0)]
    seen: set[int] = set()

    while queue:
        id_, tile, x, y = queue.pop()
        if id_ in seen:
            continue
        seen.add(id_)
        parts[(x, y)] = tile
        for neighbor in neighbors[id_]:
            if neighbor in seen:
                continue
            fitted, nx, ny = fit_to_match(tile, tiles[neighbor])
            if (x + nx, y + ny) == (0, 2):
                pass
            queue.insert(0, (neighbor, fitted, x + nx, y + ny))

    xs, ys = zip(*parts.keys())
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    shape_x, shape_y = trim_tile(tiles[c]).shape

    image = np.full((shape_x * (max_x - min_x + 1), shape_y * (max_y - min_y + 1)), 0)
    for i, x in enumerate(range(min_x, max_x + 1)):
        for j, y in enumerate(range(min_y, max_y + 1)):
            trimmed = trim_tile(parts[(x, y)])
            image[
                i * shape_x : (i + 1) * shape_x, j * shape_y : (j + 1) * shape_y
            ] = trimmed
    return image


def show_tile(tile: np.ndarray) -> str:
    def pixel(x):
        if x == 1:
            return "#"
        elif x == 2:
            return "O"
        else:
            return "."

    return "\n".join("".join(pixel(x) for x in row) for row in tile)


def highlight_sea_monsters(image: np.ndarray) -> np.ndarray:
    lines = MONSTER.strip().splitlines()
    monster_size = MONSTER.count("#")
    w, h = max(len(line) for line in lines), len(lines)
    pattern = np.array([[c == "#" for c in line] for line in MONSTER.splitlines()])
    view = image.copy()
    for flip in [False, True]:
        for rot in range(4):
            view = np.rot90(image, rot)
            if flip:
                view = np.flip(view, axis=0)
            height, width = view.shape
            for i in range(0, height - h + 1):
                for j in range(0, width - w + 1):
                    mask = np.full(view.shape, False)
                    mask[i : i + h, j : j + w] = pattern
                    masked = view[mask]
                    masked[masked == 2] = 1
                    if sum(masked) == monster_size:
                        view[mask] = 2
    return view


def water_roughness(tiles: dict[int, np.ndarray]) -> int:
    image = restore_image(tiles)
    highlighted = highlight_sea_monsters(image)
    return len(highlighted[highlighted == 1])


def parse_input(lines: list[str]) -> dict[int, np.ndarray]:
    result: dict[int, np.ndarray] = {}
    groups = [list(g) for k, g in itertools.groupby(lines, key=lambda x: x != "") if k]
    for group in groups:
        first, *rest = group
        if m := re.match(r"Tile (\d+):", first):
            id_ = int(m.group(1))
        else:
            raise ValueError(f"Unknown first line: {first!r}")
        array = np.array([[1 if c == "#" else 0 for c in row] for row in rest])
        result[id_] = array
    return result


def main() -> None:
    tiles = parse_input(utils.read_input_lines(__file__))
    print(multiply_corners(tiles))
    print(water_roughness(tiles))


if __name__ == "__main__":
    main()
