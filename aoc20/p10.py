from itertools import groupby
from math import comb, prod
from aoc20 import utils


def sort_adapters(adapters: list[int]) -> int:
    xs = sorted(adapters)
    xs.insert(0, 0)
    xs.append(xs[-1] + 3)
    ones, threes = 0, 0
    for x, y in utils.sliding_window(xs, 2):
        diff = y - x
        if diff == 1:
            ones += 1
        elif diff == 3:
            threes += 1
    return ones * threes


def count_combinations(adapters: list[int]) -> int:
    xs = sorted(adapters)
    xs.insert(0, 0)
    xs.append(xs[-1] + 3)
    diffs = (y - x for x, y in utils.sliding_window(xs, 2))
    ones = [len(list(g)) for e, g in groupby(diffs) if e == 1]
    return prod(all_comb(x - 1) - (x - 1) // 3 for x in ones)


def all_comb(n):
    return sum(comb(n, i) for i in range(n + 1))


def parse_input(lines: list[str]) -> list[int]:
    return [int(line) for line in lines]


def main() -> None:
    numbers = parse_input(utils.read_input_lines(__file__))
    print(sort_adapters(numbers))
    print(count_combinations(numbers))


if __name__ == "__main__":
    main()
