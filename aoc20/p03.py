import math

from aoc20 import utils


def count_trees(field: list[str], right: int, down: int) -> int:
    row, col, trees = 0, 0, 0
    n_rows = len(field)
    n_cols = len(field[0])
    while row < n_rows:
        if field[row][col] == "#":
            trees += 1
        row += down
        col = (col + right) % n_cols
    return trees


def check_slopes(field: list[str], slopes: list[tuple[int, int]]) -> int:
    return math.prod(count_trees(field, right, down) for right, down in slopes)


def parse_input(lines: list[str]) -> list[str]:
    return lines


def main() -> None:
    field = parse_input(utils.read_input_lines(__file__))
    print(count_trees(field, 3, 1))
    print(
        check_slopes(
            field,
            [
                (1, 1),
                (3, 1),
                (5, 1),
                (7, 1),
                (1, 2),
            ],
        )
    )


if __name__ == "__main__":
    main()
