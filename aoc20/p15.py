from typing import TypeVar

from aoc20 import utils


T = TypeVar("T")


def nth_number(starting: list[int], n: int = 2020) -> int:
    *initial, value = starting
    indexes: dict[int, int] = {x: i + 1 for i, x in enumerate(initial)}  # 1-based
    turn = len(starting)
    for _ in range(n - len(starting)):
        if value in indexes:
            next_value = turn - indexes[value]
        else:
            next_value = 0
        indexes[value] = turn
        value = next_value
        turn += 1
    return value


def parse_input(lines: list[str]) -> list[int]:
    return [int(x) for x in lines[0].split(",")]


def main() -> None:
    numbers = parse_input(utils.read_input_lines(__file__))
    print(nth_number(numbers))
    print(nth_number(numbers, 30_000_000))


if __name__ == "__main__":
    main()
