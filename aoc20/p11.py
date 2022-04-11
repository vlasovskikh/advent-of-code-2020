import copy
import functools
import itertools
from typing import Callable, TypeVar, Iterable

from aoc20 import utils


Seats = list[list[str]]
T = TypeVar("T")


def adjacent(seats: Seats, i: int, j: int) -> Iterable[str]:
    n_rows, n_cols = len(seats), len(seats[0])
    for row in range(max(i - 1, 0), min(i + 2, n_rows)):
        for column in range(max(j - 1, 0), min(j + 2, n_cols)):
            if row == i and column == j:
                continue
            yield seats[row][column]


def visible(seats: Seats, i: int, j: int) -> Iterable[str]:
    n_rows, n_cols = len(seats), len(seats[0])
    directions = [
        itertools.zip_longest(range(i - 1, -1, -1), [], fillvalue=j),
        itertools.zip_longest(range(i + 1, n_rows), [], fillvalue=j),
        itertools.zip_longest([], range(j - 1, -1, -1), fillvalue=i),
        itertools.zip_longest([], range(j + 1, n_cols), fillvalue=i),
        zip(range(i - 1, -1, -1), range(j - 1, -1, -1)),
        zip(range(i - 1, -1, -1), range(j + 1, n_cols)),
        zip(range(i + 1, n_rows), range(j + 1, n_cols)),
        zip(range(i + 1, n_rows), range(j - 1, -1, -1)),
    ]
    for direction in directions:
        for row, column in direction:
            seat = seats[row][column]
            if seat == "#" or seat == "L":
                yield seat
                break


def occupied(seats: Iterable[str]) -> int:
    return sum(1 for seat in seats if seat == "#")


def show_seats(seats: Seats) -> str:
    return "\n".join("".join(row) for row in seats)


def seating_turn(use_visible: bool, seats: Seats) -> Seats:
    limit = 5 if use_visible else 4
    neighbors = visible if use_visible else adjacent
    result = copy.deepcopy(seats)
    for i, row in enumerate(seats):
        for j, seat in enumerate(row):
            if seat == "L" and occupied(neighbors(seats, i, j)) == 0:
                result[i][j] = "#"
            elif seat == "#" and occupied(neighbors(seats, i, j)) >= limit:
                result[i][j] = "L"
    return result


def fixed_point(f: Callable[[T], T], x: T) -> T:
    while (y := f(x)) != x:
        x = y
    return y


def count_occupied_seats(seats: Seats) -> int:
    return occupied(seat for row in seats for seat in row)


def count_seats_at_fixed_point(seats: Seats, *, use_visible: bool) -> int:
    final_seats = fixed_point(functools.partial(seating_turn, use_visible), seats)
    return count_occupied_seats(final_seats)


def parse_input(lines: list[str]) -> Seats:
    return [list(line) for line in lines]


def main() -> None:
    seats = parse_input(utils.read_input_lines(__file__))
    print(count_seats_at_fixed_point(seats, use_visible=False))
    print(count_seats_at_fixed_point(seats, use_visible=True))


if __name__ == "__main__":
    main()
