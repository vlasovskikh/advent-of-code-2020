from __future__ import annotations

import functools
import math
import operator
from collections import defaultdict
from dataclasses import dataclass
from typing import NamedTuple, TypeVar, Iterable

from aoc20 import utils

T = TypeVar("T")


class Range(NamedTuple):
    start: int
    stop: int


@dataclass
class Interval:
    ranges: list[Range]

    def __or__(self, other: Interval) -> Interval:
        ranges = self.ranges.copy()
        ranges.extend(other.ranges)
        return Interval(ranges)

    def __contains__(self, item: int) -> bool:
        return any(start <= item <= stop for start, stop in self.ranges)


class Data(NamedTuple):
    rules: dict[str, Interval]
    your: list[int]
    nearby: list[list[int]]


def uber_interval(data: Data) -> Interval:
    return functools.reduce(operator.or_, data.rules.values())


def nearby_error_rate(data: Data) -> int:
    interval = uber_interval(data)
    values = (x for ticket in data.nearby for x in ticket)
    return sum(x for x in values if x not in interval)


def table_column(table: list[list[T]], index: int) -> Iterable[T]:
    for row in table:
        yield row[index]


def restore_your_ticket(data: Data) -> dict[str, int]:
    tickets = [data.your]
    tickets.extend(data.nearby)
    uber = uber_interval(data)
    valid = [ticket for ticket in tickets if all(x in uber for x in ticket)]
    n_cols = len(data.your)
    rules = data.rules.copy()
    possible_indexes: dict[int, set[str]] = defaultdict(set)
    for i in range(n_cols):
        column = list(table_column(valid, i))
        for name, interval in rules.items():
            if all(x in interval for x in column):
                possible_indexes[i].add(name)
    final_indexes: dict[int, str] = {}
    for _ in range(len(possible_indexes)):
        i, name = next(
            (i, list(names)[0])
            for i, names in possible_indexes.items()
            if len(names) == 1
        )
        final_indexes[i] = name
        for names in possible_indexes.values():
            names.discard(name)
    return {final_indexes[i]: value for i, value in enumerate(data.your)}


def departure_product(data: Data) -> int:
    ticket = restore_your_ticket(data)
    return math.prod(v for k, v in ticket.items() if k.startswith("departure"))


def parse_input(lines: list[str]) -> Data:
    rules: dict[str, Interval] = {}
    your: list[int] = []
    nearby: list[list[int]] = []
    state: str = "rules"
    for line in lines:
        if line == "your ticket:":
            state = "your"
        elif line == "nearby tickets:":
            state = "nearby"
        elif line:
            if state == "rules":
                k, v = line.split(": ")
                ranges: list[Range] = []
                for r in v.split(" or "):
                    start, stop = r.split("-")
                    ranges.append(Range(int(start), int(stop)))
                rules[k] = Interval(ranges)
            elif state == "your":
                your.extend([int(x) for x in line.split(",")])
            elif state == "nearby":
                nearby.append([int(x) for x in line.split(",")])
            else:
                raise ValueError(f"Unknown state: {state!r}")
    return Data(rules, your, nearby)


def main() -> None:
    data = parse_input(utils.read_input_lines(__file__))
    print(nearby_error_rate(data))
    print(departure_product(data))


if __name__ == "__main__":
    main()
