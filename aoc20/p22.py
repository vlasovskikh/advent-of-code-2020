from collections import deque
from itertools import groupby, islice

from aoc20 import utils


def play_crab_combat(p1: list[int], p2: list[int]) -> int:
    d1, d2 = deque(p1), deque(p2)
    while d1 and d2:
        c1, c2 = d1.popleft(), d2.popleft()
        w = d1 if c1 > c2 else d2
        w.extend([c1, c2] if w == d1 else [c2, c1])
    w = d1 or d2
    return sum(i * c for i, c in enumerate(reversed(w), 1))


def recursive_game(d1: deque[int], d2: deque[int]) -> tuple[bool, int]:
    seen: set[tuple[int, ...]] = set()
    w: deque[int]
    while d1 and d2:
        t1, t2 = tuple(d1), tuple(d2)
        if t1 in seen or t2 in seen:
            return True, 0
        seen |= {t1, t2}
        c1, c2 = d1.popleft(), d2.popleft()
        if len(d1) >= c1 and len(d2) >= c2:
            won, _ = recursive_game(deque(islice(d1, 0, c1)), deque(islice(d2, 0, c2)))
            w = d1 if won else d2
        else:
            w = d1 if c1 > c2 else d2
        w.extend([c1, c2] if w == d1 else [c2, c1])
    w = d1 or d2
    return w == d1, sum(i * c for i, c in enumerate(reversed(w), 1))


def play_recursive_combat(p1: list[int], p2: list[int]) -> int:
    _, score = recursive_game(deque(p1), deque(p2))
    return score


def parse_input(lines: list[str]) -> tuple[list[int], list[int]]:
    groups = [list(g) for k, g in groupby(lines, key=lambda line: line != "") if k]
    p1, p2 = [[int(x) for x in g[1:]] for g in groups if g]
    return p1, p2


def main() -> None:
    args = parse_input(utils.read_input_lines(__file__))
    print(play_crab_combat(*args))
    print(play_recursive_combat(*args))


if __name__ == "__main__":
    main()
