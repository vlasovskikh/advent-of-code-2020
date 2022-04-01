import itertools
import math

from aoc20 import utils


def fix_expense_report(report: list[int], items_count: int) -> int:
    for items in itertools.combinations(report, items_count):
        if sum(items) == 2020:
            return math.prod(items)
    raise ValueError("No numbers add up to 2020")


def main() -> None:
    report = parse_input(utils.read_input_lines(__file__))
    print(fix_expense_report(report, 2))
    print(fix_expense_report(report, 3))


def parse_input(lines: list[str]) -> list[int]:
    return [int(line) for line in lines]


if __name__ == "__main__":
    main()
