import itertools
from aoc20 import utils


def first_sum_mismatch(numbers: list[int], window: int = 25) -> int:
    for chunk in utils.sliding_window(numbers, window + 1):
        *rest, last = chunk
        if not any(
            x + y == last and x != y for x, y in itertools.combinations(rest, 2)
        ):
            return last
    raise ValueError("Mismatch not found")


def find_contiguous_weakness(numbers: list[int], x: int) -> int:
    for end in range(len(numbers)):
        for start in range(end):
            xs = numbers[start:end]
            if sum(xs) == x:
                return min(xs) + max(xs)
    raise ValueError("Weakness not found")


def parse_input(lines: list[str]) -> list[int]:
    return [int(line) for line in lines]


def main() -> None:
    numbers = parse_input(utils.read_input_lines(__file__))
    mismatch = first_sum_mismatch(numbers)
    print(mismatch)
    print(find_contiguous_weakness(numbers, mismatch))


if __name__ == "__main__":
    main()
